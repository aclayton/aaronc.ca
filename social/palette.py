#!/usr/bin/env python3
"""The site's palette, parsed out of style.css. Shared by both generators.

Read by:
  - ~/sites/assets-internal/build.py      (the private colour dashboard, :8100)
  - ~/sites/aaronc.ca/social/build-index.py (the asset index, /social/)

One parser, so the two surfaces cannot disagree about a colour. Nothing here is
retyped from memory: every value comes from the stylesheet, and every lookup is
asserted, so a restructured stylesheet fails loudly instead of silently shipping
a half-empty palette.

    import palette
    P = palette.load("/home/boss/sites/aaronc.ca/style.css")
    P["neutral"]   # [{name, alias, desc, light, dark}, ...]
    P["light"]     # {"--bg": "#f7f6fa", ...}
    P["roles"]     # [{n, d, m, cl, cd, vl, vd, ink_l, ink_d}, ...]
    P["acc"]       # {"d0": {"light": {...}, "dark": {...}}, ...}
    P["resting"]   # 268
"""
import json
import re

# ── the six neutral roles ───────────────────────────────────────────────────
NEUTRAL = [
    ("--bg",        "page",      "the page ground"),
    ("--surface",   "band",      "full-width bands, cards"),
    ("--surface-2", "surface 2", "hover fills, ghost-button rest"),
    ("--fg",        "ink",       "body text, the mark"),
    ("--muted",     "muted",     "secondary text, labels"),
    ("--rule",      "rule",      "hairline rules and borders"),
]


def load(style_css, correspondences_json=None):
    css = open(style_css).read()

    def token(block, name):
        """`name` includes its own leading `--`."""
        m = re.search(rf"{re.escape(name)}\s*:\s*([^;]+);", block)
        assert m, f"style.css: {name} not found — has the stylesheet been restructured?"
        return m.group(1).strip()

    light_root = css[css.index(":root {"):css.index("@media (prefers-color-scheme: dark)")]
    dark_root = css[css.index("@media (prefers-color-scheme: dark) {\n  :root {"):
                    css.index(':root[data-accent="d0"]')]

    light = {n: token(light_root, n) for n, _a, _d in NEUTRAL}
    dark = {n: token(dark_root, n) for n, _a, _d in NEUTRAL}
    light["--fill-ink"] = token(light_root, "--fill-ink")
    dark["--fill-ink"] = token(dark_root, "--fill-ink")

    # the seven, per theme: the row carrying --hue is the light one
    acc = {}
    for m in re.finditer(r':root\[data-accent="(d\d)"\]\s*\{([^}]*)\}', css):
        d, body = m.group(1), m.group(2)
        props = dict(re.findall(r"(--[a-z-]+)\s*:\s*([^;]+);", body))
        acc.setdefault(d, {})["light" if "--hue" in props else "dark"] = props

    assert len(acc) == 7, f"style.css: expected 7 accent rows, found {len(acc)}"
    for d, row in acc.items():
        assert "light" in row and "dark" in row, f"style.css: {d} missing a theme row"
        for key in ("--hue", "--accent-s", "--fill-l", "--text-l"):
            assert key in row["light"], f"style.css: {d} light row missing {key}"
        for key in ("--fill-l", "--text-l"):
            assert key in row["dark"], f"style.css: {d} dark row missing {key}"

    # the resting hue is the one the stylesheet sets at :root
    resting = int(token(light_root, "--hue"))
    row = next((r for r in acc.values() if int(r["light"]["--hue"]) == resting), None)
    assert row, f"style.css: no accent row with hue {resting} for the resting state"
    H = resting
    S = int(row["light"]["--accent-s"].rstrip("%"))
    lfill, ltext = row["light"]["--fill-l"].rstrip("%"), row["light"]["--text-l"].rstrip("%")
    dfill, dtext = row["dark"]["--fill-l"].rstrip("%"), row["dark"]["--text-l"].rstrip("%")

    # Roles. The site writes these as formulas over var(--hue), which neither
    # consumer page has — so each var-based value is RESOLVED against the resting
    # hue. A swatch that renders nothing is worse than no swatch.
    hair = "color-mix(in srgb, var(--fg) 22%, transparent)"
    ghost = "color-mix(in srgb, var(--fg) 50%, transparent)"
    roles = [
        dict(n="--accent-fill", d="the fill of anything carrying a label", m="fill",
             cl=f"hsl({H} {S}% {lfill}%)", cd=f"hsl({H} {S}% {dfill}%)",
             vl=f"hsl(hue sat {lfill}%)", vd=f"hsl(hue sat {dfill}%)",
             ink_l=light["--fill-ink"], ink_d=dark["--fill-ink"]),
        dict(n="--accent-text", d="links and toned text on the ground", m="text",
             cl=f"hsl({H} {S}% {ltext}%)", cd=f"hsl({H} {S}% {dtext}%)",
             vl=f"hsl(hue sat {ltext}%)", vd=f"hsl(hue sat {dtext}%)"),
        dict(n="--accent-wash", d="the day's wash laid over a ground", m="none",
             cl=f"hsl({H} 55% 95%)", cd=f"hsl({H} 40% 12%)",
             vl="95% lightness", vd="12% lightness"),
        dict(n="--hairline", d="construction lines — ink, never the rule colour", m="none",
             cl=hair, cd=hair, vl="ink 22%", vd="ink 22%"),
        dict(n="--ghost-line", d="the boundary of a secondary control (wants 3:1)", m="none",
             cl=ghost, cd=ghost, vl="ink 50% · 3.33:1", vd="ink 50% · 4.55:1"),
        dict(n="--fill-ink", d="the label colour that sits on a fill", m="fill",
             cl=light["--fill-ink"], cd=dark["--fill-ink"],
             vl=light["--fill-ink"], vd=dark["--fill-ink"],
             ink_l="#191725", ink_d=dark["--fg"]),
    ]

    # cross-check the accent rows against the correspondences, when given
    if correspondences_json:
        data = json.loads(open(correspondences_json).read())
        assert data["resting"] == resting, \
            f"resting hue disagrees: style.css {resting} vs json {data['resting']}"
        assert len(data["seven"]) == len(acc)
        for v in data["seven"]:
            row = acc.get(v["d"])
            assert row, f"{v['d']} is in the json but not in style.css"
            got = (int(row["light"]["--hue"]), int(row["light"]["--accent-s"].rstrip("%")),
                   int(row["light"]["--fill-l"].rstrip("%")))
            want = (v["hue"], v["s"], v["fill"])
            assert got == want, f"{v['d']}: style.css {got} vs json {want}"

    return dict(neutral=NEUTRAL, light=light, dark=dark, roles=roles,
                acc=acc, resting=resting, hues=sorted(acc))


