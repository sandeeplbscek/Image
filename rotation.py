# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 06:22:47 2019

@author: sangalpa
"""

import cv2
from matplotlib import pyplot as plt
img1=cv2.imread('Lenna.png',1)
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
rows,columns,channels=img1.shape
print(rows,columns,channels)
t=cv2.getRotationMatrix2D((columns/2,rows/2),90,1)
t1=cv2.getRotationMatrix2D((columns/2,rows/2),180,1)
print(t)
img2=cv2.warpAffine(img1,t,(columns,rows))
img3=cv2.warpAffine(img1,t1,(columns,rows))
#borderMode=cv2.BORDER_TRANSPARENT

img4=cv2.flip(img1,-1)
# horizontal=0 vertical=1 both=-1
images=[img1,img2,img3,img4]
titles=['Lenna','rotate1','rotate2','flip']
for i in range(len(images)):
    plt.subplot(1,len(images),i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]) # location specifying
    plt.yticks([])
plt.show()