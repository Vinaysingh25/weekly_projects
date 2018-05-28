'''
This script talks about the image processing in Opencv
Author @ Vinayak Singh
Date: 23rd May 2018
'''

import cv2
image1 = cv2.imread('C:\\Users\\airbus\\Documents\\Vinayak\\Weekly_Projects\\demo_image_2.jpg', 1)
image2 = cv2.imread('C:\\Users\\airbus\\Documents\\Vinayak\\Weekly_Projects\\demo_image_2.jpg', 0)
cv2.imshow('image1',image1)

# def image_display(image):
#     open_image_gray = cv2.imshow('image1',image)
#     return open_image_gray
#
# print(image_display(image1))


