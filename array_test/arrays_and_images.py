
from pathlib import Path
from PIL import Image
from time import sleep
import numpy as np

import skimage



# F:\GitHub\pixelsort\array_test
folder = Path(__file__).parent
test_image = folder / "pixels.jpg"


image = Image.open(test_image)
image.show()

image_np = np.array(image)
image_from_np = Image.fromarray(image_np)
image_from_np.show()



shape = np.shape(image)
x_max = shape[0]
y_max = shape[1]

y_array = []
for y in range(y_max):
    x_array = []
    for x in range(x_max):
        
        pixel_data = image_np[x, y]
        
        x_array.append(pixel_data)

    x_bar = str(x_array)
    y_array.append(x_bar)



for i, bar in enumerate(y_array, 0):
    print(f"row {i} | {bar}")

coord = image_np[0,0]

print(coord)

#skimage.transform.setup


image_data = image.load()
image_data_np = np.array(image_data)

sleep(1)

