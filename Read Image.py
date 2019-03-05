# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 03:48:09 2019

@author: sangalpa
"""

import cv2
img=cv2.imread('cat.4001.jpg',0) 
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# img=cv2.imread('cat.4001.jpg',0)  gray scale

