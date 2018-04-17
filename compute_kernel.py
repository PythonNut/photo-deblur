#!/usr/bin/env python3

import h5py
import numpy as np
import skimage.transform
import sys

from imageio import imread, imwrite
from matplotlib import pyplot as plt
from pyfftw.interfaces import numpy_fft as fft
from skimage import restoration

def main(blur_name, orig_name, data_name, kernel_name):
    orig = plt.imread(orig_name)[:,:,:3]
    blur = plt.imread(blur_name)[:,:,:3]

    # blur = kernel * orig → kernel = blur/orig
    # kernel = restoration.richardson_lucy(blur, orig)

    orig_f = fft.rfft2(orig, axes=(0, 1), threads=16)
    blur_f = fft.rfft2(blur, axes=(0, 1), threads=16)

    kernel_f = blur_f / orig_f
    kernel = np.nan_to_num(fft.irfft2(kernel_f, axes=(0, 1), threads=16))

    with h5py.File(data_name, 'w') as h5f:
        h5f.create_dataset('dataset_1', data=kernel)

    imwrite(kernel_name, np.fft.fftshift(kernel) / kernel.max())

if __name__ == '__main__':
    main(*sys.argv[1:])
