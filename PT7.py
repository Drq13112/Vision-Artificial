# -*- coding: utf-8 -*-
"""
SACA LA CIRCUNFERENCIA QUE APROXIMA UNA PIEZA 
@author: David

Para este ejercicio he diseñado un algoritmo que permite detectar la 
circunferencia interna  deu una brida.
Es necesario que la circunferencia interna tenga un perimetro menor a 900.
Sino no la detecta
"""

import cv2
import ransac 
import draw
import lms 
import numpy as np
        
img = cv2.imread('../imagenes/chaveta02.png',0)
#img = cv2.imread('../imagenes/arandelas_punta.png',0)

#Binarizo
img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

#No invierto la imagen para que detecte el circulo de dentro como un objeto independiente
#y por lo tanto pòder sacar su contorno con facilidad
#img_bin=cv2.bitwise_not(img_bin)

#Defino el kernel y hago una apertura y un cierre a la 
#Con esto trato de limpiar la imagen y elimiar pequeños agujeros o ruidos
kernel3 = np.ones((3, 3), np.uint8)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel3)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel3)


#Determino los objetos que hay en la imagen
num_labels,img_labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin, connectivity=8)

for i in range(1,num_labels):
    
     #imagen auxiliar
     img_aux = np.zeros_like(img_labels, np.uint8)
     img_aux[img_labels == i] = 1 
    
     #Busco los contornos de la imagen
     #En este caso voy a encontrar dos contornos, el de fuera y el interior del circulo
     contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
     cnt=contours[0]
     
     """
     #Dibujo el contorno detectado
     imgcontoursRGB=cv2.cvtColor(img_bin,cv2.COLOR_GRAY2RGB)
     imgcontoursRGB=cv2.drawContours(imgcontoursRGB,cnt, -1, (255,0,0),5)
     cv2.imshow(' ',imgcontoursRGB)
     cv2.waitKey(0)  
     """
     
     for j in range(len(contours)):
         
         #saco el perimetro
        x,y,w,h = cv2.boundingRect(cnt)
        perimeter = cv2.arcLength(cnt, True)# pongo true por que el contorno es cerrado
        
        if perimeter<900:

            #cogemos los puntos del único contorno externo que hay
            ptos_contornos=cnt
            
            #ransac para buscar rectas en los puntos de contorno
            #devuelve el mejor conjunto de puntos que se ajustan a una recta
            inliers= ransac.ransac_circunf(ptos_contornos,10) #80 iteraciones
            #aproximamos esos inliers a una 

            circABC=lms.circunf(inliers);   #minimos cuadrados sobre inliers
            draw.circunf_ABC(img, circABC, (255,0,0),3) 
        


    

