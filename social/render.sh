#!/usr/bin/env bash
# Render a social/diagram HTML file to PNG with the real Plex faces.
#
#   ./render.sh card.html                 # 1200x630 (default), 2x -> card.png
#   W=1600 H=900 ./render.sh diagram.html # any other size
#
# Why HTML and not SVG: SVG text needs the face installed on the system, which
# Plex is not, so SVG diagrams silently fall back to a system font. Rendering
# HTML through Chromium reuses the same @font-face stack as the site and the
# flyer, so every asset matches without embedding fonts by hand.
#
# Needs the local static server on $PORT so /fonts and /print/fonts resolve
# same-origin — Chromium will not load file:// fonts into a file:// page.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
PORT="${PORT:-8899}"
SCALE="${SCALE:-2}"
W="${W:-1200}"
H="${H:-630}"
# The preview unit binds the Tailscale address only (100.76.1.53), so 127.0.0.1
# never answers. Pass HOST=100.76.1.53 when rendering off the systemd unit.
HOST="${HOST:-127.0.0.1}"

if ! curl -s -o /dev/null "http://${HOST}:${PORT}/style.css"; then
  echo "ERROR: nothing answering on ${HOST}:${PORT}." >&2
  echo "  Tailscale-only unit:  HOST=100.76.1.53 ./render.sh ..." >&2
  echo "  or start one:         (cd ~/sites/aaronc.ca && python3 -m http.server ${PORT} --bind 0.0.0.0 &)" >&2
  exit 1
fi

for f in "$@"; do
  out="${HERE}/$(basename "$f" .html).png"
  chromium --headless --disable-gpu --no-sandbox \
    --hide-scrollbars --default-background-color=00000000 \
    --window-size="${W},${H}" \
    --force-device-scale-factor="${SCALE}" \
    --virtual-time-budget=8000 \
    --screenshot="${out}" \
    "http://${HOST}:${PORT}/social/${f}" >/dev/null 2>&1
  if [ -s "$out" ]; then
    printf "  %-24s -> %-24s %sx%s at %sx  (%s bytes)\n" "$f" "$(basename "$out")" "$W" "$H" "$SCALE" "$(stat -c%s "$out")"
  else
    printf "  %-24s FAILED\n" "$f"
  fi
done
