# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 08:19:52 2019

@author: sangalpa
"""

import cv2
from matplotlib import pyplot as plt
img1=cv2.imread('Lenna.png')
img2=cv2.imread('flower.png')

img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
# Addition
img3=cv2.bitwise_not(img1)
img4=cv2.bitwise_and(img1,img2)
img5=cv2.bitwise_or(img1,img2)
img6=cv2.bitwise_xor(img1,img2)


images=[img1,img2,img6]
titles=['Lenna','Flower','NOT of Lenna','AND Operation','OR Operation','xor operation']
for i in range(len(images)):
    plt.subplot(1,len(images),i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]) # location specifying
    plt.yticks([])
plt.show()