#!/usr/bin/env python3
"""Copy entry.png to the make.fun output directory, byte for byte.

The image is a top-10-style single paper on a muted fridge, drawn
entirely as if by a small child with a PENCIL: grey graphite pencil
handwriting (wobbly, uneven letters with a drifting baseline) and a
pencil-sketch drawing at the bottom — the robot-judge asleep under a
hatched star blanket, "Zzz" floating above, a crescent moon and
sketchy stars, plus a pencil party hat taped at the top-right corner.
The letter is original (the judge never sleeps, so a child brings a
blanket and offers to watch the pictures). (JPEG, 1024x1024, under
1 MiB.)

Deterministic, standard library only, no network access.
"""
import os
import shutil
from pathlib import Path

# The image lives next to this script, so the copy works from any cwd.
# entry.png is a JPEG, 1024x1024, 100,499 bytes (well under the 1 MiB
# cap), deterministic — byte-identical across two renders of the
# pencil-style draw script (seeded RNG 20261117).
HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

# make.fun sets MAKEFUN_OUTPUT_DIR; fall back to /output/entry.png.
# Byte-verified below, so a partial or corrupted copy can never pass silently.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DEST = OUTPUT_DIR / "entry.png"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    assert DEST.read_bytes() == SOURCE.read_bytes(), "byte verification failed: output differs from entry.png"
    print(f"Copied {SOURCE} -> {DEST} ({DEST.stat().st_size} bytes, byte-verified)")


if __name__ == "__main__":
    main()
