# -* coding: utf-8 *-

'''
In this chapter,
# We will learn about Image Pyramids
# We will use Image pyramids to create a new fruit, “Orapple”
# We will see these functions: cv2.pyrUp(), cv2.pyrDown()
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

A = cv2.imread('B.jpg')
B = cv2.imread('A.jpg')

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in xrange(4):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in xrange(4):
    G = cv2.pyrDown(G)
    gpB.append(G)

# plt.imshow(gpA[3])

# g = cv2.pyrUp(gpA[2])
# L = cv2.subtract(gpA[1], g)
# plt.imshow(L)

# plt.show()
# generate Laplacian Pyramid for A
lpA = [gpA[3]]
for i in xrange(3, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    # print GE.shape
    # print gpA[i-1].shape
    L = cv2.subtract(gpA[i - 1], GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[3]]
for i in xrange(3, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i - 1], GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols / 2], lb[:, cols / 2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in xrange(1, 4):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:, :cols / 2], B[:, cols / 2:]))

cv2.imwrite('Pyramid_blending2.jpg', ls_)
cv2.imwrite('Direct_blending.jpg', real)
