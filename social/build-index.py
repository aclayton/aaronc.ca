#!/usr/bin/env python3
"""Emit social/index.html.

The mark's `d` attribute is a long opaque string that has to be byte-exact, and
retyping it is how it gets silently truncated. So it is taken from logo.svg and
asserted token-for-token, and the hue list is read from profile.css rather than
duplicated. The output is a plain hand-editable HTML file; the site still has no
build step.
"""
import json
import re
from pathlib import Path

SITE = Path("/home/boss/sites/aaronc.ca")
SOCIAL = SITE / "social"

# ── the mark, from its single source of truth ────────────────────────────────
svg = (SITE / "logo.svg").read_text()
logo_d = re.search(r'd="([^"]+)"', svg, re.S).group(1)

# The single-line form the render sources already use, proven by their renders.
MARK = ("M18,0v144h156.02H234V0H18z M134.625,5.76c-11.049,4.608-20.677,12.123"
        "-28.068,21.392L94.207,5.76H134.625z M23.76,5.76h63.796L23.76,114.156V5.76z "
        "M23.76,138.24v-12.564L90.44,11.232l73.603,127.008H23.76z M228.24,138.24h"
        "-37.131c8.688-4.032,16.502-9.352,23.037-15.979l-5.17-3.13c-10.599,10.28-"
        "24.039,16.538-38.531,18.176L109.666,31.996c1.927-2.587,4.054-5.07,6.376-"
        "7.392c12.512-12.512,29.146-19.41,46.838-19.41c17.347,0,33.673,6.622,"
        "46.096,18.671l5.17-2.699c-6.527-6.621-14.328-11.95-23.005-15.406h"
        "37.099V138.24z")

strip = lambda s: re.sub(r"\s+", "", s)
assert strip(MARK) == strip(logo_d), "the inlined mark does not match logo.svg"
print(f"  mark verified against logo.svg ({len(strip(MARK))} chars, identical)")

# ── the hue list, from the stylesheet rather than a second copy ─────────────
css = (SOCIAL / "profile.css").read_text()
hues = [(int(h), int(s), int(l)) for _i, h, s, l in
        re.findall(r"\.h(\d)\{ --hue:\s*(\d+); --accent-s:\s*(\d+)%; --fill-l:\s*(\d+)%; \}", css)]
print(f"  hues read from profile.css: {[h for h, _s, _l in hues]}")

# ── the correspondences, from the same file the private dashboard reads ─────
# DELIBERATE RISK, and why the guard exists:
#   The standing rule is that the hue numbers are public and the reason for them
#   is not. Dude asked for the correspondences on this page anyway (2026-11-16).
#   This page lives in the DEPLOYABLE tree, so netlify.toml forces /social/* to
#   a 404 — the whole directory is a working directory (render sources, build
#   scripts) that should never be served. Without that rule, deploying the site
#   would publish the day and planet names permanently.
CORRESP = json.loads((Path("/home/boss/sites/assets-internal/correspondences.json")).read_text())
by_hue = {v["hue"]: v for v in CORRESP["seven"]}
RESTING = CORRESP["resting"]

for h, s, l in hues:
    v = by_hue.get(h)
    assert v, f"hue {h} present in profile.css but missing from correspondences.json"
    assert (s, l) == (v["s"], v["fill"]), \
        f"hue {h}: profile.css says s={s}% fill={l}%, correspondences.json says " \
        f"s={v['s']}% fill={v['fill']}% — re-solve before shipping"
print(f"  correspondences cross-checked against profile.css: {len(hues)} hues agree")

# ── the palette — ONE shared parser, so this page and the private dashboard at
# :8100 cannot disagree about a colour. It reads style.css and asserts every
# lookup, and it cross-checks the accent rows against the correspondences file.
import sys
sys.path.insert(0, str(SOCIAL))
import palette                                              # noqa: E402

