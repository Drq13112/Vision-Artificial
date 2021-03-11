# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:23:52 2021

@author: david
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img =cv2.imread('../Imagenes/deportivo5.jpg',0)

#Obtengo el histograma de la foto para trabajar con el
hist,bins = np.histogram(img.flatten(),256,[0,256])

#Calculo la suma acumulada del histograma
cdf = hist.cumsum()

#Genero una mascara con los valores iguales a cero de la suma acumulada
cdf_mask = np.ma.masked_equal(cdf,0)

#Estiro el histograma y se aplico a la foto
cdf = (cdf - cdf.min())*255/(cdf.max()-cdf.min())
img2 = cdf[img]

#Paso la imagen de formato float a uint8 para hacer el histograma
img3= img2.astype(np.uint8)


#Paso del formato BGR a RGB
img_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_RGB_retocada=cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)

#Imprimo los datos por pantalla
plt.subplot(2,2,1),plt.imshow(img_RGB)
plt.title('Foto Original')
plt.axis(False)

plt.subplot(2,2,2),plt.imshow(img_RGB_retocada)

plt.subplot(2,2,3),plt.hist(img.flatten(),256,[0,256])
plt.title('Histograma Original')

plt.title('Foto Retocada')
plt.axis(False)
plt.subplot(2,2,4),plt.hist(img3.flatten(),256,[0,256])
plt.title('Histograma Retocado')

#Imprimo de nuevo el histograma porque con el sublot se pierden algunos detalles
plt.show()
plt.hist(img3.flatten(),256,[0,256])
plt.title('Histograma Retocado')

