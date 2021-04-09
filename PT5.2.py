# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 02:17:09 2021

@author: david
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img_bin=cv.imread('../imagenes/sudoku_bin.png',0)
img_bin=cv.bitwise_not(img_bin)

#Defino los kernels
h_size=img_bin.shape[1] //18
v_size=img_bin.shape[0]//13
#kernel3=np.ones((5,5),np.uint8)
kernel_h=cv.getStructuringElement(cv.MORPH_RECT,(h_size,1))
kernel_v=cv.getStructuringElement(cv.MORPH_RECT,(1,v_size))

#Obtengo las columenas y filas
Img_horizontal  =  cv.morphologyEx(img_bin,cv.MORPH_OPEN,kernel_h)
Img_vertical  =  cv.morphologyEx(img_bin,cv.MORPH_OPEN,kernel_v)
                                 
Img_background=Img_horizontal+Img_vertical

#Obtengo la imagen final, es decir, solo los números
img=img_bin-Img_background

#filtro la imagen con un filtro de la mediana
img=cv.medianBlur(img,7)
#Elimino las particulas pequeñas con en este algoritmo
nb_components, output, stats, centroids = cv.connectedComponentsWithStats(img, connectivity=8)
sizes = stats[1:, -1]; nb_components = nb_components - 1

#Defino el size minimo
#Todo aquello que tenga un tamaño menor se ese valor es eliminado
min_size = 100

#
img2 = np.zeros((output.shape))
for i in range(0, nb_components):
    if sizes[i] >= min_size:
        img2[output == i + 1] = 255
        
plt.imshow(img2,'gray')



