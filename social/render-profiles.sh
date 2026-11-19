#!/usr/bin/env bash
# Render every profile asset from its HTML source.
#
# HOST is required because aaronc-site binds the Tailscale address only —
# 127.0.0.1 never answers, so render.sh's readiness check would fail.
#
#   ./render-profiles.sh
#   HOST=127.0.0.1 ./render-profiles.sh        # if you started a local server
set -euo pipefail
cd "$(dirname "$0")"
HOST="${HOST:-100.76.1.53}"
export HOST

r() {  # r <html> <W> <H> <SCALE> <output name>
  local html="$1" w="$2" h="$3" s="$4" name="$5"
  W="$w" H="$h" SCALE="$s" ./render.sh "$html" >/dev/null
  [ -s "${html%.html}.png" ] || { echo "*** FAILED: $html -> $name" >&2; exit 1; }
  mv "${html%.html}.png" "$name"
  printf "  %-26s -> %-32s %sx%s\n" "$html" "$name" "$w" "$h"
}

echo "neutral grounds"
r profile-light.html 460 460 2 profile-light-920.png
r profile-light.html 460 460 1 profile-light-460.png
r profile-light.html 400 400 1 profile-light-400.png
r profile-dark.html  460 460 2 profile-dark-920.png
r profile-dark.html  460 460 1 profile-dark-460.png
r profile-dark.html  400 400 1 profile-dark-400.png

echo "accent fields (the seven solved pairs)"
for h in 046 268 010 030 222 152 340; do
  r "profile-hue-${h}.html" 460 460 2 "profile-hue-${h}-920.png"
  r "profile-hue-${h}.html" 460 460 1 "profile-hue-${h}-460.png"
done

echo "github social card"
r github-social.html 1280 640 2 github-social-2560x1280.png
r github-social.html 1280 640 1 github-social-1280x640.png
