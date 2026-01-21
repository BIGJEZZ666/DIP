import cv2
gImg = cv2.imread('3.1_cat.jpg',cv2.IMREAD_GRAYSCALE)
gImg_neg = 255 - gImg
cv2.imshow("Input Image", gImg)
cv2.imshow("Image Negative", gImg_neg)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("3.4_cat_g.png", gImg)
cv2.imwrite("3.4_cat_g_neg.png", gImg_neg)

# |  a  |  r  |   g  |   b
#  0x00 |  00 |  00  |  00