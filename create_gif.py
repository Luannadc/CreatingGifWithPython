import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['cat_image01.png', 'cat_image02.png']
images = [ ]

#define a common size for all images(width, height)
size = (512, 512)

for filename in filenames:
  img = Image.open(filename).convert("RGB").resize(size)
  images.append(np.array(img))
  
iio.imwrite('cat.gif', images, duration=300, loop = 0)

# first argument is the output file name
# second argument is the list containing the imags data
# how long each picture should be displayed in milliseconds
# loop=0 means the gif will loop forever

