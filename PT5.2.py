# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 02:17:09 2021

@author: david
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('../imagenes/sudoku_bin.png',0)
img_bin=cv.medianBlur(img,5)
kernel1=np.ones((45,1),np.uint8)
kernel2=np.ones((1,45),np.uint8)
"""
Img_erode = cv.erode(img_bin,kernel,iterations=1)
Img_dilate = cv.dilate(img_bin,kernel,iterations=1)
Img_opening = cv.morphologyEx(img_bin, cv.MORPH_OPEN, kernel1)"""
Img_closing1  =  cv.morphologyEx(img_bin, cv.MORPH_CLOSE, kernel1)
Img_closing2  =  cv.morphologyEx(img_bin, cv.MORPH_CLOSE, kernel2)

Img_background=~Img_closing1+~Img_closing2

#plt.imshow(Img_closing1,'gray')
#plt.imshow(Img_closing2,'gray')
#plt.imshow(Img_background,'gray')

Imgfinal=img_bin+Img_background
img_filtered=cv.medianBlur(Imgfinal,7)
#plt.imshow(img_filtered,'gray')