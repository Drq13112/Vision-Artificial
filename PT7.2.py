# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:32:18 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


#img=cv2.imread('../Imagenes/tuercas_tornillo2.bmp',0)
#img=cv2.imread('../Imagenes/tuercas_tornillos3.bmp',0)
img=cv2.imread('../Imagenes/llave_tornillos.png',0)
#img=cv2.imread('../Imagenes/llaves1.bmp',0)
#img=cv2.imread('../Imagenes/pinon1.png',0)
#img=cv2.imread('../Imagenes/corona1.bmp',0)
#img=cv2.imread('../Imagenes/corona0.bmp',0)
#img=cv2.imread('../Imagenes/brida.png',0)


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

Arandelas=[0]*num_labels
Tuercas=[0]*num_labels
Tornillos=[0]*num_labels
Llave_fija=[0]*num_labels
Llave_estrella=[0]*num_labels
Bridas=[0]*num_labels
Piñones=[0]*num_labels
Coronas=[0]*num_labels

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
        
        #Para mostrar el contorno que toma la función
        imgcontoursRGB=cv2.cvtColor(img_bin,cv2.COLOR_GRAY2RGB)
        imgcontoursRGB=cv2.drawContours(imgcontoursRGB,contours, -1, (255,0,0),5)
        cv2.imshow(' ',imgcontoursRGB)
        cv2.waitKey(0)
        
        _,y,_=hierarchy.shape
        if perimeter == 0:
            break
        if y>3:
            if 0.8<circularity:
                Bridas.insert(i,i)
                break
            else :
                Coronas.insert(i,i)
                break
        if y==3:
            Llave_estrella.insert(i,i)
            break
        if y==2:
            if 0.8<=circularity and area<310:
                Arandelas.insert(i,i)
                break
            if 0.8<circularity and area<3000:
                Tuercas.insert(i,i)
                break
            if 0.5<circularity and area>10000:
                Piñones.insert(i,i)
                break
            if 0.8<circularity and 1000<area<=3000:
                Bridas.insert(i,i)
                break
        if y==1 and area>3500 and 0.8>circularity:
            Llave_fija.insert(i,i)
            break
        if y==1 and area<=3500 and 0.8>circularity:
            Tornillos.insert(i,i)
            break 
           
Lista_objetos_letra=['Cantidad de arandelas','Cantidad de tuercas',
               'Cantidad de llaves estrella','Cantidad de llaves fijas'
               ,'Cantidad de tornillos','Cantidad de piñones','Cantidad de coronas','Cantidad de bridas']
#Lista_objetos=[len(Arandelas),len(Tuercas),len(Llave_estrella),len(Llave_fija),len(Tornillos),len(Piñones),
#              len(Coronas),len(Bridas)]
Lista_objetos2=[Arandelas,Tuercas,Llave_estrella,Llave_fija,Tornillos,Piñones,
               Coronas,Bridas]

Lista_Aux=[]
Lista_Aux2=[]
for i in range(len(Lista_objetos_letra)):
    Lista_Aux=Lista_objetos2[i]
    for j in range(len(Lista_objetos2[i])):
        if Lista_Aux[j]!=0:
            Lista_Aux2.append(j)
            
    print(Lista_objetos_letra[i],len(Lista_Aux2))
    if len(Lista_objetos2[i])!=num_labels:  
        print('Está formado por los objetos:',Lista_Aux2)
    Lista_Aux2=[]
        

            
            
        
            
        
        
        
        
