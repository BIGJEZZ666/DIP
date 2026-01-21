from PIL import Image
from numpy import asarray

img = Image.open('2.8_cat_bw_trim.png')
img.show()
print("Image Size:", img.size)
print(asarray(img))