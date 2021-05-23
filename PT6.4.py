# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:08:19 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_num_etiquetas(img_bin):
    num_labels, img_labels, stats, centroids = cv2.connectedComponentsWithStats(
        img_bin)

    font = cv2.FONT_HERSHEY_SIMPLEX
    img_color = cv2.merge([img_bin, img_bin, img_bin])
    for i in range(1, num_labels): 
        
        cg = (int(centroids[i][0]), int(centroids[i][1]))
        cv2.circle(img_color, cg, 3, (255, 0, 0), -1)
        cv2.putText(img_color, str(i), cg, font,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
    plt.imshow(img_color)
    plt.axis('off')
    plt.title("Imagen")
    plt.show()
    
img=cv2.imread('../imagenes/sudoku.png',0)

#Filtro de Gauss para suavizar
img=cv2.GaussianBlur(img,(5,5),0)

#Binarizacion adaptativa
img_bin=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#Invierto de la imagen
img_bin=cv2.bitwise_not(img_bin)

#Ahora elimino las barras verticales y horizontales
#Obtengo la cantidad de numeros y barras 
num_labels,img_labels = cv2.connectedComponents(img_bin)

#Examino cada uno de los objetos   
img_final=np.zeros_like(img_labels, np.uint8)
for j in range(1,num_labels):
    img_aux = np.zeros_like(img_labels, np.uint8)
    img_aux[img_labels == j] = 1
    contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt=contours[0]
    for i in range(len(contours)):
        x,y,w,h = cv2.boundingRect(cnt)
        if w<50 and h<50:
            img_final=img_aux+img_final

#Pongo un filtro de tamaño
img_final = cv2.medianBlur(img_final, 7)

num_labels,img_labels, stats, centroids = cv2.connectedComponentsWithStats(img_final, connectivity=8)
font = cv2.FONT_HERSHEY_SIMPLEX
img_color = cv2.merge([img_final, img_final, img_final])
lista=[]

img_final2=np.zeros_like(img_labels, np.uint8)
for j in range(1,num_labels):
    img_aux = np.zeros_like(img_labels, np.uint8)
    img_aux[img_labels == j] = 1
    
    
    
    cg = (int(centroids[j][0]), int(centroids[j][1]))
    cv2.circle(img_color, cg, 3, (255, 0, 0), -1)
    cv2.putText(img_color, str(j), cg, font,
                1, (255, 0, 0), 2, cv2.LINE_AA)
    
    contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt=contours[0]
    #Perimetro
    perimeter = cv2.arcLength(cnt, True)
    
    #Area
    area = cv2.contourArea(cnt)
    
    #Relación de aspecto
    x,y,w,h = cv2.boundingRect(cnt)
    aspect_ratio = float(w)/h
    
    #Solided
    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)
    
    if hull_area!=0:
        solidity = float(area)/hull_area
    else:
        solidity=0
    
    #Circularidad
    circularity = 4*np.pi*(area/(perimeter*perimeter))
    texto='Figura:',j
    lista.append([texto,'perimetro:',perimeter,'area:',area,'Relacion de aspecto:',aspect_ratio,'solided:',solidity,'circularidad:',circularity])
    
plt.subplot(1,2,1),plt.imshow(img_final,'gray')   
plt.subplot(1, 2 ,2),plt.imshow(img_color,'gray')
print(lista)


