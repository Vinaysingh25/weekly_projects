'''
This script talks about the image processing in Opencv
Author @ Vinayak Singh
Date: 23rd May 2018
'''

import cv2
from matplotlib import pyplot as plt
import numpy as np


def open_image():
    image1 = cv2.imread('demo_image_2.jpg', 0)
    cv2.imshow('image1', image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("demo_image_2_b/w.jpg", image1)
    print('done')
    plt.imshow(image1)
    plt.show()


# print(open_image())

def capture_from_video():
    capture = cv2.VideoCapture('SampleVideo.mp4')
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# print(capture_from_video())

def image_properties():
    image2 = cv2.imread('circle.jpg', 1)
    image3 = cv2.imread('circle.jpg', 0)
    # cv2.imshow('image2', image2)
    # cv2.waitKey(0)
    print('Some facts about the image: ')
    print('the shape of the coloured image is: ', image2.shape)
    print('the shape of the gray image is: ', image3.shape)
    print('Total number of pixels in coloured image: ', image2.size)
    print('Total number of pixels in grayed image: ', image3.size)
    print('the image data type is: ', image2.dtype)
    print('the image pixel intensity at [100, 95] is: ', image2[100, 95])
    print('the value for red is:  ', image2.item(10, 10, 2))
    image2.itemset((10, 10, 2), 100)
    print('the modified RED value is', image2.item(10, 10, 2))


#print(image_properties())

def image_content_copy_paste():
    image_clrd = cv2.imread('circle.jpg', 1)
    crop = image_clrd[100:450, 350:700]
    image_clrd[200:550, 350:700]  = crop
    cv2.imshow('image', image_clrd)
    cv2.waitKey(0)
#print(image_content_copy_paste())

def extracting_b_g_r():
    image_clrd = cv2.imread('circle.jpg', 1)
    b,g,r  = cv2.split(image_clrd)
    image_clrd[:,:,2] = 0 # red pixels to zero
    cv2.imshow('image', image_clrd)
    cv2.waitKey(0)
#print(extracting_b_g_r())

def adding_a_border():
    image_clrd2 = cv2.imread('circle.jpg', 1)
    combination = [0,0,255]
    border_example = cv2.copyMakeBorder(image_clrd2, 10,10,10,10,cv2.BORDER_WRAP, value=combination)
    plt.imshow(border_example, 'gray'), plt.title('Border Example')
    plt.show()

#print(adding_a_border())

def image_blending():
    image1 = cv2.imread('circle.jpg')
    image2 = cv2.imread('demo_image_2.jpg')
    distribution =  cv2.addWeighted(image1, 0.2, image2, 0.8, 0)
    cv2.imshow('added', distribution)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
print(image_blending())




