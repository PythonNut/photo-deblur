#!/usr/bin/env python3

import numpy as np
import skimage.transform
import h5py
import sys

from imageio import imread, imwrite
from matplotlib import pyplot as plt
from skimage import restoration
from pyfftw.interfaces import numpy_fft as fft
from concurrent.futures import ThreadPoolExecutor

def main(blur_name, orig_name, data_name, kernel_name):
    orig = plt.imread(orig_name)[:,:,:3]
    blur = plt.imread(blur_name)[:,:,:3]


    with ThreadPoolExecutor() as executor:
        deconv_results = executor.map(
            restoration.unsupervised_wiener,
            [*np.moveaxis(blur, 2, 0)],
            [*np.moveaxis(orig, 2, 0)]
        )

    kernel_r, _ = next(deconv_results)
    kernel_b, _ = next(deconv_results)
    kernel_g, _ = next(deconv_results)

    kernel = np.stack([kernel_r, kernel_b, kernel_g], axis=2)

    with h5py.File(data_name, 'w') as h5f:
        h5f.create_dataset('dataset_1', data=kernel)

    imwrite(kernel_name, kernel/kernel.max())

if __name__ == '__main__':
    main(*sys.argv[1:])
