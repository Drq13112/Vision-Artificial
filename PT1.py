# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:19:09 2021

@author: 71325085s
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Cargo las imagenes del directorio
img1=cv2.imread('../Imagenes/Cameraman.tif')
img2=cv2.imread('../Imagenes/cojinetes.bmp')
img3=cv2.imread('../Imagenes/rice.png')
img4=cv2.imread('../Imagenes/Parrots.jpg')

#Paso de BGR a RGB
B, G, R = cv2.split(img4)
 
#crea imagen RGB 
img_RGB=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

#Obtengo una de los canales por separado
rojo  = cv2.merge([ R,  G*0, B*0])
verde = cv2.merge([R*0,  G,  B*0])
azul  = cv2.merge([R*0, G*0,  B])

#Uso la funcion help
help(img1)

#Muestro por pantalla en formato de celdas
plt.subplot(1,4,1),plt.imshow(azul)
plt.title("Azul")
plt.axis(False) # to hide tick values on X and Y axis

plt.subplot(1,4,2),plt.imshow(verde)
plt.title("Verde")
plt.axis(False) # to hide tick values on X and Y axis

plt.subplot(1,4,3),plt.imshow(rojo)
plt.title("Rojo")
plt.axis(False) # to hide tick values on X and Y axis

plt.subplot(1,4,4),plt.imshow(img4)
plt.title("Original")
plt.axis(False) # to hide tick values on X and Y axis


#Imprimo por pantalla la longitud y el ancho de la imagen
print(img1.shape[0:2])