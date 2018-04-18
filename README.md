# Photo deblur

Experiments in correcting the focus of photographs.

Done as part of Spring 2018 Camera Lab at Harvey Mudd College.

## Dependencies

* [Python 3](https://www.python.org/)
* [Tcl/Tk](http://tcl.sourceforge.net/)
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

### Setup on Arch Linux

Install Python:

    $ sudo pacman -Sy python

Install Python dependencies in a virtual environment:

    $ python -m venv ~/.virtualenvs/photo-deblur
    $ source ~/.virtualenvs/photo-deblur/bin/activate
    $ pip install -r requirements.txt

Install Tcl/Tk:

    $ sudo pacman -Sy tk

Install Hugin:

    $ sudo pacman -Sy hugin

## Usage

Run all the experiments:

    $ make

(Refer to `Makefile` for more advanced usage.)

## Further reading

* http://yuzhikov.com/articles/BlurredImagesRestoration1.htm
* http://yuzhikov.com/articles/BlurredImagesRestoration2.htm
* http://aishack.in/tutorials/image-convolution-examples/
* http://www.naturefocused.com/articles/photography-image-processing-kernel.html
* http://setosa.io/ev/image-kernels/
* http://www.robots.ox.ac.uk/~az/lectures/ia/lect2.pdf
* https://github.com/aurelienpierre/Image-Cases-Studies