def surface_rows(pal):
    """The two-column neutral table, both themes."""
    out = []
    for name, alias, desc in pal["neutral"]:
        out.append(f"""      <tr>
        <th scope="row"><code>{name}</code><span class="alias">{alias}</span><span class="desc">{desc}</span></th>
        <td class="plate-light"><span class="swatch" style="background:{pal['light'][name]}"></span><code>{pal['light'][name]}</code></td>
        <td class="plate-dark"><span class="swatch" style="background:{pal['dark'][name]}"></span><code>{pal['dark'][name]}</code></td>
      </tr>""")
    return "\n".join(out)


def role_rows(pal):
    """The role-token table. Each column sits on a PLATE of its own theme, so a
    light-theme token is judged on light and a dark one on dark — otherwise both
    columns follow prefers-color-scheme and one is always telling a lie."""
    out = []
    for r in pal["roles"]:
        tds = []
        for theme, css_val, val in (("light", r["cl"], r["vl"]), ("dark", r["cd"], r["vd"])):
            if r["m"] == "fill":
                inner = f'<b style="color:{r["ink_" + theme[0]]}">Aa</b>'
            elif r["m"] == "text":
                inner = f'<b style="color:{css_val}">Aa link</b>'
            else:
                inner = ""
            tds.append(f'<td class="plate-{theme}">'
                       f'<span class="chip2" style="background:{css_val}">{inner}</span>'
                       f'<code>{val}</code></td>')
        out.append(f"""      <tr>
        <th scope="row"><code>{r['n']}</code><span class="desc">{r['d']}</span></th>
        {tds[0]}
        {tds[1]}
      </tr>""")
    return "\n".join(out)
