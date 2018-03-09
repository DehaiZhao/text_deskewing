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
img_path = '/home/dehai/Pictures/origin/'

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
#randomly chose an image
img_name = random.choice(filelist)
img_name = '00203.jpg'
img = cv2.imread(img_path + img_name)
img_shape = img.shape
time1 = time.time()
#gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#blank space to draw houghlines
blank = np.uint8(np.zeros((img_shape[0],img_shape[1])))
skernel = cv2.getStructuringElement(cv2.MORPH_RECT,(25, 25))

#binarization
ret2,th2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#denoise
opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, skernel)
#erosion
erosion = cv2.erode(opening,skernel)
#canny edge detection
edges = cv2.Canny(erosion, 80, 240, apertureSize = 3)
#hough line transform
lines = cv2.HoughLinesP(edges,1,np.pi/180,200,minLineLength=250,maxLineGap=70)
lines1 = lines[:,0,:]
Theta = []
for x1,y1,x2,y2 in lines1[:]:
    cv2.line(blank,(x1,y1),(x2,y2),(255,255,255),5)
    #calculate angle
    theta = math.atan2(y1-y2,x2-x1)
    Theta.append(theta*180/np.pi)
#find the most angle
angle_i = np.histogram(Theta,bins=90)[0].tolist()
angle_m = angle_i.index(max(angle_i))
angle = np.histogram(Theta,bins=90)[1].tolist()
#rotate
rows,cols = img.shape[:2]
angle_i = np.histogram(Theta,bins=90)[0].tolist()
angle_m = angle_i.index(max(angle_i))
angle = np.histogram(Theta,bins=90)[1].tolist()
height,width = img.shape[:2]
degree = angle[angle_m]*-1
heightNew=int(width*math.fabs(math.sin(math.radians(degree)))+height*math.fabs(math.cos(math.radians(degree))))
widthNew=int(height*math.fabs(math.sin(math.radians(degree)))+width*math.fabs(math.cos(math.radians(degree))))
M = cv2.getRotationMatrix2D((width/2,height/2),degree,1)
M[0,2] += (widthNew-width)/2  
M[1,2] += (heightNew-height)/2
res = cv2.warpAffine(img,M,(widthNew,heightNew))

#show result
print 'image:',img_name
print 'angle:',angle[angle_m]
print 'time cost:',time.time()-time1
images = [img,gray,th2,erosion,edges,blank,res]
titles = [img_name,'gray','th2','erosion','canny','houghp','rotation']
plt.figure()
for i in range(len(images)):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
plt.subplot(3,3,i+2),plt.hist(gray.ravel(),256)
plt.title('OTSU')
plt.subplot(3,3,i+3),plt.hist(Theta,90)
plt.title('angle')
plt.show()

    
