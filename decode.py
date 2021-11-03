import cv2
import base64
import numpy as np
import io

# Base64-encoded file path
target_file=r"encode.txt"

# Path where the decoded image will be saved
image_file=r"decode.jpg"

with open(target_file, 'rb') as f:
    img_base64 = f.read()

img_binary = base64.b64decode(img_base64)
jpg=np.frombuffer(img_binary,dtype=np.uint8)

img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
cv2.imwrite(image_file,img)
