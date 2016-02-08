# coding: utf-8 *#

import cv2
'''import numpy as np'''
from matplotlib import pyplot as plt

img = cv2.imread("a.jpg")           # read image as b g r channels
px = img[0, 0]
print px

# cv2模块也有imshow，但是显示效果不太好。
b, g, r = cv2.split(img)
img = cv2.merge((r, g, b))
plt.imshow(img, 'gray')             # show image as r g b channels

plt.show()