CORRESP_PATH = Path("/home/boss/sites/assets-internal/correspondences.json")
P = palette.load(SITE / "style.css", CORRESP_PATH)
ACC = P["acc"]
print(f"  palette: {len(P['neutral'])} neutral roles x 2 themes, {len(P['roles'])} role tokens")

# ── platform marks — third-party brand colours, a DELIBERATE departure ──────
# The system's palette is six neutrals and one rotating accent; these are other
# people's colours, used because the point is to sit beside a platform's chrome.
# Nothing here belongs in style.css. The brand table and the WCAG maths are
# shared with build-platforms.py so the two pages cannot disagree.
import contrast                                             # noqa: E402

BRANDS = json.loads((SOCIAL / "brands.json").read_text())["brands"]
print(f"  brands: {len(BRANDS)} (from brands.json)")


def platform_slug(n):
    return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")


def platform_card(b):
    name, hex_, src = b["name"], b["hex"], b["src"]
    sl = platform_slug(name)
    mark, ratio = contrast.best_on(hex_)
    ok = ratio >= 3.0
    return f"""
        <article class="asset" data-platform="{sl}">
          <div class="pair">
            <img class="rnd" src="platform-round-{sl}-460.png" alt="Round crop of the mark on the {name} brand field." width="460" height="460" loading="lazy" decoding="async">
            <img src="platform-{sl}-460.png" alt="The mark reversed out of the {name} brand field." width="460" height="460" loading="lazy" decoding="async">
          </div>
          <h3>{name}</h3>
          <p class="meta">
            <span class="hexchip" style="background:{hex_}"></span><code>{hex_}</code>
            <span class="ratio {'ok' if ok else 'no'}">{mark} · {ratio:.2f}:1</span>
          </p>
          <p class="stack">920 · 460 · round 920 · round 460</p>
          <ul class="dl">
            <li><a href="platform-{sl}-920.png" download>920</a></li>
            <li><a href="platform-{sl}-460.png" download>460</a></li>
            <li><a href="platform-round-{sl}-920.png" download>round 920</a></li>
            <li><a href="platform-round-{sl}-460.png" download>round 460</a></li>
          </ul>
          <p class="note">{src}.</p>
        </article>"""


def solved(v):
    """The four solved surfaces for this hue. The two 'text' chips sit on their own
    theme's plate — otherwise a dark-theme text colour gets judged against a light
    ground whenever the reader happens to be in light mode."""
    h, s = v["hue"], v["s"]
    L, D = ACC[v["d"]]["light"], ACC[v["d"]]["dark"]
    lf, df = L["--fill-l"].rstrip("%"), D["--fill-l"].rstrip("%")
    lt, dt = L["--text-l"].rstrip("%"), D["--text-l"].rstrip("%")
    out = []
    for cap, bg, fg, val in (
            ("light fill", f"hsl({h} {s}% {lf}%)", P["light"]["--fill-ink"], L["--fill-l"]),
            ("dark fill", f"hsl({h} {s}% {df}%)", P["dark"]["--fill-ink"], D["--fill-l"]),
            ("light text", P["light"]["--bg"], f"hsl({h} {s}% {lt}%)", L["--text-l"]),
            ("dark text", P["dark"]["--bg"], f"hsl({h} {s}% {dt}%)", D["--text-l"])):
        out.append(f'            <span class="chipset">'
                   f'<span class="chip2" style="background:{bg};color:{fg}"><b>Aa</b></span>'
                   f'<span class="capl">{cap} {val}</span></span>')
    return ('          <div class="chips">\n' + "\n".join(out) + "\n          </div>")


