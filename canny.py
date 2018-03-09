__author__ = 'dehai'
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
img_path = '/home/dehai/Pictures/'
img_name = '00002.jpg'

def CannyThreshold(lowThreshold):
    gray1 = cv2.GaussianBlur(gray,(3,3),0)
    detected_edges = cv2.Canny(gray1,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
#    dst = cv2.bitwise_and(img,img,mask = detected_edges)  
    lines = cv2.HoughLinesP(detected_edges,1,np.pi/180,30,minLineLength=60,maxLineGap=10)
    lines1 = lines[:,0,:]
    for x1,y1,x2,y2 in lines1[:]:
        cv2.line(detected_edges,(x1,y1),(x2,y2),(255,0,0),1)
    cv2.imshow('canny demo',detected_edges)
    

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3

img = cv2.imread(img_path + img_name)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('canny demo',0)

cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)

CannyThreshold(0)  # initialization
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

