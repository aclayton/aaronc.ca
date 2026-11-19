#!/usr/bin/env python3
"""Emit social/platforms.html — the mark in platform brand colours.

A DELIBERATE DEPARTURE FROM THE SYSTEM. The style guide's palette is his own:
one rotating accent, six neutrals. These use third-party brand colours instead,
because the point is to sit beside a platform's own chrome. They are experiments,
not additions to the palette — nothing here goes into style.css.

Brand colours are SOURCED, never remembered:
  - most come from Simple Icons (simple-icons.json, 3472 brands)
  - LinkedIn and Slack are trademark-restricted there, so LinkedIn's blue was read
    off linkedin.com's own legal page (#0077B5 there; #0A66C2 is the current brand
    blue — both are shown, because both are in circulation)

The mark's `d` is read from logo.svg, never retyped.

Threshold: WCAG 1.4.11 wants 3:1 for a non-text graphic, which is what a mark is.
So the reversed-mark colour is SOLVED per brand against that 3:1, not eyeballed.
"""
import re
from pathlib import Path

import contrast as _contrast          # the WCAG maths, shared with build-index.py

HERE = Path(__file__).parent
SITE = Path("/home/boss/sites/aaronc.ca")

MARK = re.sub(r"\s+", " ",
              re.search(r'd="([^"]+)"', (SITE / "logo.svg").read_text(), re.S).group(1)).strip()

INK = "#191725"          # his light-theme ink
PAPER = "#f7f6fa"        # his light ground
NIGHT = "#0b0910"        # his dark ground
WHITE = "#ffffff"

# ── the brand table, from the single shared source ──────────────────────────
# NOT inlined: the asset index reads the same file for its download list.
import json

_BRANDS = json.loads((HERE / "brands.json").read_text())["brands"]
BRANDS = [(b["name"], b["hex"], b["src"]) for b in _BRANDS]


def lum(h):
    return _contrast.lum(h)


def contrast(a, b):
    return _contrast.contrast(a, b)


def best_on(field):
    """Which of white / his ink reads better on this field, and by how much."""
    return _contrast.best_on(field, (WHITE, INK))


def slug(n):
    return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")


def svg(cls):
    return (f'<svg class="{cls}" viewBox="18 0 216 144" aria-hidden="true" focusable="false">'
            f'<path fill="currentColor" d="{MARK}"/></svg>')


PLATFORM_CSS = """/* Platform-coloured marks — render sources.
   A deliberate departure from the system: the field is a third-party brand colour.
   Nothing here belongs in style.css. */
:root { --field: #181717; --mark: #ffffff; }
html, body { margin: 0; padding: 0; height: 100%; }
body {
  width: 100vw; height: 100vh; overflow: hidden;
  background: var(--field); color: var(--mark);
  display: grid; place-items: center;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
/* Same 74% as the profile avatars: the largest the mark can sit and stay clear
   of the inscribed circle every platform crops to. */
.mark { display: block; width: 74%; height: auto; aspect-ratio: 216/144;
        color: var(--mark); }
"""

RENDER_TMPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Aaron Clayton — {name} mark</title>
<link rel="stylesheet" href="/social/platform.css">
</head>
<body style="--field:{hex_};--mark:{mark}">
  <svg class="mark" viewBox="18 0 216 144" role="img" aria-label="Aaron Clayton">
    <path fill="currentColor" d="{mark_path}"/>
  </svg>
