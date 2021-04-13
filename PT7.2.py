# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:32:18 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

Arandelas=[]
Tuercas=[]
Tornillos=[]
Llave_fija=[]
Llave_estrella=[]
Bridas=[]
Piñones=[]
Coronas=[]

#img=cv2.imread('../Imagenes/tuercas_tornillo2.bmp',0)
#img=cv2.imread('../Imagenes/tuercas_tornillos3.bmp',0)
#img=cv2.imread('../Imagenes/llave_tornillos.png',0)
img=cv2.imread('../Imagenes/llaves1.bmp',0)



#Filtro de Gauss para suavizar
img=cv2.GaussianBlur(img,(3,3),0)

#Filtro de Otsu para binarizar
img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#Defino el kernel y hago una apertura y un cierre a la imagen
kernel3 = np.ones((3, 3), np.uint8)
#img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel3)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel3)
#Obtengo la cantidad de objetos 
num_labels,labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin)

#Clasifico
plt.imshow(img_bin,'gray')
for i in range(1,num_labels):
    img_aux = np.zeros_like(labels, np.uint8)
    img_aux[labels == i] = 1
    
    # Obtengo los contornos
    contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    cnt=contours[0]
    #if i>=1:
    for j in range(len(contours)):
        x,y,w,h = cv2.boundingRect(cnt)
        perimeter = cv2.arcLength(cnt, True)# pongo true por que el contorno es cerrado
        area = cv2.contourArea(cnt)
        circularity = 4*np.pi*(area/(perimeter*perimeter)) 
        if perimeter == 0:
            break
        if j==2:
            Llave_estrella.append(i)
            break
        if j==1:
            if 0.8<=circularity and area<310:
                Arandelas.append(i)
                break
            if 0.8<circularity and area<3000:
                Tuercas.append(i)
                break
        if j==0 and area>3500 and 0.8>circularity:
            Llave_fija.append(i)
            break
        if j==0 and area<=3500 and 0.8>circularity:
            Tornillos.append(i)
            break 
           
Lista_objetos_letra=['Cantidad de arandelas','Cantidad de tuercas',
               'Cantidad de llaves estrella','Cantidad de llaves fijas'
               ,'Cantidad de tornillos']
Lista_objetos=[len(Arandelas),len(Tuercas),len(Llave_estrella),len(Llave_fija),len(Tornillos)]

for i in range(len(Lista_objetos_letra)):
    print(Lista_objetos_letra[i],Lista_objetos[i])

            
            
        
            
        
        
        
        
