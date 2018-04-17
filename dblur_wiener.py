#!/usr/bin/env python3

import numpy as np
import h5py
import sys

from imageio import imread, imwrite
from skimage import color, data, restoration
from matplotlib import pyplot as plt
from math import floor, ceil
from pyfftw.interfaces import numpy_fft as fft
from concurrent.futures import ThreadPoolExecutor

def main(blur_name, kernel_data_name, deconvolved_name):
    with h5py.File(kernel_data_name,'r') as h5f:
        kernel = h5f['dataset_1'][:][10:-10,13:-13,:]

    # cut the low frequency components out, since we know they don't
    # contain any useful information. This has the side-effect of
    # significantly speeding up the deconvolution.
    x, y, _ = kernel.shape
    ksize = 20
    kernel_small = kernel[floor(x/2 - ksize):ceil(x/2 + ksize), floor(y/2-ksize):ceil(y/2 + ksize), :]
    kernel_small[ksize//2,:] = (kernel_small[ksize//2 + 1,:] + kernel_small[ksize//2 - 1,:])/2
    kernel_small[:,ksize//2] = (kernel_small[:,ksize//2 + 1] + kernel_small[:,ksize//2 - 1])/2

    kernel_r, kernel_g, kernel_b = np.moveaxis(kernel_small, 2, 0)
    kernel_r /= kernel_r.sum()
    kernel_g /= kernel_g.sum()
    kernel_b /= kernel_b.sum()

    blur = plt.imread(blur_name)[:, :, :3]/255

    with ThreadPoolExecutor() as executor:
        deconv_results = executor.map(
            restoration.unsupervised_wiener,
            [*np.moveaxis(blur, 2, 0)],
            (kernel_r, kernel_b, kernel_g)
        )

    deconvolved_r, _ = next(deconv_results)
    deconvolved_g, _ = next(deconv_results)
    deconvolved_b, _ = next(deconv_results)

    deconvolved = np.stack([deconvolved_r, deconvolved_g, deconvolved_b], axis=2)

    imwrite(deconvolved_name, deconvolved)

if __name__ == '__main__':
    main(*sys.argv[1:])