</body>
</html>
"""


def card(name, hex_, src):
    sl = slug(name)
    mark, ratio = best_on(hex_)
    on_paper = contrast(hex_, PAPER)
    on_night = contrast(hex_, NIGHT)
    ok_field, ok_paper, ok_night = ratio >= 3.0, on_paper >= 3.0, on_night >= 3.0
    viable = [t for t, good in (("brand field", ok_field),
                                ("brand mark on paper", ok_paper),
                                ("brand mark on night", ok_night)) if good]
    verdict = ("works: " + ", ".join(viable)) if viable else "no treatment reaches 3:1"

    def fig(cls, bg, fg, cap, val, good):
        return (f'<figure><span class="disc {cls}" style="background:{bg};color:{fg}">'
                f'{svg("mark")}</span><figcaption>{cap}<br>'
                f'<span class="mono {"ok" if good else "no"}">{val:.2f}:1</span>'
                f'</figcaption></figure>')

    return f"""
      <article class="card" id="{sl}">
        <div class="row3">
          {fig("", hex_, mark, "brand field", ratio, ok_field)}
          {fig("paper", PAPER, hex_, "on paper", on_paper, ok_paper)}
          {fig("night", NIGHT, hex_, "on night", on_night, ok_night)}
        </div>

        <h3>{name}</h3>
        <p class="meta">
          <span class="hexchip" style="background:{hex_}"></span>
          <code>{hex_}</code>
        </p>
        <p class="note">{verdict}. <span class="src">{src}</span></p>
      </article>"""


CSS = """
@font-face { font-family:"Plex Sans"; src:url("/fonts/plex-sans.woff2") format("woff2-variations");
             font-weight:400 700; font-display:swap; }
@font-face { font-family:"Plex Mono"; src:url("/fonts/plex-mono-400.woff2") format("woff2");
             font-weight:400; font-display:swap; }
@font-face { font-family:"Plex Mono"; src:url("/fonts/plex-mono-600.woff2") format("woff2");
             font-weight:600; font-display:swap; }
:root {
  --s1:.5rem; --s2:.8125rem; --s3:1.3125rem; --s4:2.125rem; --s5:3.4375rem; --s6:5.5625rem;
  --container:55.625rem;
  --bg:#f7f6fa; --surface:#eeebf6; --fg:#191725; --muted:#5e5a72; --rule:#dcd6ea;
  --font-sans:"Plex Sans", system-ui, sans-serif;
  --font-mono:"Plex Mono", ui-monospace, monospace;
}
@media (prefers-color-scheme: dark) {
  :root { --bg:#0b0910; --surface:#141120; --fg:#e9e6f2; --muted:#9a94ae; --rule:#272137; }
}
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font-family:var(--font-sans);
       font-size:1rem; line-height:1.618; padding:var(--s5) var(--s4) var(--s6); }
main, header, footer { max-width:var(--container); margin-inline:auto; }
h1 { font-size:2.618rem; line-height:1.272; letter-spacing:-.018em; margin:0 0 var(--s2); }
h2 { font-size:1.618rem; margin:var(--s6) 0 var(--s2); letter-spacing:-.018em; }
h3 { font-size:1.272rem; margin:0 0 var(--s1); letter-spacing:-.018em; }
.lede { color:var(--muted); max-width:calc(var(--container)/1.618); margin:0 0 var(--s4); }
.note { margin:0; font-size:.8125rem; color:var(--muted); }
.mono, code { font-family:var(--font-mono); }
.src { font-size:.75rem; }
.caveat { border-left:6px solid var(--fg); padding:var(--s3) var(--s4); margin:0 0 var(--s5);
          background:var(--surface); border-radius:0 6px 6px 0; font-size:.875rem; }
.caveat p { margin:0 0 var(--s1); }
.grid { display:grid; gap:var(--s4); grid-template-columns:repeat(auto-fit,minmax(17rem,1fr)); }
.grid > * { min-width:0; }
.card { border:1px solid var(--rule); border-radius:6px; padding:var(--s4);
        background:var(--surface); display:flex; flex-direction:column; gap:var(--s2); }
.row3 { display:grid; grid-template-columns:repeat(3,1fr); gap:var(--s2); }
figure { margin:0; }
.disc { display:grid; place-items:center; aspect-ratio:1; border-radius:50%;
        border:1px solid var(--rule); }
