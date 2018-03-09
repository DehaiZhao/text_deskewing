__author__ = 'dehai'
# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np
import random
import os
import math
import time

#image path
img_path = '/home/dehai/Pictures/rotated/'

def getFileList(p):
    if p == '':
        return []
    if p[-1] != '/':
        p = p + '/'
    a = os.listdir(p)
    b = [x for x in a if os.path.isfile(p+x)]
    if len(b)==0:
        print 'No files!'
        sys.exit()
    else:
        return b

filelist = getFileList(img_path)
img_name = random.choice(filelist)
img_name = '00002.jpg'
img = cv2.imread(img_path + img_name)
img_shape = img.shape
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
skernel = cv2.getStructuringElement(cv2.MORPH_RECT,(11, 11))

ret2,th2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,10)  
th4 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,10)
opening = cv2.morphologyEx(th3, cv2.MORPH_OPEN, skernel)

images = [img,gray,th2,opening,th3,th4]
titles = [img_name,'gray','th2','opening','mean','gaussian']
plt.figure()
cv2.imwrite('/home/dehai/OCR/tesseract/test/'+img_name, th3)
for i in range(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
#plt.show()


