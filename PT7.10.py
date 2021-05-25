# -*- coding: utf-8 -*-
"""
Created on Sun May 23 01:37:23 2021

@author: david

Deteccion de esquinas de rectangulos
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math




img=cv2.imread('../imagenes/matricula_coche_2.jpg',0)


#Binarización de otsu tras un suavizado gaussiano
blur = cv2.GaussianBlur(img,(5,5),0)
_,img_bin = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

num_labels, labels= cv2.connectedComponents(img_bin)

img_final=np.zeros_like(labels, np.uint8)

#Este parametro sirve para discrimar objetos pequeño que cumplen las caraterísticas
#pero que en realidad no son placas
area_max=0
for etiq in range(1,num_labels):
    img_aux = np.zeros_like(labels, np.uint8)
    img_aux[labels == etiq] = 255
    cnt, _ = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    """
    #Para ver los objetos seleccionados
    imgcontoursRGB=cv2.cvtColor(img_aux,cv2.COLOR_GRAY2RGB)
    imgcontoursRGB=cv2.drawContours(imgcontoursRGB,cnt, -1, (255,0,0),5)
    cv2.imshow(' ',imgcontoursRGB)
    cv2.waitKey(0)
    """
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
            #Hago esto porque la placa del coche tiene una forma muy especifica y regular
            #en comparación las formas irregulares y raras que van a aparecer 
            #en el resto de la binarización
            area_max=area
            
            #Muestro por la terminal
            img_final=img_aux
            #Paso a la imagen a RGB para pintar de color los puntos
            img_final=cv2.cvtColor(img_final,cv2.COLOR_GRAY2RGB)
            cv2.circle(img_final,(cx, cy), 5, (0,0,255), -1)
            
            #Calculo las esquinas del objeto detectado y calculo la esquina más alejada
            
            x, y, w, h = cv2.boundingRect(img_aux)          
                                                
            left = (x, np.argmax(img_aux[:, x]))                       
            right = (x+w-1, np.argmax(img_aux[:, x+w-1]))     
            top = (np.argmax(img_aux[y, :]), y)               
            bottom = (np.argmax(img_aux[y+h-1, :]), y+h-1)    
            
            Lista_esquinas=[left,right,top,bottom]
            
            #Ahora calculo la esquina más alejada
            modulo_max=0
            punto_aux=0
            
            for j in range(4):
                
                punto=Lista_esquinas[j]
                distancia_x=cx-punto[0]
                distancia_y=cy-punto[1]
                modulo=math.sqrt(pow(distancia_x,2)+pow(distancia_y,2))
                
                if modulo>modulo_max:
                    
                    modulo_max=modulo
                    punto_max=punto
                    
                    
                    #Pongo esta codición para que me examine las 4 esquinas 
                    #y posteriormente me dibuje la más alejada
                if j==3:
                    
                    # Dibujamos los ejes de la matrícula, la esquina y la recta que los une
                    cv2.line(img_final,(cx,y),(cx,y+h),(255,0,0),5)
                    cv2.line(img_final,(x,cy),(x+w,cy),(255,0,0),5)
                    cv2.circle(img_final,punto_max, 5, (0,0,255), -1)
                    cv2.line(img_final,(cx, cy),punto_max,(0,255,0),5)
            
        
cv2.imshow("Img_final",img_final)
cv2.waitKey()
            
            
