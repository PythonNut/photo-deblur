#!/usr/bin/env python3

import os
import sys

from PIL import Image

sys.path.insert(0, "Image-Cases-Studies")

import deconvolve

def main(blurred_filename, deblurred_filename):
    mask = [2127, 2127 + 255, 1414, 1414 + 255]
    with Image.open(blurred_filename) as image:
        deblurred_dir, deblurred_file = os.path.split(os.path.abspath(deblurred_filename))
        deblurred_root, deblurred_ext = os.path.splitext(deblurred_file)
        assert deblurred_ext == ".tif", "we only write .tif's here! got: " + deblurred_ext
        deconvolve.deblur_module(image, deblurred_root, deblurred_dir, 25, mask=mask, display=True, confidence=50, neighbours=8, bias=1e-3)

if __name__ == "__main__":
    main(*sys.argv[1:])
