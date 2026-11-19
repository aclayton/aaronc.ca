#!/usr/bin/env python3
"""WCAG contrast, in one place.

Used by build-platforms.py (to solve the reversed-mark colour per brand) and by
build-index.py (to label the download list). Two copies of this maths would drift,
and a contrast claim that has drifted is worse than no claim.

    3:1  — a non-text graphic that has to be perceivable (WCAG 1.4.11). A mark is
           a graphic, so this is the bar for a mark on a field.
    4.5:1 — body text.

Relative luminance per WCAG 2.x: sRGB channels linearised, then
0.2126 R + 0.7152 G + 0.0722 B.
"""


def lum(h):
    """#rrggbb -> relative luminance."""
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))

    def f(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a, b):
    """Contrast ratio between two #rrggbb colours."""
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def best_on(field, candidates=("#ffffff", "#191725")):
    """Whichever candidate reads better on `field`, with its ratio."""
    scored = [(contrast(c, field), c) for c in candidates]
    ratio, colour = max(scored)
    return colour, ratio
