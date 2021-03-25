# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:19:45 2021

@author: david
"""

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../imagenes/textoMalaLuz.bmp', 0)
#suavizamos previamente porque esta imagen tiene mucho ruido
img = cv.medianBlur(img,5)
#Vamos a hacerlo de tres formas
#Binarización global en umbral 127
ret,bin1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
#Binarización adaptativa con tamaño de bloque 11 y con 2 niveles debajo la media 
bin2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
bin3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, bin1, bin2, bin3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis(False)
plt.show()