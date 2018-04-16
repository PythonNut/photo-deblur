#!/usr/bin/env python3

import numpy as np
import skimage.transform
import h5py
from imageio import imread, imwrite
from matplotlib import pyplot as plt
from skimage import restoration
from pyfftw.interfaces import numpy_fft as fft

def main():
    orig = plt.imread('ha0001.tif')[:,:,:3]
    blur = plt.imread('ha0000.tif')[:,:,:3]

    # blur = kernel * orig → kernel = blur/orig
    # kernel = restoration.richardson_lucy(blur, orig)

    orig_f = fft.rfft2(orig, axes=(0, 1), threads=16)
    blur_f = fft.rfft2(blur, axes=(0, 1), threads=16)

    kernel_f = blur_f / orig_f
    kernel = np.nan_to_num(fft.irfft2(kernel_f, axes=(0, 1), threads=16))

    with h5py.File('data.h5', 'w') as h5f:
        h5f.create_dataset('dataset_1', data=kernel)

    imwrite('kernel.png', np.fft.fftshift(kernel) / kernel.max())

if __name__ == '__main__':
    main()
