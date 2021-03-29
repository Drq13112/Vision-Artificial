# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:47:10 2021

@author: david
"""
import cv2 
import numpy as np
import matplotlib.pyplot as  plt

#Importo imagenes
img=cv2.imread("../imagenes/murallas.bmp",0)

#Para sacar los contornos que proporciona el filtro de Sobel con umbral1=umbral2
edgesSobel = cv2.Canny(img,100,100)

#Genero matrices
sobely=np.array([[-1,-2,-1],
                 [0,0,0],
                 [1,2,1]])

#Genero la matriz transpuesta, es decir la deverida respecto a y
sobelx=np.transpose(sobely)

#Filtramos las imágenes con esas máscaras
dx= cv2.filter2D(img, cv2.CV_64F, sobelx) #en CV_64F. habrá valores positivos y negativos
dy= cv2.filter2D(img, cv2.CV_64F, sobely)

#Scales, calculates absolute values, and converts the result to 8-bit
dx_abs=cv2.convertScaleAbs(dx)
dy_abs=cv2.convertScaleAbs(dy)

#Obtengo el modulo del gradiente
module=cv2.addWeighted(dx_abs,0.5,dy_abs,0.5,0)

#Resultado de binarizar el modulo del gradiente
otsu_threshold, img_bin = cv2.threshold(module, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#Imprimo por pantalla
plt.subplot(2,2,1),plt.imshow(dx,'gray'),plt.title('Componente Horizontal',fontsize=25)
plt.subplot(2,2,2),plt.imshow(dy,'gray'),plt.title('Componente Vertical',fontsize=25)
plt.subplot(2,2,3),plt.imshow(module,'gray'),plt.title('Modulo del gradiente',fontsize=25)
plt.subplot(2,2,4),plt.imshow(img_bin,'gray'),plt.title('Modulo binarizado',fontsize=25)
cv2.imshow('Usando el filtro de Canny',edgesSobel)
cv2.waitKey(0) 
cv2.destroyAllWindows()
