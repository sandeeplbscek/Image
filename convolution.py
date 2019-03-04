# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 03:38:58 2019

@author: sangalpa
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np
img1=cv2.imread('Lenna.png',1)
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
#k=np.array(([0,0,0],[0,1,0],[0,0,0]),np.float32)
k=np.array(np.ones((3,3),np.float32))
img2=cv2.filter2D(img1,-1,k)
# depth of image -1 same size
k=np.array(([1,0,-1],[0,0,0],[-1,0,1]),np.float32)
img3=cv2.filter2D(img1,-1,k)
#img4=cv2.boxFilter(img1,-1,(53,53))
#img4=cv2.blur(img1,(13,13))
#img4=cv2.GaussianBlur(img1,(37,37),0)
#medianBlur(img,3) 3 filter size

images=[img1,img3]
titles=['Lenna','Identity Filter']
for i in range(len(images)):
    plt.subplot(1,len(images),i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]) # location specifying
    plt.yticks([])
plt.show()