def hue_card(v):
    h = v["hue"]
    label = f"{h:03d} <span class=\"note\">— {v['planet']}</span>"
    if h == RESTING:
        label += ' <span class="note">· resting</span>'
    alt = f"Round crop of the mark on the hue {h:03d} field."
    alt2 = f"The mark reversed out of the hue {h:03d} field."
    return f"""
        <article class="asset" data-hue="{h}">
          <div class="pair">
            <img class="rnd" src="profile-round-hue-{h:03d}-460.png" alt="{alt}" width="460" height="460" loading="lazy" decoding="async">
            <img src="profile-hue-{h:03d}-460.png" alt="{alt2}" width="460" height="460" loading="lazy" decoding="async">
          </div>
          <h3>{label}</h3>
          <p class="stack">920 · 460 · round 920 · round 460</p>
{solved(v)}
          <dl class="cresp">
            <dt>day</dt><dd>{v['day']}</dd>
            <dt>colour</dt><dd>{v['colour']}</dd>
            <dt>incense</dt><dd>{v['incense']}</dd>
            <dt>god-name</dt><dd>{v['god']}</dd>
            <dt>tarot</dt><dd>{v['tarot']}</dd>
            <dt>sephira</dt><dd>{v['sphere']}</dd>
            <dt>path</dt><dd>{v['path']}</dd>
          </dl>
          <ul class="dl">
            <li><a href="profile-hue-{h:03d}-920.png" download>920</a></li>
            <li><a href="profile-hue-{h:03d}-460.png" download>460</a></li>
            <li><a href="profile-round-hue-{h:03d}-920.png" download>round 920</a></li>
            <li><a href="profile-round-hue-{h:03d}-460.png" download>round 460</a></li>
          </ul>
        </article>"""

PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Profile &amp; social assets — Aaron Clayton</title>
<meta name="description" content="Profile pictures and social cards, rendered from the mark at 2x and measured against the pixels.">
<!-- This page lives inside the deployable site directory but is for local use.
     If this directory is ever published, exclude social/ first. -->
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/style.css">

