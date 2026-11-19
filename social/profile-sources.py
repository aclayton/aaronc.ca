#!/usr/bin/env python3
"""Write the render sources for the profile images.

Nine near-identical files, so they are generated from one template rather than
maintained by hand — the three neutral grounds plus the seven accent fields.
Re-run after editing the template or the mark.

    python3 profile-sources.py

Then render (the preview unit is Tailscale-only, hence HOST):

    HOST=100.76.1.53 W=460 H=460 SCALE=2 ./render.sh profile-light.html
    ...
    or just: ./render-profiles.sh
"""
from pathlib import Path

HERE = Path(__file__).parent

MARK = ("M18,0v144h156.02H234V0H18z M134.625,5.76c-11.049,4.608-20.677,12.123"
        "-28.068,21.392L94.207,5.76H134.625z M23.76,5.76h63.796L23.76,114.156V5.76z "
        "M23.76,138.24v-12.564L90.44,11.232l73.603,127.008H23.76z M228.24,138.24h"
        "-37.131c8.688-4.032,16.502-9.352,23.037-15.979l-5.17-3.13c-10.599,10.28-"
        "24.039,16.538-38.531,18.176L109.666,31.996c1.927-2.587,4.054-5.07,6.376-"
        "7.392c12.512-12.512,29.146-19.41,46.838-19.41c17.347,0,33.673,6.622,"
        "46.096,18.671l5.17-2.699c-6.527-6.621-14.328-11.95-23.005-15.406h"
        "37.099V138.24z")

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Aaron Clayton — profile mark ({label})</title>
<link rel="stylesheet" href="/social/profile.css">
</head>
<body{cls}>
  <svg class="mark" viewBox="18 0 216 144" role="img" aria-label="Aaron Clayton">
    <path fill="currentColor" d="{mark}"/>
  </svg>
</body>
</html>
"""

# filename stem -> (css classes, human label used only in the <title>)
VARIANTS = [
    ("profile-light", "",                          "paper"),
    ("profile-dark",  ' class="dark"',             "night"),
    ("profile-hue-046", ' class="solid h0"',       "hue 046"),
    ("profile-hue-268", ' class="solid h1"',       "hue 268"),
    ("profile-hue-010", ' class="solid h2"',       "hue 010"),
    ("profile-hue-030", ' class="solid h3"',       "hue 030"),
    ("profile-hue-222", ' class="solid h4"',       "hue 222"),
    ("profile-hue-152", ' class="solid h5"',       "hue 152"),
    ("profile-hue-340", ' class="solid h6"',       "hue 340"),
]

for stem, cls, label in VARIANTS:
    out = HERE / f"{stem}.html"
    out.write_text(TEMPLATE.format(cls=cls, mark=MARK, label=label))
    print(f"  wrote {out.name}")

# The superseded single-accent version is gone: its field was a hand-picked
# lightness, not one of the solved pairs.
for stale in ("profile-solid.html", "profile-solid-920.png", "profile-solid-460.png"):
    p = HERE / stale
    if p.exists():
        p.unlink()
        print(f"  removed {stale}")
