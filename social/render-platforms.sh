#!/usr/bin/env bash
# Render the platform-coloured marks from their sources, then derive round crops.
#
# HOST is required because aaronc-site binds the Tailscale address only.
#   ./render-platforms.sh
set -euo pipefail
cd "$(dirname "$0")"
HOST="${HOST:-100.76.1.53}"
export HOST

SLUGS=(github x linkedin linkedin-old telegram bluesky mastodon discord reddit
       youtube instagram facebook stack-overflow npm signal)

for sl in "${SLUGS[@]}"; do
  src="platform-${sl}.html"
  [ -f "$src" ] || { echo "*** missing $src — run build-platforms.py first" >&2; exit 1; }
  W=460 H=460 SCALE=2 ./render.sh "$src" >/dev/null
  mv "platform-${sl}.png" "platform-${sl}-920.png"
  W=460 H=460 SCALE=1 ./render.sh "$src" >/dev/null
  mv "platform-${sl}.png" "platform-${sl}-460.png"
  printf "  %-26s -> platform-%s-{920,460}.png\n" "$src" "$sl"
done

echo "deriving round crops"
python3 round-crop.py "${SLUGS[@]/#/platform-}"
