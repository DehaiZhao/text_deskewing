# -*- coding: utf-8 -*-

import cv2
import os

img_path = '/home/dehai/Pictures/DPI/'

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
c = 0
for img_name in filelist:
    c += 1
    print 'processing image{},{}/{}'.format(img_name,c,len(filelist))
    os.system('mogrify -density 200 -units PixelsPerInch ' + os.path.join(img_path, img_name))
