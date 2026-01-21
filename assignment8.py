from PIL import Image 
import numpy as np 
img = np.array(Image.open('2.6_cat_g.png'))
print(img.shape)
im_trim = img[460:470,200:215]
print(im_trim.shape)
Image.fromarray(im_trim).save('2.12_cat_g_trim.png')
img = Image.open('2.12_cat_g_trim.png')
img.show()