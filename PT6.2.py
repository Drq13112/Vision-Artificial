# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:54:40 2021

@author: david

Eliminar barras y pequeñas regiones de sudoku analizando formas
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Usa esta función en lugar del filtro de la media para que no afecte a los numeros
def Filtro_tamaño(img_bin,min_size):             
    
    #Elimino las particulas pequeñas con en este algoritmo
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(img_bin, connectivity=8)
    sizes = stats[1:, -1]; nb_components = nb_components - 1
    
    #Defino el size minimo
    #Todo aquello que tenga un tamaño menor se ese valor es eliminado
    img2 = np.zeros((output.shape))
    for i in range(0, nb_components):
        if sizes[i] >= min_size:
            img2[output == i + 1] = 255
    return img2

img=cv2.imread('../imagenes/sudoku.png',0)

#Filtro de Gauss para suavizar
img=cv2.GaussianBlur(img,(5,5),0)

#Binarizacion adaptativa
img_bin=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#Invierto de la imagen
img_bin=cv2.bitwise_not(img_bin)

plt.imshow(img_bin,'gray')
plt.axis(False)
plt.show()

#Ahora elimino las barras verticales y horizontales 
#Para ello me voya a basar en la diferencia de aspecto
#que hay entre las lineas de la cuadrícula y los números.
#Por ejemplo, los numeros tienen una altura y anchura menor.

#Obtengo la cantidad de numeros y barras 
num_labels,img_labels = cv2.connectedComponents(img_bin)

#Examino cada uno de los objetos.
#Para ello creo una imagen llena de ceros donde se irán copiando
#de uno en uno todos los objetos detectados por la función connectedComponents
#Posteriormente analizo el contorno de este único objeto y determino si es un
#número u otro elemento de la imagen

img_final=np.zeros_like(img_labels, np.uint8)
for j in range(num_labels):
    img_aux = np.zeros_like(img_labels, np.uint8)
    img_aux[img_labels == j] = 255
    contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt=contours[0]
    if j>=1:
        for i in range(len(contours)):
            x,y,w,h = cv2.boundingRect(cnt)
            #Mediante prueba y error he llegado a la conclusión 
            #de que esta es la mejor combinación
            if w<50 and h<50:
                img_final=img_aux+img_final

"""
plt.imshow(img_final,'gray')
plt.axis(False)
plt.show()
"""
#Pongo un filtro de aspecto
img_final=Filtro_tamaño(img_final,120)

plt.imshow(img_final,'gray')
plt.axis(False)
