import base64

# Path of the image to encode in Base64
target_file=r"bio.jpg"
# Path where the encoded image will be saved
encode_file=r"encode.txt"

with open(target_file, 'rb') as f:
    data = f.read()
#Encode images in Base64
encode=base64.b64encode(data)
with open(encode_file,"wb") as f:
    f.write(encode)
