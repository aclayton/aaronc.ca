#!/usr/bin/env python3
"""Derive the round crops from the finished squares.

Clipping to a circle here, rather than rendering a round HTML variant, guarantees
the crop is the *same* geometry the platforms apply to the square — which is the
only thing worth previewing. The edge is feathered by one pixel.

For platforms that crop for you (GitHub, X, LinkedIn) upload the SQUARE. These
round files are for surfaces that want a transparent circle: decks, documents,
favicons.

    python3 round-crop.py
"""
import math, struct, sys, zlib
from pathlib import Path

HERE = Path(__file__).parent
SIZES = (920, 460)

# The squares to crop, and the stem of the round file each produces.
TARGETS = [
    "profile-light", "profile-dark",
    "profile-hue-046", "profile-hue-268", "profile-hue-010", "profile-hue-030",
    "profile-hue-222", "profile-hue-152", "profile-hue-340",
]

# Anything named on the command line replaces the default list, so the platform
# marks can share this crop logic instead of growing a second copy of it:
#     python3 round-crop.py platform-github platform-npm
if len(sys.argv) > 1:
    TARGETS = sys.argv[1:]


def read_png(path):
    d = path.read_bytes()
    assert d[:8] == b"\x89PNG\r\n\x1a\n", f"{path.name}: not a png"
    pos, idat = 8, b""
    w = h = bd = ct = il = 0
    while pos < len(d):
        ln = struct.unpack(">I", d[pos:pos + 4])[0]
        typ = d[pos + 4:pos + 8]
        data = d[pos + 8:pos + 8 + ln]
        if typ == b"IHDR":
            w, h, bd, ct, _c, _f, il = struct.unpack(">IIBBBBB", data)
        elif typ == b"IDAT":
            idat += data
        elif typ == b"IEND":
            break
        pos += 12 + ln
    assert il == 0, "interlaced png unsupported"
    assert bd == 8, f"bit depth {bd}"
    ch = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[ct]
    stride = w * ch
    raw = zlib.decompress(idat)
    out = bytearray(h * stride)
    prev = bytearray(stride)
    p = 0
    for y in range(h):
        ft = raw[p]; p += 1
        line = bytearray(raw[p:p + stride]); p += stride
        if ft == 1:
            for i in range(ch, stride):
                line[i] = (line[i] + line[i - ch]) & 255
        elif ft == 2:
            for i in range(stride):
                line[i] = (line[i] + prev[i]) & 255
        elif ft == 3:
            for i in range(stride):
                a = line[i - ch] if i >= ch else 0
                line[i] = (line[i] + ((a + prev[i]) >> 1)) & 255
        elif ft == 4:
            for i in range(stride):
                a = line[i - ch] if i >= ch else 0
                b = prev[i]
                c = prev[i - ch] if i >= ch else 0
                pp = a + b - c
                pa, pb, pc = abs(pp - a), abs(pp - b), abs(pp - c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[i] = (line[i] + pr) & 255
        out[y * stride:(y + 1) * stride] = line
        prev = line
    return w, h, ch, bytes(out), stride


def write_png(path, w, h, rgba):
    raw = bytearray()
    for y in range(h):
        raw.append(0)                                # filter: none
        raw += rgba[y * w * 4:(y + 1) * w * 4]
    comp = zlib.compress(bytes(raw), 9)

    def chunk(t, d):
        return (struct.pack(">I", len(d)) + t + d
                + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF))

    path.write_bytes(b"\x89PNG\r\n\x1a\n"
                     + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
                     + chunk(b"IDAT", comp)
                     + chunk(b"IEND", b""))


for size in SIZES:
  for stem in TARGETS:
      src = HERE / f"{stem}-{size}.png"
      w, h, ch, buf, stride = read_png(src)
      assert w == h, f"{src.name} is not square"
      cx = cy = (w - 1) / 2
      R = w / 2 - 0.5
      rgba = bytearray(w * h * 4)
      for y in range(h):
        for x in range(w):
            d = math.hypot(x + 0.5 - cx, y + 0.5 - cy)
            if d >= R + 0.5:
                continue                              # outside: leave alpha 0
            a = 255 if d <= R - 0.5 else int(255 * (R + 0.5 - d))
            so = y * stride + x * ch
            do = (y * w + x) * 4
            rgba[do] = buf[so]
            rgba[do + 1] = buf[so + 1]
            rgba[do + 2] = buf[so + 2]
            rgba[do + 3] = a
      # profile-light -> profile-round-light ; platform-github -> platform-round-github
      dst = HERE / f"{stem.replace('-', '-round-', 1)}-{size}.png"
      write_png(dst, w, h, rgba)
      print(f"  {src.name:26s} -> {dst.name}")
