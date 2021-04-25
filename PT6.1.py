# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:13:13 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def Recoloca_calculadora(img):
    # Primero suavizamos la imagen y luego la binarizamoscon Otsu
    img_suavizada = cv2.medianBlur(img,3)
    _, img_bin = cv2.threshold(img_suavizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    #Obtengo las caracteristicas 
    num_labels, img_labels, stats, cg = cv2.connectedComponentsWithStats(img_bin)
    
    #Defino el contorno de la calculadora
    contours,_ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt = contours[0]
    ((centx,centy), (width,height), angle)=cv2.fitEllipse(cnt)
    
    """
    #Lo imprimo por pantalla
    imgcontoursRGB=cv2.cvtColor(img_bin,cv2.COLOR_GRAY2RGB)
    imgcontoursRGB=cv2.drawContours(imgcontoursRGB,contours, -1, (255,0,0),5)
    cv2.imshow(' ',imgcontoursRGB)
    cv2.waitKey(0)
    """
    
    #Giro la imagen de tal forma que la calculadora quede verticalmente
    M=cv2.getRotationMatrix2D((int(cg[1][0]),int(cg[1][1])),angle,1)
    img_recortada= cv2.warpAffine(img,M,(img_bin.shape[0],img_bin.shape[1]))
    img_bin= cv2.warpAffine(img_bin,M,(img_bin.shape[0],img_bin.shape[1]))
    contours2, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
    #Recorto la imagen 
    x,y,w,h = cv2.boundingRect(contours2[0])
    img_recortada = img_recortada[y:y+h,x:x+w]
    img_bin = img_bin[y:y+h,x:x+w]
    
    #Defino el kernel y hago una apertura fuerte para elimar los botones y dejar solo al pantalla
    Mat=cv2.getStructuringElement(cv2.MORPH_RECT,(25,25))
    img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_DILATE, Mat)
    
    #Compruebo que la imagen esta colocada correctamente
    img_abajo=img_bin[int(img_bin.shape[0]/2):img_bin.shape[0]]
    img_arriba=img_bin[0:int(img_bin.shape[0]/2)]
    
    #Defino el algoritmo que determina si la imagen esta bien o está al revés
    contours, hierarchy = cv2.findContours(img_abajo, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    if hierarchy.shape[1]>1:
        print('esta al reves')   
        ((centx,centy), (width,height), angle)=cv2.fitEllipse(cnt)
        img_recortada=cv2.rotate(img_recortada,cv2.cv2.ROTATE_180)
        
    return img_recortada
#--------------------------------------------------------------------

#Importo la imagen
img=cv2.imread('../imagenes/calculadora.png',0)
img3=cv2.imread('../imagenes/calculadora3.png',0)
img4=cv2.imread('../imagenes/calculadora4.png',0)
img_recortada=Recoloca_calculadora(img)
img_recortada3=Recoloca_calculadora(img3)
img_recortada4=Recoloca_calculadora(img4)
#Imprimo por pantalla
plt.subplot(3,2,1),plt.imshow(img,'gray'),plt.axis(False)
plt.subplot(3,2,2),plt.imshow(img_recortada,'gray'),plt.axis(False)
plt.subplot(3,2,3),plt.imshow(img3,'gray'),plt.axis(False)
plt.subplot(3,2,4),plt.imshow(img_recortada3,'gray'),plt.axis(False)
plt.subplot(3,2,5),plt.imshow(img4,'gray'),plt.axis(False)
plt.subplot(3,2,6),plt.imshow(img_recortada4,'gray'),plt.axis(False)

