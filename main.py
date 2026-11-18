#!/usr/bin/env python3
"""news-image-20261118 entry (Python 3.13, standard library only).

The image is the entry.png beside this file: a one-day newspaper front page
summing up the world's news of Wednesday, 18 November 2026. The program
copies it to /output/entry.png (or $MAKEFUN_OUTPUT_DIR, which stands in for
/output outside the grader's container). Copying fixed bytes is deterministic,
so two runs write identical bytes.

Run it with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT, "entry.png"))
