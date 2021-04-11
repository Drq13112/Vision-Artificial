# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:08:19 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def Filtro_tamaño(img_bin,min_size):             
    #Elimino las particulas pequeñas con en este algoritmo
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(img_bin, connectivity=8)
    sizes = stats[1:, -1]; nb_components = nb_components - 1
    #Defino el size minimo
    #Todo aquello que tenga un tamaño menor se ese valor es eliminado
    img2 = np.zeros((output.shape))
    for i in range(0, nb_components):
        if sizes[i] >= min_size:
            img2[output == i + 1] = 255
    return img2

img=cv2.imread('../imagenes/sudoku.png',0)

#Filtro de Gauss para suavizar
img=cv2.GaussianBlur(img,(5,5),0)

#Binarizacion adaptativa
img_bin=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#Invierto de la imagen
img_bin=cv2.bitwise_not(img_bin)

#img_bin=cv2.medianBlur(img_bin, 7)

#Ahora elimino las barras verticales y horizontales
#Obtengo la cantidad de numeros y barras 
num_labels,img_labels = cv2.connectedComponents(img_bin)

#Examino cada uno de los objetos   
""" 
h_min=10000
w_min=10000
img_final=np.zeros_like(img_labels, np.uint8)
for j in range(num_labels):
    img_aux = np.zeros_like(img_labels, np.uint8)
    img_aux[img_labels == j] = 1
    contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt=contours[0]
    if j>=1:
        for i in range(len(contours)):
            x,y,w,h = cv2.boundingRect(cnt)
            relation=w/h
            if 
                h_min=h
                w_min=w
        for i in range(len(contours)):
            x,y,w,h = cv2.boundingRect(cnt)
            if w<=w_min and h<=h_min:
                img_final=img_aux+img_final
"""
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

#Pongo un filtro de aspecto
img_final=Filtro_tamaño(img_final,120)

plt.imshow(img_final,'gray')

