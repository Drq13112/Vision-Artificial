# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:13:13 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Importo la imagen
img=cv2.imread('../imagenes/calculadora.png',0)

#Filtro de Otsu para binarizar
img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#Invierto la imagen
img_bin=cv2.bitwise_not(img_bin)

#Defino el kernel 
Mat=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5),(-1,-1))
    
#Someto a la imagen a proceso de erosión y dilatacion 
img_bin=cv2.dilate(img_bin,Mat,iterations=6)
img_bin=cv2.erode(img_bin,Mat,iterations=5)

#Obtengo las caracteristicas 
num_labels, img_labels, stats, cg = cv2.connectedComponentsWithStats(img_bin)

#Defino el contorno de la calculadora
contours,_ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]
((centx,centy), (width,height), angle)=cv2.fitEllipse(cnt)

#Lo imprimo por pantalla
imgcontoursRGB=cv2.cvtColor(img_bin,cv2.COLOR_GRAY2RGB)
imgcontoursRGB=cv2.drawContours(imgcontoursRGB,contours, -1, (255,0,0),5)
cv2.imshow(' ',imgcontoursRGB)
cv2.waitKey(0)

#(int(cg[1][1]),int(cg[1][0]
#img_bin.shape[1],img_bin.shape[0]

#Giro la imagen de tal forma que la calculadora quede verticalmente
M=cv2.getRotationMatrix2D((int(cg[1][0]),int(cg[1][1])),angle,1)
img= cv2.warpAffine(img,M,(img_bin.shape[0],img_bin.shape[1]))

#Recorto la imagen 
x,y,w,h = cv2.boundingRect(cnt)
img = img[y:y+h,x:x+w]

#Compruebo que la imagen esta colocada correctamente
img_abajo=img_bin[int(img_bin.shape[0]/2):img_bin.shape[0]]
img_arriba=img_bin[0:int(img_bin.shape[0]/2)]

#Defino el algoritmo que determina si la imagen esta vbien o esta al revés
contours, hierarchy = cv2.findContours(img_abajo, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
if hierarchy.shape[1]>1:
    print('esta al reves')
img=cv2.rotate(img,cv2.cv2.ROTATE_180)
plt.imshow(img,'gray')