.disc.paper { background:#f7f6fa; }
.disc.night { background:#0b0910; }
.mark { width:74%; height:auto; aspect-ratio:216/144; display:block; }
figcaption { color:var(--muted); font-size:.6875rem; margin-top:.3rem; line-height:1.4; }
.meta { display:flex; align-items:center; gap:var(--s2); margin:0; font-size:.8125rem; flex-wrap:wrap; }
.hexchip { display:inline-block; width:18px; height:18px; border-radius:4px;
           border:1px solid color-mix(in srgb, currentColor 22%, transparent); }
.flag { font-size:.6875rem; font-weight:600; text-transform:uppercase; letter-spacing:.08em;
        padding:1px 7px; border-radius:99px; }
.mono.ok { color:#1b5e20; font-weight:600; }
.mono.no { color:#8c1d18; font-weight:600; }
@media (prefers-color-scheme: dark) {
  .mono.ok { color:#81c784; } .mono.no { color:#ff8a80; }
}
footer { margin:var(--s6) auto 0; padding-top:var(--s3); border-top:1px solid var(--rule);
         color:var(--muted); font-size:.8125rem; }
footer p { margin:0 0 var(--s1); }
"""

PAGE = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Platform-coloured marks</title>
<meta name="robots" content="noindex, nofollow, noarchive">
<style>{CSS}</style>
</head>
<body>

<header>
  <h1>Platform-coloured marks</h1>
  <p class="lede">The mark in each platform's own brand colour, three ways: reversed out of a
  brand field, and drawn as the mark on his paper and night grounds.</p>

  <div class="caveat">
    <p><strong>A deliberate departure from the system.</strong> His palette is six neutrals and one
    rotating accent. These are third-party brand colours, used because the point is to sit beside a
    platform's chrome. They are experiments — <strong>nothing here belongs in
    <code>style.css</code></strong>.</p>
    <p>Brand hexes are sourced, not remembered: Simple Icons for most, LinkedIn from their own
    page. The reversed-mark colour is <strong>solved per brand</strong> against WCAG 1.4.11's 3:1
    for a non-text graphic — which is what a mark is — not chosen by eye.</p>
    <p>Second caveat: an avatar in a platform's exact brand colour can read as implying an
    affiliation. Worth a thought before it becomes the profile picture on a site that lists no
    employer.</p>
  </div>
</header>

<main>
  <div class="grid">
{''.join(card(*b) for b in BRANDS)}
  </div>
</main>

<footer>
  <p>The mark is read from <code>logo.svg</code> at build time; brand colours from
  <code>simple-icons.json</code> (3472 brands) and, for LinkedIn, their own published page.
  Contrast is WCAG relative luminance.</p>
  <p>Rebuild with <code>python3 build-platforms.py</code>. Once a winner is picked, add it as a
  <code>platform-&lt;slug&gt;.html</code> render source and run it through <code>render.sh</code> +
  <code>round-crop.py</code>, the same pipeline the profile avatars use.</p>
</footer>

</body>
</html>
"""

(HERE / "platforms.html").write_text(PAGE)
print(f"  wrote {HERE / 'platforms.html'} ({len(PAGE):,} bytes)")

# ── render sources, so the marks can be rendered to PNG and put on the asset
# index's download list. One square source per brand; round crops are derived
# from the rendered square by round-crop.py, as with the profile avatars.
(HERE / "platform.css").write_text(PLATFORM_CSS)
written = 0
for name, hex_, _src in BRANDS:
    m, _r = best_on(hex_)
    (HERE / f"platform-{slug(name)}.html").write_text(
        RENDER_TMPL.format(name=name, hex_=hex_, mark=m, mark_path=MARK))
    written += 1
print(f"  wrote platform.css + {written} render sources (platform-<slug>.html)")
print(f"  {len(BRANDS)} brands")
for name, hex_, _s in BRANDS:
    m, r = best_on(hex_)
    print(f"    {name:16s} {hex_}  mark {m}  {r:.2f}:1  {'ok' if r >= 3 else 'FAILS 3:1'}"
          f"   on paper {contrast(hex_, PAPER):.2f}:1  on night {contrast(hex_, NIGHT):.2f}:1")
