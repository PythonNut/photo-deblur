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
