# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 19:43:34 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('../Imagenes/tornillo_fondo_negro.jpg',0)

#Creo la funcion que binariza la imagen
def binaria_maker(img):
    #creo una matriz uint8 donde escribiré la imag binaria. La pongo a ceros.
    binaria=np.zeros(img.shape, np.uint8) 
    
    filas,columnas=img.shape
    for i in range(filas):
        for j in range(columnas):
            if img[i][j] > 20: 
                binaria[i][j]=255

    """
    He puesto el umbral muy bajo para que se tome mejor la silueta 
    y opacidad del tornillo de forma que las mediones sean mas exactas      
    """          
    return binaria

#Creo la función que calcula el largo del tornillo
def Largo(img):
    filas,columnas=img.shape
    contador_max=0
    
    for i in range(filas):  
        contador=0
        for j in range(columnas):
            if img [i][j]==255: 
                contador=contador+1
        if contador>contador_max:
            contador_max=contador
                
    return contador_max

#Creo la función que determina la altura del tornillo           
def Altura(img):
    
    filas,columnas=img.shape
    contador_max=0
    
    for i in range(columnas):  
        contador=0
        
        for j in range(filas):
            if img [j][i]>1: 
                contador=contador+1
                
        if contador>contador_max:
            contador_max=contador
                
    return contador_max

#Ejecuto las funciones y las imprimo los resultados y la imagen binarizada
img1=binaria_maker(img)
print("largo",Largo(img1))
print("Alura",Altura(img1))
plt.imshow(img1,'gray')