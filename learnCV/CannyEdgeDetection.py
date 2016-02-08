'''
In this chapter, we will learn about
# Concept of Canny edge detection
# OpenCV functions for that: cv2.Canny()
'''

# Canny Edge Detection is a popular edge detection algorithm. It was developed
# by John F.Canny in 1986. It is a multi-stage algorithm and we will go through
# each stages.

# see more information at http://opencv-python-tutroals.readthedocs.org/
# en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html#canny

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dave.jpg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
