import numpy as np
import h5py
from imageio import imread, imwrite
from skimage import color, data, restoration
from matplotlib import pyplot as plt
from math import floor, ceil
from pyfftw.interfaces import numpy_fft as fft

def main():
    with h5py.File('data.h5','r') as h5f:
        kernel = h5f['dataset_1'][:][10:-10,12:-12,:]

    # cut the low frequency components out, since we know they don't
    # contain any useful information. This has the side-effect of
    # significantly speeding up the deconvolution.
    # x, y, _ = kernel.shape
    # shift = np.fft.fftshift(kernel)
    # shift_clip = shift[floor(x/2 - 20):ceil(x/2 + 20), floor(y/2-20):ceil(y/2 + 20), :]
    # kernel_small = np.fft.fftshift(shift_clip)

    blur = plt.imread('hb0000.tif')[:, :, :3]
    # deconvolved = restoration.richardson_lucy(blur, kernel_small)

    blur_f = fft.rfft2(blur, axes=(0, 1), threads=16)
    kernel_f = fft.rfft2(kernel, axes=(0, 1), threads=16)

    deconvolved_f = blur_f / kernel_f
    deconvolved = np.nan_to_num(fft.irfft2(deconvolved_f, axes=(0, 1), threads=16))

    imwrite('deconvolved.png', deconvolved)

if __name__ == '__main__':
    main()
