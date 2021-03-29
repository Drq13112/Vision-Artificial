# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:59:44 2021

@author: david
"""

import cv2
import matplotlib.pyplot as plt
import noiselib as nl

img=cv2.imread('../imagenes/perritos.jpg',0)

#Genero ruido de gauss
img_filtered_gauss = nl.add_gaussian_noise(img,0,5)

#Aplico el filtro de Canny con imganes con ruido gaussiano
edgesSobel1=cv2.Canny(img_filtered_gauss,100,200)
edgesSobel2=cv2.Canny(img_filtered_gauss,50,100)
edgesSobel3=cv2.Canny(img_filtered_gauss,200,250)
edgesSobel4=cv2.Canny(img_filtered_gauss,50,250)

plt.subplot(2,2,1),plt.imshow(edgesSobel1,'gray'),plt.title('Canny con ruido de Gauss; config:100,200',fontsize=25)
plt.subplot(2,2,2),plt.imshow(edgesSobel2,'gray'),plt.title('Canny con ruido de Gauss; config:50,100',fontsize=25)
plt.subplot(2,2,3),plt.imshow(edgesSobel3,'gray'),plt.title('Canny con ruido de Gauss; config:200,250',fontsize=25)
plt.subplot(2,2,4),plt.imshow(edgesSobel4,'gray'),plt.title('Canny con ruido de Gauss; config:50,250',fontsize=25)
#------------------------------------------------
#Ahora voy a probar a hacer lo mismo pero teniendo ruido de sal y pimmienta

img_sal_p= nl.add_salt_and_pepper_noise(img)
edgesSobel1=cv2.Canny(img_sal_p,100,200)
edgesSobel2=cv2.Canny(img_sal_p,50,100)
edgesSobel3=cv2.Canny(img_sal_p,200,250)
edgesSobel4=cv2.Canny(img_sal_p,50,250)

plt.subplot(2,2,1),plt.imshow(edgesSobel1,'gray'),plt.title('Canny con ruido de sal y pimienta; config:100,200',fontsize=25)
plt.subplot(2,2,2),plt.imshow(edgesSobel2,'gray'),plt.title('Canny con ruido de sal y pimienta; config:50,100',fontsize=25)
plt.subplot(2,2,3),plt.imshow(edgesSobel3,'gray'),plt.title('Canny con ruido de sal y pimienta; config:200,250',fontsize=25)
plt.subplot(2,2,4),plt.imshow(edgesSobel4,'gray'),plt.title('Canny con ruido de sal y pimienta; config:50,250',fontsize=25)

