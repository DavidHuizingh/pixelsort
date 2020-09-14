
from pathlib import Path
from PIL import Image
from time import sleep
import numpy

import skimage

skimage.io._plugins.pil_plugin

numpy.pil_

# F:\GitHub\pixelsort\array_test
folder = Path(__file__).parent
test_image = folder / "pixels.jpg"


image = Image.open(test_image)

image_data = image.load()

image_numpy = numpy.array(image)
image_data_numpy = numpy.array(image_data)

sleep(1)

