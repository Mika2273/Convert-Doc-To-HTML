import mammoth # docx → html
import os # create file
import glob # read file name
import base64
import cv2
import numpy as np
import io
import uuid

from bs4 import BeautifulSoup # html linter
from bs4 import Tag

import re #regular expression

os.makedirs('images')

def convert_image(image):


    with image.open() as image_bytes:
        encoded_src = base64.b64encode(image_bytes.read()).decode("ascii")
        # encoded_src = image_bytes.read()
        # directory = (os.getcwd())
        # image_path = directory + '/images/' '*' + 'g' + '*' + '.jpg'
        # files = glob.glob(image_path)
        uniqid = str(uuid.uuid4())
        image_file=r"images/" + uniqid + ".jpg"
        img_binary = base64.b64decode(encoded_src)
        # img_binary = encoded_src
        jpg=np.frombuffer(img_binary,dtype=np.uint8)

        img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
        cv2.imwrite(image_file,img)

    return {
        "src": "data:{0};base64,{1}".format(image.content_type, encoded_src)
    }

files = glob.glob('./src/*.docx')

for file in files:
  with open(file, 'rb') as docx_file:
    result = mammoth.convert_to_html(docx_file, convert_image=mammoth.images.img_element(convert_image))
    # result = mammoth.convert_to_html(docx_file)
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
