.PHONY: all
all: align kernel deblur

img_aligned/trees1_blurred.tif img_aligned/trees1_sharp.tif: img_raw/trees1_blurred.jpg img_raw/trees1_sharp.jpg
	rm -rf work
	mkdir -p work
	align_image_stack $^ -a work/ -m --gpu --use-given-order -C
	mkdir -p img_aligned
	mv work/0000.tif img_aligned/trees1_blurred.tif
	mv work/0001.tif img_aligned/trees1_sharp.tif
	rm -rf work

img_aligned/trees2_blurred.tif img_aligned/trees2_sharp.tif: img_raw/trees2_blurred.jpg img_raw/trees2_sharp.jpg
	rm -rf work
	mkdir -p work
	align_image_stack $^ -a work/ -m --gpu --use-given-order -C
	mkdir -p img_aligned
	mv work/0000.tif img_aligned/trees2_blurred.tif
	mv work/0001.tif img_aligned/trees2_sharp.tif
	rm -rf work

.PHONY: align
align: img_aligned/trees1_blurred.tif img_aligned/trees1_sharp.tif img_aligned/trees2_blurred.tif img_aligned/trees2_sharp.tif

kernel/trees1_data.h5 kernel/trees1_kernel.png: img_aligned/trees1_blurred.tif img_aligned/trees1_sharp.tif compute_kernel.py
	mkdir -p kernel
	time ./compute_kernel.py img_aligned/trees1_blurred.tif img_aligned/trees1_sharp.tif kernel/trees1_data.h5 kernel/trees1_kernel.png

kernel/trees1_data_unaligned.h5 kernel/trees1_kernel_unaligned.png: img_raw/trees1_blurred.jpg img_raw/trees1_sharp.jpg compute_kernel.py
	mkdir -p kernel
	time ./compute_kernel.py img_raw/trees1_blurred.jpg img_raw/trees1_sharp.jpg kernel/trees1_data_unaligned.h5 kernel/trees1_kernel_unaligned.png

kernel/trees1_data_wiener.h5 kernel/trees1_kernel_wiener.png: img_aligned/trees1_blurred.tif img_aligned/trees1_sharp.tif compute_kernel_wiener.py
	mkdir -p kernel
	time ./compute_kernel_wiener.py img_aligned/trees1_blurred.tif img_aligned/trees1_sharp.tif kernel/trees1_data_wiener.h5 kernel/trees1_kernel_wiener.png

.PHONY: kernel
kernel: kernel/trees1_data.h5 kernel/trees1_kernel.png kernel/trees1_data_unaligned.h5 kernel/trees1_kernel_unaligned.png kernel/trees1_data_wiener.h5 kernel/trees1_kernel_wiener.png

output/trees2_simple.jpg: img_raw/trees2_blurred.jpg kernel/trees1_data.h5 deblur.py
	mkdir -p output
	time ./deblur.py img_raw/trees2_blurred.jpg kernel/trees1_data.h5 output/trees2_simple.jpg

output/trees2_simple_blur_aligned.jpg: img_aligned/trees2_blurred.tif kernel/trees1_data.h5 deblur.py
	mkdir -p output
	time ./deblur.py img_aligned/trees2_blurred.tif kernel/trees1_data.h5 output/trees2_simple_blur_aligned.jpg

output/trees2_simple_kernel_unaligned.jpg: img_raw/trees2_blurred.jpg kernel/trees1_data_unaligned.h5 deblur.py
	mkdir -p output
	time ./deblur.py img_raw/trees2_blurred.jpg kernel/trees1_data_unaligned.h5 output/trees2_simple_kernel_unaligned.jpg

output/trees2_simple_blur_aligned_kernel_unaligned.jpg: img_aligned/trees2_blurred.tif kernel/trees1_data_unaligned.h5 deblur.py
	mkdir -p output
	time ./deblur.py img_aligned/trees2_blurred.tif kernel/trees1_data_unaligned.h5 output/trees2_simple_blur_aligned_kernel_unaligned.jpg

output/trees2_wiener.jpg: img_raw/trees2_blurred.jpg kernel/trees1_data.h5 deblur_wiener.py
	mkdir -p output
	time ./deblur_wiener.py img_raw/trees2_blurred.jpg kernel/trees1_data_wiener.h5 output/trees2_wiener.jpg

output/trees2_rl.tif: img_raw/trees2_blurred.jpg deconvolve_rl.py
	mkdir -p output
	time ./deconvolve_rl.py img_raw/trees2_blurred.jpg output/trees2_rl.tif

.PHONY: deblur
deblur: output/trees2_simple.jpg output/trees2_simple_blur_aligned.jpg output/trees2_simple_kernel_unaligned.jpg output/trees2_simple_blur_aligned_kernel_unaligned.jpg output/trees2_wiener.jpg

.PHONY: clean
clean:
	rm -rf img_aligned kernel output work
