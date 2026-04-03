#!/usr/bin/env python3
"""Horizontally concatenate two images with a border between them."""

import sys
from PIL import Image


def hconcat(path1: str, path2: str, output: str = "output.png",
            border: int = 10, border_color: tuple = (0, 0, 0)):
    img1 = Image.open(path1)
    img2 = Image.open(path2)

    # Match heights (scale smaller to taller)
    if img1.height != img2.height:
        target_h = max(img1.height, img2.height)
        if img1.height < target_h:
            img1 = img1.resize((int(img1.width * target_h / img1.height), target_h))
        else:
            img2 = img2.resize((int(img2.width * target_h / img2.height), target_h))

    total_w = img1.width + border + img2.width
    result = Image.new("RGB", (total_w, img1.height), border_color)
    result.paste(img1, (0, 0))
    result.paste(img2, (img1.width + border, 0))
    result.save(output)
    print(f"Saved to {output}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python hconcat.py <image1> <image2> [output] [border_px] [border_hex]")
        print("  e.g. python hconcat.py a.png b.png out.png 20 '#ff0000'")
        sys.exit(1)

    out = sys.argv[3] if len(sys.argv) > 3 else "output.png"
    bw = int(sys.argv[4]) if len(sys.argv) > 4 else 10
    bc = tuple(int(sys.argv[5].strip("#")[i:i+2], 16) for i in (0, 2, 4)) if len(sys.argv) > 5 else (0, 0, 0)

    hconcat(sys.argv[1], sys.argv[2], out, bw, bc)
