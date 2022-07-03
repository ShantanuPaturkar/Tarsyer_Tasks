# Mr.sp2
# task1---->crop ,save 3 images croped , annotation through mouse and point, third original on which we will draw rectangle

#import
import cv2
import os
import cvzone
# from numpy import True_, true_divide
import numpy as np
# import matplotlib.pyplot as plt

# conditions for cropping
cropping = False
x_start, y_start, x_end, y_end = 0, 0, 0, 0
path = "\Desktop\crop image  CV"    # please change path accordingly to save output images

# Reading Image
image = cv2.imread('TASK-1.jpeg')    # please change path for image
oriImage = image.copy()


def crop_img(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping

    # if the mouse left button is DOWN, cropping is started
    if event == cv2.EVENT_LBUTTONDOWN:
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # b = image[y, x, 0]
        # g = image[y, x, 1]
        
        # cv2.putText(image, str(b) + ',' +str(g),(x,y), font, 1,(1, 0, 0), 2)
        
    
        # cv2.imshow('image', image)
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
            
                

    # after do image has been croped
    if event == cv2.EVENT_LBUTTONUP:
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # b = image[y, x, 0]
        # g = image[y, x, 1]
        
        # cv2.putText(image, str(b) + ',' +str(g),(x,y), font, 1,(1, 0, 0), 2)
        cv2.imshow('image', image)
        x_end, y_end = x, y
        cropping = True


        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2: #two points cordinates

            Task_1_cropped = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", Task_1_cropped)
            cv2.imwrite('Task_1_Cropped.jpg',Task_1_cropped)#using this saving technique is effecient as it directly saves the image ,,,, no specific path required
              

cv2.namedWindow("image")
cv2.setMouseCallback("image", crop_img)

while True:
    Task_1_insights = image.copy()
    
    
    if not cropping:
        cv2.imshow("image", image)

    elif cropping:
        cv2.rectangle(Task_1_insights, (x_start, y_start), (x_end, y_end), (1, 0, 0), 2)
        cv2.imshow("Task_1_insights", Task_1_insights)

        # points right-bottom and left-top
        cvzone.putTextRect(Task_1_insights, f"({x_start}, {y_start})", (x_start, y_start), scale=1,thickness=1, offset=20, colorR=(0, 0, 0))
        cvzone.putTextRect(Task_1_insights, f"({x_end}, {y_end})", (x_end, y_end), scale=1,thickness=1, offset=20, colorR=(0, 0, 0))

        #  Image with bounding box
    
    cv2.imwrite('task-1-insights.jpg',Task_1_insights) #using this saving technique is effecient as it directly saves the image ,,,, no specific path required
    cv2.waitKey(1)