#!/usr/bin/env python3

import h5py
import numpy as np
import sys

from imageio import imread, imwrite
from math import floor, ceil
from matplotlib import pyplot as plt
from pyfftw.interfaces import numpy_fft as fft
from skimage import color, data, restoration

def resize_to_fit(img1, img2):
    width1, height1, _ = img1.shape
    width2, height2, _ = img2.shape

    width = min(width1, width2)
    height = min(height1, height2)

    width1_crop = width1 - width
    width2_crop = width2 - width
    height1_crop = height1 - height
    height2_crop = height2 - height

    width1_crop_left = width1_crop // 2
    width2_crop_left = width2_crop // 2

    height1_crop_top = height1_crop // 2
    height2_crop_top = height2_crop // 2

    width1_crop_right = width1_crop - width1_crop_left
    width2_crop_right = width2_crop - width2_crop_left

    height1_crop_bottom = height1_crop - height1_crop_top
    height2_crop_bottom = height2_crop - height2_crop_top

    img1_cropped = img1[width1_crop_left:-width1_crop_right or width1,
                        height1_crop_top:-height1_crop_bottom or height1,
                        :]

    img2_cropped = img2[width2_crop_left:-width2_crop_right or width2,
                        height2_crop_top:-height2_crop_bottom or height2,
                        :]

    return img1_cropped, img2_cropped

def main(blur_name, kernel_data_name, deconvolved_name):
    with h5py.File(kernel_data_name, 'r') as h5f:
        kernel = h5f['dataset_1'][:]

    # cut the low frequency components out, since we know they don't
    # contain any useful information. This has the side-effect of
    # significantly speeding up the deconvolution.
    # x, y, _ = kernel.shape
    # shift = np.fft.fftshift(kernel)
    # shift_clip = shift[floor(x/2 - 20):ceil(x/2 + 20), floor(y/2-20):ceil(y/2 + 20), :]
    # kernel_small = np.fft.fftshift(shift_clip)

    blur = plt.imread(blur_name)[:, :, :3]

    print("Kernel has size: " + str(kernel.shape[:2]))
    print("Blurred image has size: " + str(blur.shape[:2]))
    kernel, blur = resize_to_fit(kernel, blur)
    print("Cropped to size: " + str(blur.shape[:2]))

    # deconvolved = restoration.richardson_lucy(blur, kernel_small)

    blur_f = fft.rfft2(blur, axes=(0, 1), threads=16)
    kernel_f = fft.rfft2(kernel, axes=(0, 1), threads=16)

    deconvolved_f = blur_f / kernel_f
    deconvolved = np.nan_to_num(fft.irfft2(deconvolved_f, axes=(0, 1), threads=16))

    imwrite(deconvolved_name, deconvolved)

if __name__ == '__main__':
    main(*sys.argv[1:])
