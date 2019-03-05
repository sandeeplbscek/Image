# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:37:31 2019

@author: sangalpa
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt 
img=cv2.imread('cat.4001.jpg',0)
#height=np.size(img,0)
#width=np.size(img,1)
#img1=[[]]
#for i in range(0,height):
 #   for j in range(0,width):
  #      img1[i][j]=255-img[i][j]
img1=255-img
histg = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.plot(histg) 
plt.show() 
histg = cv2.calcHist([img1],[0],None,[256],[0,256]) 
plt.plot(histg) 
plt.show()   
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
        



