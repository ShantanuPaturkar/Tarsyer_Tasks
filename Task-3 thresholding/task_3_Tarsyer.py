# Mr.SP2
# TASK3- Tarsyer -> thresholding techniques

#import 

import cv2 as cv
# import numpy as np
from matplotlib import pyplot as plt
import os             

img = cv.imread('task_3.jpeg',0)
img = cv.medianBlur(img,5)

# adaptive Mean Thresholding
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
    cv.THRESH_BINARY,11,2)

# simple Thresholding--->BINARY INVERSE
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
titles = ['Adaptive Mean Thresholding','THRESH_BINARY_INV']

images = [ th2,thresh2]



for i in range(2):         # 2 images so 
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv.destroyAllWindows()

# for saving user o/p to folder 
#using this saving technique is effecient as it directly saves the image ,,,, no specific path required
cv.imwrite('adaptive_thresholding.jpg', th2 )
cv.imwrite('simple_thresholding.jpg',thresh2 )

# cv.destroyAllWindows()
