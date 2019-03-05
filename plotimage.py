# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 05:23:21 2019

@author: sangalpa
"""

import cv2
from matplotlib import pyplot as plt
img1=cv2.imread('Lenna.png')
img2=cv2.imread('flower.png')

img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
# Addition
add=img1+img2
sub1=img1-img2
sub2=img2-img1
mul=img1*img2
div=img1/img2

images=[img1,img2,div]
        #,mul,div]
titles=['Lenna','Flower','Addition','Subtraction1','Subtraction2','Multiplication','Division']
for i in range(len(images)):
    plt.subplot(1,len(images),i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]) # location specifying
    plt.yticks([])
plt.show()
    
 