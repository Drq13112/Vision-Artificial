# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 00:36:38 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Funcion que genera el histograma del foto que recibe como argumento
def miHistograma(img):
    filas,columnas =img.shape
    histo=np.zeros(256, dtype=int)
    
    for i in range(filas):
        for j in range(columnas):
            histo[ img[i][j] ] = histo[ img[i][j] ] + 1
    
    return(histo)

#Traigo una foto del directorio
img =cv2.imread('../Imagenes/deportivo5.jpg',0)

#Genero el histograma y paso la imagen a formato RGB
Histo_Original=miHistograma(img)

img_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Modifico el histograma con la funcion equilizeHist()
img_retocada=cv2.equalizeHist(img)

#Genero el histograma de la foto retocada y paso la foto a formato RGB
Histo_retocada=miHistograma(img_retocada)

img_retocada_RGB=cv2.cvtColor(img_retocada,cv2.COLOR_BGR2RGB)

#Defino los limtes de los histogramas
#x=np.linspace(0, 255,256)
plt.xlim(0,255)

#Imprimo por pantalla las imagenes
plt.subplot(2,2,1),plt.imshow(img_RGB)
plt.title('Foto Original')
plt.axis(False)

plt.subplot(2,2,2),plt.imshow(img_retocada_RGB)
plt.title('Foto Retocada')
plt.axis(False)

plt.subplot(2,2,3),plt.plot(Histo_Original)
plt.title('Histograma Original')

plt.subplot(2,2,4),plt.plot(Histo_retocada)
plt.title('Histograma Retocado')


    
    
    
    