from PIL import Image
import numpy as np

img = np.array(Image.open("2.7_cat_bw.png"))
print(img.shape)
im_trim = img[460:470, 200:215]
print(im_trim.shape)
Image.fromarray(im_trim).save('2.8_cat_bw_trim.png')
img = Image.open('2.8_cat_bw_trim.png')
img.show()