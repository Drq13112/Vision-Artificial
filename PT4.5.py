# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:45:12 2021

@author: david
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#Importo imagenes
img=cv2.imread('../Imagenes/llave.jpg',0)


gauss_5x1 = cv2.getGaussianKernel(5, -1)  # tamaño 5x1 y -1 calcula la sigma
gauss_1x5 = np.transpose(gauss_5x1)
gauss_5x5 = gauss_5x1 @ gauss_1x5  # tamaño 5x5

img_filtered_gauss = cv2.filter2D(img, -1, gauss_5x5)

#Filtro de canny con umbral1=umbral2=100->Filtro de Sobel
edgesSobel=cv2.Canny(img,100,100)

#Sobel sobre el filtro de gauss
edgesSobel1=cv2.Canny(img_filtered_gauss,100,100)

plt.subplot(1,3,1),plt.imshow(edgesSobel,'gray'),plt.title('Sobel sin filtro de Gauss',fontsize=25)
plt.subplot(1,3,2),plt.imshow(edgesSobel1,'gray'),plt.title('Sobel con filtro de Gauss',fontsize=25)
#----------------------------------------------------------------------

#Ahora voy a comparar el filtro de Sobel con el de Canny
#umbral minimo=100;umbral maximo=200
img_canny=cv2.Canny(img,100,200)
plt.subplot(1,3,1),plt.imshow(img_canny,'gray'),plt.title('Filtro de Canny',fontsize=25)
plt.subplot(1,3,2),plt.imshow(edgesSobel,'gray'),plt.title('Sobel sin filtro de Gauss',fontsize=25)
plt.subplot(1,3,3),plt.imshow(edgesSobel1,'gray'),plt.title('Sobel con filtro de Gauss',fontsize=25)



