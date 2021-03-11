# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 13:18:57 2021

@author: david
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import noiselib as nl

img = cv2.imread('../Imagenes/caja06.png', 0)

#Defino todos los filtros

#Filtro de la media
def get_mean_filter(size):
    return np.ones((size, size)) / size**2


#Genero artificalmente las imagenes con varios tipos de ruidos
img_gauss = nl.add_gaussian_noise(img,0,5)
img_speckle = nl.add_speckle_noise(img)
img_sal_p = nl.add_salt_and_pepper_noise(img)

#Aplico los filtros a las imagenes con ruido

# filtro de la media; tamaño de la matriz 5x5
mean_5x5 = get_mean_filter(3)
img_filtered_mean1 = cv2.filter2D(img_gauss, -1, mean_5x5)
img_filtered_mean2 = cv2.filter2D(img_speckle, -1, mean_5x5)
img_filtered_mean3 = cv2.filter2D(img_sal_p, -1, mean_5x5)

#Filtro gaussiano
gauss_5x1 = cv2.getGaussianKernel(5, -1)  # tamaño 5x1 y -1 calcula la sigma
gauss_1x5 = np.transpose(gauss_5x1)
gauss_5x5 = gauss_5x1 @ gauss_1x5  # tamaño 5x5

img_filtered_gauss1 = cv2.filter2D(img_gauss, -1, gauss_5x5)
img_filtered_gauss2 = cv2.filter2D(img_speckle, -1, gauss_5x5)
img_filtered_gauss3 = cv2.filter2D(img_sal_p, -1, gauss_5x5)
imagenes=[img_gauss,img_speckle,img_sal_p,img_filtered_mean1,img_filtered_mean2,
              img_filtered_mean3,img_filtered_gauss1,img_filtered_gauss2,
              img_filtered_gauss3]
lista_nombres=['Ruido de gauss','Ruido de speckle','Ruido de sal y pimienta',
               'Ruido de gauss filtrado por media','Ruido de speckle filtrado por media',
               'Ruido de sal y pimienta filtrado por media',
               'Ruido de gauss filtrado por gauss','Ruido de speckle filtrado por gauss',
               'Ruido de sal y pimienta filtrado por gauss']
for i in range(9):
    
    #Imprimo por pantalla
    plt.subplot(3,3,i+1),plt.imshow(imagenes[i],'gray')
    plt.title(lista_nombres[i])
    plt.axis(False)