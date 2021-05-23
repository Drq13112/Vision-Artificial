# -*- coding: utf-8 -*-
"""
Created on Sun May 23 01:37:23 2021

@author: david
Deteccion de esquinas de rectangulos
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('../imagenes/matricula_coche_1.jpg',0)

#Binarización de otsu tras un suavizado gaussiano
blur = cv2.GaussianBlur(img,(5,5),0)
_,img_bin = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Aplicamo morfología para eliminar las letras qeu están dentro de la matrícula
kernel3 = np.ones((13, 13), np.uint8)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel3)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel3)
num_labels, labels= cv2.connectedComponents(img_bin)

img_final=np.zeros_like(labels, np.uint8)


area_max=0
for etiq in range(1,num_labels):
    img_aux = np.zeros_like(labels, np.uint8)
    img_aux[labels == etiq] = 1
    cnt, _ = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
    #Para ver los objetos seleccionados
    imgcontoursRGB=cv2.cvtColor(img_aux,cv2.COLOR_GRAY2RGB)
    imgcontoursRGB=cv2.drawContours(imgcontoursRGB,cnt, -1, (255,0,0),5)
    cv2.imshow(' ',imgcontoursRGB)
    cv2.waitKey(0)
    
    for i in range(len(cnt)):
        
        #Aspecto
        x, y, w, h = cv2.boundingRect(cnt[i])
        
        #circularidad
        a = cv2.contourArea(cnt[i])
        p= cv2.arcLength(cnt[i], True)  # true porque cont es cerrado
        if p!=0:
            circularidad= (4.0*np.pi*a)/(p*p)
        
        #Area
        hull = cv2.convexHull(cnt[i])
        area= cv2.contourArea(hull)
        
        if w/h>2 and area>area_max and circularidad>0.3:
            
            #Centro de gravedad
            momentos = cv2.moments(cnt[i])
            cx = int(momentos['m10']/momentos['m00'])
            cy = int(momentos['m01']/momentos['m00'])
            
            #Con esta linea me aseguro de que se escoge el objeto con más area
            area_max=area
            
            #Muestro por la terminal
            img_final=img_aux
            
            cv2.circle(img_final,(cx, cy), 5, (0,255,0), -1)
            """
            cv2.imshow('aqui',img_final)
            cv2.waitKey(0)
            """
        
plt.imshow(img_final,'gray')
plt.axis('off')
plt.title("Imagen")
plt.show()

