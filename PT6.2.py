# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:05:11 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Importo imagen
img_bin=cv2.imread("../imagenes/sudoku_solo_numeros.png",0)

#Invierto la imagen
img_bin=cv2.bitwise_not(img_bin)

#Trato de intensificar las caracteristicas de cada numero
#Para que el programa no se confunda
Mat=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3),(-1,-1))
img_bin=cv2.erode(img_bin,Mat)
img_bin=cv2.dilate(img_bin,Mat)

#Determino la cantidad de objetos y etiqueto cada uno
num_labels, img_labels, stats, cg = cv2.connectedComponentsWithStats(img_bin)

#Creo una imagen de cada numero por separado que ha detectado y lo examino
#para ver si cumple las caractericticas y por tanto descartarlo o incluirlo 
img_final_1=np.zeros_like(img_labels, np.uint8)
img_final_8=img_final_1
for j in range(num_labels):
    img_aux = np.zeros_like(img_labels, np.uint8)
    img_aux[img_labels == j] = 1
    contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE) 
    if j>=1:    
        cnt=contours[0]
        x,y,w,h = cv2.boundingRect(cnt)
        if len(contours) == 3:
            img_final_8=img_aux+img_final_8
        if h/w>2:
            img_final_1=img_aux+img_final_1
 
plt.imshow(img_final_8,'gray')