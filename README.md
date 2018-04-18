# Photo deblur

Experiments in correcting the focus of photographs.

Done as part of Spring 2018 Camera Lab at Harvey Mudd College.

## Dependencies

* [Python 3](https://www.python.org/)
* [Hugin](http://hugin.sourceforge.net/)

### Setup on macOS

Install command-line tools:

    $ xcode-select --install

Install [Homebrew](https://brew.sh/):

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install Python:

    $ brew install python

Install Python dependencies in a virtual environment:

    $ python -m venv ~/.virtualenvs/photo-deblur
    $ source ~/.virtualenvs/photo-deblur/bin/activate
    $ pip install -r requirements.txt

Install Hugin:

    $ brew cask install hugin
    $ ln -s /Applications/Hugin/Hugin.app/Contents/MacOS/align_image_stack /usr/local/bin/

## Usage

Align the raw images:

    $ make align

Estimate the kernel of the focus blur:

    $ make kernel

## Further reading

* http://yuzhikov.com/articles/BlurredImagesRestoration1.htm
* http://yuzhikov.com/articles/BlurredImagesRestoration2.htm
* http://aishack.in/tutorials/image-convolution-examples/
* http://www.naturefocused.com/articles/photography-image-processing-kernel.html
* http://setosa.io/ev/image-kernels/
* http://www.robots.ox.ac.uk/~az/lectures/ia/lect2.pdf
* https://github.com/aurelienpierre/Image-Cases-Studies
