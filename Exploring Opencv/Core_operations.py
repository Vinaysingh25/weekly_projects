'''
This script talks about the image processing in Opencv
Author @ Vinayak Singh
Date: 23rd May 2018
'''

import cv2
from matplotlib import pyplot as plt
import numpy as np


# def open_image():
#     image1 = cv2.imread('demo_image_2.jpg', 0)
#     cv2.imshow('image1', image1)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     cv2.imwrite("demo_image_2_b/w.jpg", image1)
#     print('done')
#     plt.imshow(image1)
#     plt.show()
# print(open_image())

def capture_from_video():
    capture = cv2.VideoCapture('SampleVideo.mp4')
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


print(capture_from_video())



