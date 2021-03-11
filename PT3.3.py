# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:34:16 2021

@author: david
"""
import noiselib as nl
import cv2 
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('../Imagenes/caja06.png', 0)
def min_filter(src, tam):
    '''Devuelve la imagen dst resultante de pasar un filtro del minimo 
    de tamaño tam a la imagen src'''
    shape = cv2.MORPH_RECT  # indica que el filtro es rectang
    size = (tam, tam)  # definimos un filtro cuadrado
    kernel = cv2.getStructuringElement(shape, size)  # crea elem.estructurador
    dst = cv2.erode(src, kernel)
    return dst


def max_filter(src, tam):
    '''Devuelve la imagen dst resultante de pasar un filtro del maximo 
    de tamaño tam a la imagen src'''
    shape = cv2.MORPH_RECT  # indica que el filtro es rectang
    size = (tam, tam)  # definimos un filtro cuadrado
    kernel = cv2.getStructuringElement(shape, size)  # crea elem.estructurador
    dst = cv2.dilate(src, kernel)
    return dst

#Genero artificalmente las imagenes con varios tipos de ruidos
img_gauss = nl.add_gaussian_noise(img,0,5)
img_speckle = nl.add_speckle_noise(img)
img_sal_p = nl.add_salt_and_pepper_noise(img)

#Filtro de la mediana; tamaño 3
img_filtered_median1 = cv2.medianBlur(img_gauss, 5)  
img_filtered_median2 = cv2.medianBlur(img_speckle, 5)
img_filtered_median3 = cv2.medianBlur(img_sal_p, 5)

#Filtor del minimo
img_filtered_min1 = min_filter(img_gauss, 3)
img_filtered_min2 = min_filter(img_speckle, 3)
img_filtered_min3 = min_filter(img_sal_p, 3)

#Filtro del máximo
img_filtered_max1 = max_filter(img_gauss, 3)
img_filtered_max2 = max_filter(img_speckle, 3)
img_filtered_max3 = max_filter(img_sal_p, 3)
#Imprimo por pantalla
imagenes=[img_gauss,img_speckle,img_sal_p,img_filtered_median1,img_filtered_median2,
              img_filtered_median3,img_filtered_min1,img_filtered_min2,
              img_filtered_min3,img_filtered_max1,img_filtered_max2,img_filtered_max3]

lista_nombres=['Ruido de gauss','Ruido de speckle','Ruido de sal y pimienta',
               'Ruido de gauss filtrado por mediana','Ruido de speckle filtrado por mediana',
               'Ruido de sal y pimienta filtrado por mediana',
               'Ruido de gauss filtrado por mínimo','Ruido de speckle filtrado por mínimo',
               'Ruido de sal y pimienta filtrado por mínimo',
               'Ruido de gauss filtrado por máximo','Ruido de speckle filtrado por máximo',
               'Ruido de sal y pimienta filtrado por máximo']
for i in range(12):
    #Imprimo por pantalla
    plt.subplot(4,3,i+1),plt.imshow(imagenes[i],'gray')
    plt.title(lista_nombres[i])
    plt.axis(False)