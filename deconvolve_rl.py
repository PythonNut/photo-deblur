#!/usr/bin/env python3

import os
import sys

from PIL import Image

sys.path.insert(0, "Image-Cases-Studies")

import deconvolve

def main(blurred_filename, deblurred_filename, blur_diameter, mask_x, mask_y, mask_w, mask_h, confidence, neighbors, bias):
    blur_diameter = int(blur_diameter)
    mask_x = int(mask_x)
    mask_y = int(mask_y)
    mask_w = int(mask_w)
    mask_h = int(mask_h)
    confidence = int(confidence)
    neighbors = int(neighbors)
    bias = float(bias)
    mask = [mask_x, mask_x + mask_w, mask_y + mask_h]
    with Image.open(blurred_filename) as image:
        deblurred_dir, deblurred_file = os.path.split(os.path.abspath(deblurred_filename))
        deblurred_root, deblurred_ext = os.path.splitext(deblurred_file)
        assert deblurred_ext == ".tif", "we only write .tif's here! got: " + deblurred_ext
        deconvolve.deblur_module(image, deblurred_root, deblurred_dir, blur_diameter, mask=mask, display=False, confidence=confidence, neighbours=neighbors, bias=bias)

if __name__ == "__main__":
    main(*sys.argv[1:])
