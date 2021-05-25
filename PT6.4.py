# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:08:19 2021

@author: david

Extracción de características diversas
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

    
img=cv2.imread('../imagenes/sudoku_limpia.png',0)

#Invierto de la imagen
img=cv2.bitwise_not(img)

#Determino la cantidad de objetos que hay en la imagen
num_labels,img_labels, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=8)
font = cv2.FONT_HERSHEY_SIMPLEX

#Genero la img en RGB para que se vea de color lo que dibuje en la imagen
img_color = cv2.merge([img, img, img])

#Genero la lsita donde voya a almacenar las carateristicas de cada número
#Añado un cero para tener el cuenta el fondo y que el numero de la imagen concuerde
#con su posición en el vector
lista=[0]

img_final2=np.zeros_like(img_labels, np.uint8)

for j in range(1,num_labels):
    img_aux = np.zeros_like(img_labels, np.uint8)
    img_aux[img_labels == j] = 1
    
    
    #Centro de gravedad
    cg = (int(centroids[j][0]), int(centroids[j][1]))
    cv2.circle(img_color, cg, 3, (255, 0, 0), -1)
    cv2.putText(img_color, str(j), cg, font, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt=contours[0]
    
    #Perimetro
    perimeter = cv2.arcLength(cnt, True)
    
    #Area
    area = cv2.contourArea(cnt)
    
    #Relación de aspecto
    x,y,w,h = cv2.boundingRect(cnt)
    aspect_ratio = float(w/h)
    
    #Solided
    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)
    
    if hull_area!=0:
        solidity = float(area)/hull_area
    else:
        solidity=0
    
    #Circularidad
    circularity = 4*np.pi*(area/(perimeter*perimeter))
    
    # Número de agujeros
    num_agujeros = 0
    for i in range(hierarchy[:,:,0].size):
        if hierarchy[0,i,3] != -1:
            num_agujeros += 1
    
    #Rectangularidad y cg
    marco_x, marco_y,_,_, marco_area = stats[j]
    if marco_area!=0:
        rectangularidad= area/marco_area
    
    cgx,cgy=centroids[j]
    cg = (cgx-marco_x, cgy-marco_y)
    
    
    texto='Figura:',j
    lista.append([texto,'perimetro:',perimeter,'area:',area,'Relacion de aspecto:',aspect_ratio,'solided:',solidity,'circularidad:',circularity
                  ,'n agujeros',num_agujeros,'rectangularidad',rectangularidad,'centro gravedad',cg])
    
plt.imshow(img_color,'gray')
plt.axis(False)
print(lista)


