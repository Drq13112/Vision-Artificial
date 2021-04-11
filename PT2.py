# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 11:58:24 2021

@author: david
"""
import cv2 
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('../imagenes/tirafondos0.png',0)

#Filtro de Gauss para suavizar
img=cv2.GaussianBlur(img,(5,5),0)

#Binarizacion adaptativa
img_bin=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#Invierto de la imagen
img_bin=cv2.bitwise_not(img_bin)

num_labels,img_labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin)

img_final=np.zeros_like(img_labels, np.uint8)
for j in range(num_labels):
    img_aux = np.zeros_like(img_labels, np.uint8)
    img_aux[img_labels == j] = 1
    contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt=contours[0]
    if j>=1:
        for i in range(len(contours)):
            x,y,w,h = cv2.boundingRect(cnt)
            if w<50 and h<50:
                img_final=img_aux+img_final
