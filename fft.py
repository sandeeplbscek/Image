# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 03:48:09 2019

@author: sangalpa
"""

import cv2
import numpy as np
img=cv2.imread('cat.4001.jpg',0)
f=np.fft.fft2(img) 
m=20*np.log(np.abs(f))
m1=np.array(m,dtype=np.uint8)

cv2.imshow('fft',m1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# img=cv2.imread('cat.4001.jpg',0)  gray scale

