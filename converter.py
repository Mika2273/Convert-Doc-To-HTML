import mammoth # docx → html
import os # create file
import glob # read file name
import base64
import cv2
import numpy as np
import io
import uuid
import shutil

from bs4 import BeautifulSoup # html linter
from bs4 import Tag

import re #regular expression

class ImageWriter(object):
    def __init__(self, output_dir):
        self._output_dir = output_dir
        self._image_number = 1

    def __call__(self, element):
        extension = element.content_type.partition("/")[2]
        image_filename = "{0}.{1}".format(self._image_number, extension)
        with open(os.path.join(self._output_dir, image_filename), "wb") as image_dest:
            with element.open() as image_source:
                shutil.copyfileobj(image_source, image_dest)

        self._image_number += 1

        return {"src": image_filename}

outdir = 'images'
files = glob.glob('./src/*.docx')

for file in files:
  with open(file, 'rb') as docx_file:
    convert_image = mammoth.images.inline(ImageWriter(outdir))
    result = mammoth.convert_to_html(docx_file,convert_image=convert_image)
    source = result.value

    # --------------------- class setting start ---------------------

    # heading
    source = source.replace('<h1>', '<h1 class="">')
    source = source.replace('<h2>', '<h2 class="">')
    source = source.replace('<h3>', '<h3 class="">')
    source = source.replace('<h4>', '<h4 class="">')
    source = source.replace('<h5>', '<h5 class="">')

    # Remove p-tags in tables
    source = re.sub('<th(.*?)<p>(.*?)</p>', '<th\\1\\2', source)
    source = re.sub('<td(.*?)<p>(.*?)</p>', '<td\\1\\2', source)

    # paragraph
    source = source.replace('<p>', '<p class="">')

    # Image (Image is not supported, so a dummy image will be displayed)
    # source = re.sub('<img src=\"(.*?)\"', '<img src="https://placehold.jp/150x150.png"', source)

    # list
    source =source.replace('<ul>', '<ul class="">')
    source =source.replace('<ol>', '<ol class="">')

    # table
    source =source.replace('<table>', '<table class="">')
    source =source.replace('<tr>', '<tr class="">')
    source =source.replace('<td>', '<td class="">')

    # --------------------- class setting end ---------------------

    html = BeautifulSoup(source, 'lxml')
    html = html.prettify()
    messages = result.messages

    outputfile = file.replace('.docx', '.html')
    outputfile = outputfile.replace('/src/', '/dist/')

  with open(outputfile, mode='w') as f:
    f.write(html)
  print("finished convert output file: " + f.name)
