# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 06:18:42 2019

@author: sangalpa
"""
#https://www.hdm-stuttgart.de/~maucher/Python/MMCodecs/html/transforms.html#discrete-cosine-transform-dct
#https://www.youtube.com/watch?v=FmW0vdEccZM
import cv2
import numpy as np
#from matplotlib import pyplot as plt
#from matplotlib.colors import Normalize
#import matplotlib.cm as cm
B=8 #blocksize
fn3= 'cat.4001.jpg'
img1 = cv2.imread(fn3,0)
h,w=np.array(img1.shape[:2])/B * B
h=int(h)
w=int(w)
print(h)
print(w)

img1=img1[:h,:w]

blocksV=int(h/B)
blocksH=int(w/B)
vis0 = np.zeros((h,w), np.float32)
Trans = np.zeros((h,w), np.float32)
vis0[:h, :w] = img1
for row in range(blocksV):
    for col in range(blocksH):
        currentblock = cv2.dct(vis0[row*B:(row+1)*B,col*B:(col+1)*B])
        Trans[row*B:(row+1)*B,col*B:(col+1)*B]=currentblock

m1=np.array(Trans,dtype=np.uint8)    
cv2.imshow('fft',m1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
#cv2.cv.SaveImage('Transformed.jpg', cv2.cv.fromarray(Trans))
