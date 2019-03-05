# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 08:53:37 2019

@author: sangalpa
"""

import cv2
import time
import numpy as np
img1=cv2.imread('Lenna.png') 
img2=cv2.imread('flower.png')
# linear spaacing
for i in np.linspace(0,1,10):
    alpha=i
    beta=1-alpha
    gamma=0
    output=cv2.addWeighted(img1,0.5,img2,0.5,gamma)
    cv2.imshow('image',output)
    time.sleep(1)
    if cv2.waitKey(1)==27:  # 27 escape key
        break
cv2.destroyAllWindows()