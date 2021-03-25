# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:43:23 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
Imagen original->imagen en escala de grises
->filtro de ruido-> detector de bordes de canny
->detector de contornos
"""
#importo imagen en escala de grisis
img=cv2.imread('../imagenes/tirafondos0.png',0)

plt.imshow(img,'gray')
#defino la funcion
def CuentaObjetos(BW):
    
    
    img_filtered=cv2.GaussianBlur(BW,(5,5), 0)
     
    Mat=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5),(-1,-1))
    
    #Mat=np.ones((5,5),np.uint8)  
    img_eroded=cv2.erode(img_filtered,Mat,iterations=0)
    img_dilated=cv2.dilate(img_eroded,Mat,iterations=7)
    
    #Binarizo con canny
    img_canny=cv2.Canny(img_dilated,150,200)
    #Filtro la imagen con el filtro de gauss
   
    plt.imshow(img_canny,'gray')

    #Aplico el dectector de contornos
    #Para ello uso la funcion fincountours de OpenCV
    (contornos,_) = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # Mostramos el número de monedas por consola
    print("He encontrado {} objetos".format(len(contornos)))
     
    cv2.drawContours(BW,contornos,-1,(0,0,255), 2)
    
    cv2.imshow("contornos",img_canny)

img=cv2.bitwise_not(img)
contorno=CuentaObjetos(img)


    
    
    
    
