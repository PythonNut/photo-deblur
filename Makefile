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
