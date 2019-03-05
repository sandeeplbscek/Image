# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:32:10 2019

@author: sangalpa
"""

import cv2

img1=cv2.imread('Lenna.png') 
cv2.imwrite('D:/Image.jpg', img1)
img1=cv2.resize(img1,None,fx=5.5,fy=1,interpolation=cv2.INTER_LINEAR)
cv2.imwrite('D:/Image1.jpg', img1)
img1=cv2.resize(img1,None,fx=0.2,fy=0.5,interpolation=cv2.INTER_LINEAR)
cv2.imwrite('D:/Image2.jpg', img1)
# INTER_CUBIC INTER_AREA
cv2.imshow('image',img1)
cv2.waitKey(0) # infinite time waiting
cv2.destroyAllWindows()