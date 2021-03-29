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
def CuentaObjetos(BW,blocksize):
    
    #Uso un filtro de Gauss para suavizar la foto
    img_filtered=cv2.GaussianBlur(BW,(5,5), 0)
    
    #Binarizo la foto con OTSU
    otsu_threshold, img_bin = cv2.threshold(BW, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    #Defino el kernel 
    Mat=cv2.getStructuringElement(cv2.MORPH_RECT,(blocksize,blocksize),(-1,-1))
    
    #Someto a la imagen a proceso de erosión y dilaton 
    #para poder diferenciar adecuamente cada tirafondos
    img_eroded=cv2.erode(img_bin,Mat,iterations=5)
    img_dilated=cv2.dilate(img_eroded,Mat,iterations=2)
    
    #Obtengo la cantidad de objetos que hay e la imagen
    retval,labels=cv2.connectedComponents(img_dilated)
    
    #Saco por pantalla la cantidad de objetos que hay
    #Le resto 1 por que la función tiene en cuenta el fondo
    print('Cantidad de objetos en la imagen:',retval-1)
    plt.imshow(img_dilated,'gray')

img=cv2.bitwise_not(img)
contorno=CuentaObjetos(img,5)


    
    
    
    
