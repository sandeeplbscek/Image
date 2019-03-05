# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 05:46:14 2019

@author: sangalpa
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np
img1=cv2.imread('Lenna.png',1)
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
rows,columns,channels=img1.shape
print(rows,columns,channels)
t=np.float32([[1,0,50],[0,1,-50]])
print(t)
t1=np.float32([[1,0,-50],[0,1,-50]])
img2=cv2.warpAffine(img1,t,(columns,rows),borderMode=cv2.BORDER_TRANSPARENT)
img3=cv2.warpAffine(img1,t1,(columns,rows),borderMode=cv2.BORDER_TRANSPARENT)
#borderMode=cv2.BORDER_TRANSPARENT
images=[img1,img2,img3]
titles=['Lenna','translated1','translated2']
for i in range(len(images)):
    plt.subplot(1,len(images),i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]) # location specifying
    plt.yticks([])
plt.show()