<style>
  /* Page-scoped: the asset index. Every value comes from the site's own tokens
     and its spacing sequence. Nothing new is introduced. */
  .assets {{
    display: grid; gap: var(--s4);
    grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
    margin-top: var(--s4);
  }}
  .assets > * {{ min-width: 0; }}

  .asset {{
    display: flex; flex-direction: column; gap: var(--s2);
    padding: var(--s3);
    border: 1px solid var(--rule); border-radius: var(--s1);
    background: var(--bg);
  }}
  /* the square alongside its round crop, so the crop is judged, not imagined */
  .pair {{ display: grid; grid-template-columns: 1fr 1fr; gap: var(--s2); }}
  .pair img, .asset.wide img {{
    display: block; width: 100%; height: auto;
    object-fit: contain;
    border: 1px solid var(--rule); border-radius: var(--s1);
  }}
  .pair img {{ aspect-ratio: 1; }}
  .pair .rnd {{ border-radius: 50%; }}
  .asset.wide img {{ aspect-ratio: 2; }}
  .asset h3 {{ margin: 0; }}
  .asset p {{ margin: 0; }}
  .asset .stack {{ font-family: var(--font-mono); font-size: var(--t-small); color: var(--muted); }}

  .dl {{ list-style: none; display: flex; flex-wrap: wrap; gap: var(--s1) var(--s3);
        padding: 0; margin: var(--s1) 0 0; }}
  .dl li {{ margin: 0; font-family: var(--font-mono); font-size: var(--t-small); }}

  /* the correspondences inside each accent card */
  dl.cresp {{ display: grid; grid-template-columns: auto 1fr; gap: .1rem var(--s2);
             margin: 0; font-size: var(--t-small); }}
  dl.cresp dt {{ color: var(--muted); white-space: nowrap; }}
  dl.cresp dd {{ margin: 0; }}

  /* the palette tables — identical markup to the private dashboard, one parser */
  table.pal {{ width: 100%; border-collapse: collapse; font-size: var(--t-small); }}
  table.pal th, table.pal td {{ text-align: left; vertical-align: middle;
    padding: var(--s2) var(--s3); border-bottom: 1px solid var(--rule); }}
  table.pal thead th {{ font-size: .6875rem; font-weight: 600; letter-spacing: .1em;
    text-transform: uppercase; color: var(--muted); border-bottom: 1px solid var(--fg); }}
  table.pal th[scope=row] {{ font-weight: 400; }}
  table.pal code {{ font-family: var(--font-mono); font-size: .75rem; }}
  .alias {{ display: block; margin-top: .1rem; }}
  .desc {{ display: block; color: var(--muted); font-size: .75rem; }}
  table.pal td code {{ display: block; margin-top: .25rem; color: var(--muted); }}
  .swatch {{ display: block; height: 26px; border-radius: var(--s1);
             border: 1px solid color-mix(in srgb, currentColor 18%, transparent); }}
  /* Each column sits on its own theme's plate, so a light token is judged on
     light and a dark one on dark. Both columns follow prefers-color-scheme
     otherwise, and one of them is then always telling a lie. */
  .plate-light {{ background: #f7f6fa; color: #191725; }}
  .plate-dark  {{ background: #0b0910; color: #e9e6f2; }}
  .plate-light code, .plate-dark code {{ color: color-mix(in srgb, currentColor 62%, transparent); }}
  .chip2 {{ display: grid; place-items: center; min-height: 34px; width: 100%;
            border-radius: var(--s1);
            border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
            font-size: var(--t-small); }}
  .chips {{ display: grid; grid-template-columns: 1fr 1fr; gap: var(--s2); }}
  .chipset {{ display: block; min-width: 0; }}
  .capl {{ display: block; color: var(--muted); font-size: .6875rem;
           font-family: var(--font-mono); margin-top: .25rem; }}

  /* platform marks — brand colour chip + the solved contrast for the mark */
  .asset .meta {{ display: flex; align-items: center; gap: var(--s2); margin: 0;
                  font-size: var(--t-small); flex-wrap: wrap; }}
  .hexchip {{ display: inline-block; width: 18px; height: 18px; border-radius: 4px;
              border: 1px solid var(--rule); }}
  .asset .meta code {{ font-family: var(--font-mono); font-size: .75rem; }}
  .ratio {{ font-family: var(--font-mono); font-size: .6875rem; font-weight: 600; }}
  .ratio.ok {{ color: #1b5e20; }}
  .ratio.no {{ color: #8c1d18; }}
  @media (prefers-color-scheme: dark) {{
    .ratio.ok {{ color: #81c784; }} .ratio.no {{ color: #ff8a80; }}
  }}
</style>
</head>

<body>
<a class="skip" href="#main">Skip to content</a>

<header class="site">
  <nav aria-label="Main">
    <a class="brand" href="/">Aaron Clayton</a>
    <ul>
      <li><a href="/">Site</a></li>
      <li><a href="#palette">Palette</a></li>
      <li><a href="platforms.html">Marks</a></li>
    </ul>
  </nav>
</header>

<main id="main">

  <section class="hero">
    <p class="eyebrow">Local · tailnet only</p>
    <h1>Profile &amp; social assets</h1>
    <p class="lede">The whole palette, the mark at every size the profiles need, and all seven accent fields. Rendered at 2&times;, then decoded and measured — not judged by eye.</p>
    <div class="cta">
      <a class="btn" href="profile-assets-2026-11-16.zip" download>Download all (zip)</a>
      <a class="btn ghost" href="/">Back to the site</a>
    </div>
    <p class="note" style="margin-top:var(--s3)">Every tile shows the square beside its round crop. <strong>GitHub, X and LinkedIn crop the square for you — upload the square.</strong> The round files have a transparent background, for surfaces that want a circle cut in the artwork: decks, documents, favicons.</p>
    <p class="note">Each accent field also carries what it corresponds to. <strong>This page is local-only and must never be published</strong> — it sits in the deployable tree, so <span class="nowrap">netlify.toml</span> forces <span class="nowrap">/social/*</span> to a 404 to keep the names off the live site.</p>
    <p class="note">On this page: <a href="#palette">the palette</a> ·
      <a href="#neutral">neutral grounds</a> ·
      <a href="platforms.html">platform-coloured marks</a> ·
      <a href="#hues">accent fields</a> ·
      <a href="#card">social card</a> ·
      <a href="#checked">what was measured</a>.</p>
  </section>

  <section id="palette">
    <h2>The palette</h2>
    <p>Every colour token in the system, parsed out of <span class="nowrap">style.css</span> each time this page is built. Nothing here is copied by hand, so a token added there appears here — and the same parser feeds the private dashboard, so the two cannot disagree.</p>

    <h3>Neutral surfaces</h3>
    <p class="note">Six roles, two themes. A cool neutral ground tinted toward the violet passage.</p>
    <table class="pal">
      <thead><tr><th>role</th><th>light</th><th>dark</th></tr></thead>
      <tbody>
{palette.surface_rows(P)}
      </tbody>
    </table>

    <h3>Role tokens</h3>
    <p class="note">Derived, not literal — each is a formula over the day's hue, so all seven hues are solved to equal contrast. Sampled on the resting hue ({RESTING}). Each column sits on a plate of its own theme, because both columns would otherwise follow the reader's theme and one of them would be telling a lie.</p>
    <table class="pal">
      <thead><tr><th>token</th><th>light</th><th>dark</th></tr></thead>
      <tbody>
{palette.role_rows(P)}
      </tbody>
    </table>
  </section>

  <section id="neutral">
    <h2>Neutral grounds</h2>
    <p>No colour of their own beyond the tonal field. For where the surface should stay quiet.</p>

    <div class="assets">

      <article class="asset">
        <div class="pair">
          <img class="rnd" src="profile-round-light-460.png" alt="Round crop of the mark on the pale ground." width="460" height="460" loading="lazy" decoding="async">
          <img src="profile-light-460.png" alt="The mark in dark ink on a pale ground." width="460" height="460" loading="lazy" decoding="async">
        </div>
        <h3>Paper</h3>
        <p class="note">Ink mark on the light ground. For a light surface — the site, a document, a PDF.</p>
        <p class="stack">920 · 460 · 400 · round 920 · round 460</p>
        <ul class="dl">
          <li><a href="profile-light-920.png" download>920</a></li>
          <li><a href="profile-light-460.png" download>460</a></li>
          <li><a href="profile-light-400.png" download>400</a></li>
          <li><a href="profile-round-light-920.png" download>round 920</a></li>
          <li><a href="profile-round-light-460.png" download>round 460</a></li>
        </ul>
      </article>

      <article class="asset">
        <div class="pair">
          <img class="rnd" src="profile-round-dark-460.png" alt="Round crop of the mark on the near-black ground." width="460" height="460" loading="lazy" decoding="async">
          <img src="profile-dark-460.png" alt="The mark in pale ink on a near-black ground." width="460" height="460" loading="lazy" decoding="async">
        </div>
        <h3>Night</h3>
        <p class="note">The same on the near-black ground. For a dark surface, or a profile read in dark mode most of the time.</p>
        <p class="stack">920 · 460 · 400 · round 920 · round 460</p>
        <ul class="dl">
          <li><a href="profile-dark-920.png" download>920</a></li>
          <li><a href="profile-dark-460.png" download>460</a></li>
          <li><a href="profile-dark-400.png" download>400</a></li>
          <li><a href="profile-round-dark-920.png" download>round 920</a></li>
          <li><a href="profile-round-dark-460.png" download>round 460</a></li>
        </ul>
      </article>

    </div>
  </section>

  <section id="hues" class="band">
    <div>
      <h2>Accent fields</h2>
      <p>The seven accent hues with the mark reversed out of them — the same solved pairs the site's stylesheet carries, with hue, saturation and fill lightness pinned per hue so every one holds the same contrast against its white mark.</p>

      <div class="assets">
{''.join(hue_card(by_hue[h]) for h, _s, _l in hues)}
      </div>
    </div>
  </section>

  <section id="platforms">
    <h2>Platform-coloured marks</h2>
    <p>The mark reversed out of each platform's own brand colour. <strong>A deliberate departure from the system</strong> — these are other people's colours used so the mark sits beside a platform's chrome; they are not additions to the palette, and nothing here belongs in <span class="nowrap">style.css</span>. The brand hexes are sourced rather than remembered, and the mark colour is solved per brand against WCAG 1.4.11's 3:1 for a non-text graphic.</p>
    <p class="note">On GitHub and X the mark is white on a near-black field — the same value that vanishes against your own night ground (1.11:1). Reversed out of a brand field is the one treatment that works for every platform here; <a href="platforms.html">the comparison page</a> shows the other two treatments and the four cases that fail. An avatar in a platform's exact brand colour can also read as implying an affiliation — worth a thought on a profile that lists no employer.</p>
    <div class="cta" style="margin-top:var(--s3)">
      <a class="btn" href="platform-assets-2026-11-16.zip" download>Download all platform marks (zip)</a>
      <a class="btn ghost" href="platforms.html">Compare the treatments</a>
    </div>

    <div class="assets">
{''.join(platform_card(b) for b in BRANDS)}
    </div>
  </section>

  <section id="card">
    <h2>GitHub social card</h2>
    <p>For a repository's Settings &rarr; Social preview. Points at <span class="nowrap">github.com/aclayton</span>; regenerate it if the code lands elsewhere.</p>

    <div class="assets">
      <article class="asset wide">
        <img src="github-social-1280x640.png" alt="A wide card: the mark top left, the headline, and three chips." width="1280" height="640" loading="lazy" decoding="async">
        <p class="stack">2560×1280 · 1280×640</p>
        <ul class="dl">
          <li><a href="github-social-1280x640.png" download>1280×640</a></li>
          <li><a href="github-social-2560x1280.png" download>2560×1280</a></li>
        </ul>
      </article>
    </div>
  </section>

  <section id="checked" class="band">
    <div>
      <h2>What was measured</h2>
      <p>Each of these was checked by decoding the PNG and reading the pixels. A render that looks right is not evidence that it is.</p>
      <ol class="steps">
        <li><strong>Crop safe, everywhere.</strong> In all nine fields the mark sits at 74% of the canvas width, centred to 0.0px, and its furthest ink pixel reaches 203px from centre against a circle of 230 — 26px of clearance at 460, 52px at 920. Nothing is lost when a platform crops it round.</li>
        <li><strong>The fields are the solved pairs.</strong> Each accent field was sampled at the corner and matched against the stylesheet's own hue, saturation and fill lightness: every one exact, to zero. The white mark is present in all seven.</li>
        <li><strong>The ground is a field, not a shape.</strong> The largest jump between adjacent pixels is 1 on the neutral grounds and 0 on the accent fields. A hairline edge measures 20+ — so there is provably no ring left in the artwork.</li>
        <li><strong>The round crops are the real crop.</strong> Corners fully transparent, centre opaque, and the opaque disc's radius lands within a pixel of half the canvas — the same circle a platform applies.</li>
        <li><strong>Exact sizes.</strong> 400, 460 and 920 squares, round crops at 460, and the card at 1280&times;640 and 2560&times;1280.</li>
      </ol>

      <h3>Known limitation</h3>
      <p class="note">The mark is wide and drawn in thin strokes, so it needs size to resolve. Below roughly 32px every variant reads as a smudge. A mark that stays legible at favicon size would be a separate drawing cut for that job, not a smaller copy of this one.</p>
    </div>
  </section>

</main>

<footer class="site">
  <svg class="mark-foot" viewBox="18 0 216 144" aria-hidden="true" focusable="false">
    <path fill="currentColor" d="{MARK}"/>
  </svg>
  <p>Aaron Clayton · Niagara, Canada</p>
  <p><a href="https://github.com/aclayton" rel="me">GitHub</a></p>
</footer>

<script src="/accent.js" defer></script>

</body>
</html>
"""

out = SOCIAL / "index.html"
out.write_text(PAGE)
print(f"  wrote {out} ({len(PAGE):,} bytes)")
