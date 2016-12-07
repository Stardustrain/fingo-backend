import os
import binascii
from PIL import Image, ImageOps
from io import BytesIO


def create_thumbnail(image):
    size = 200, 200
    im = Image.open(image)
    image = ImageOps.fit(im, size, Image.ANTIALIAS)

    temp_file = BytesIO()
    image.save(temp_file, "JPEG")
    temp_file.seek(0)

    random_image_name = binascii.hexlify(os.urandom(10)).decode("utf-8")
    im.close()

    return temp_file, random_image_name
