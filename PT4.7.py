# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 01:25:34 2021

@author: david
"""

import cv2
import matplotlib.pyplot as plt

#importo imagen
img=cv2.imread('../imagenes/cojinetes.bmp',0)

#paso el filtro de la laplaciana
laplacian = cv2.Laplacian(img,cv2.CV_64F)

#Realizo la operacion de Img-Img pasada por filtro gaussiano
img_gauss=cv2.GaussianBlur(img,(1,1),cv2.BORDER_DEFAULT)
img_gauss2=cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)

#Resto las imagenes
imgfinal=img_gauss-img_gauss2

#imprimo por pantalla
plt.subplot(1,3,1),plt.imshow(img,'gray'),plt.title('Original',fontsize=25)
plt.subplot(1,3,2),plt.imshow(laplacian,'gray'),plt.title('Laplaciano',fontsize=25)
plt.subplot(1,3,3),plt.imshow(imgfinal,'gray'),plt.title('img_gauss(1,1)-img_gauss(3,3)',fontsize=25)
