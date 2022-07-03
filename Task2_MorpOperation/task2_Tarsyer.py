# Mr.SP2
# task2---> morphological operations on image (erosion,tophat,blackhat)
# import all needed


import cv2
import numpy as np
# import os : if we have to save or get output

# path = # provide path to save output

img = cv2.imread('task_2.jpeg', 0)
kernel = np.ones((5, 5), np.uint8)

# Morphological Operations
img_erosion = cv2.erode(img, kernel, iterations=1)
# img_boundary = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# output image (original)
cv2.imshow('Input', img)

# Erosion
cv2.imshow('Erosion', img_erosion)


#tophat
cv2.imshow('Tophat', tophat)


# # Gradient (Boundary)
# cv2.imshow('Boundary', img_boundary)

# Blackhat
cv2.imshow('blackhat', blackhat)


cv2.waitKey(0)