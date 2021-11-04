# Convert doc to HTML
This is a tool for converting word documents into HTML. It uses Python's open source library, 'mammoth'.

## How to use?
In the root, prepare a folder 'src' for the word documents to be converted, and a folder 'dist' where the generated HTML will be saved. Also, prepare a folder 'images' for the images in 'dist'.
Run `python3 converter.py`
## How to set up a python environment
1. Setting Up Python 3
  * Check the version of Python 3 `python3 -V`
  * Check if pop is installed `pip -V`
  * Install manage software packages for Python `sudo apt install -y python3-pip`

2. install libraries

  * If you want to see a list of installed packages
    `python3 -m pip list`
  * install mammoth
    Python library for convert Word documents from docx to simple and clean HTML and Markdown
    `pip3 install mammoth`
  * install beautiful soup4 and lxml
    `pip3 install bs4`
    `pip3 install lxml`
