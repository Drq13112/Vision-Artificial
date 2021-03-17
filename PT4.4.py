# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:47:10 2021

@author: david
"""
import cv2 
import numpy as np
import matplotlib.pyplot as  plt

#Importo imagenes
img=cv2.imread("../imagenes/llave.jpg")

#Genero matrices
sobely=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

#Genero la matriz transpuesta, es decir la deverida respecto a y
sobelx=np.transpose(sobely)

#Filtramos las imágenes con esas máscaras
dx= cv2.filter2D(img, cv2.CV_64F, sobelx) #en CV_64F. habrá valores positivos y negativos
dy= cv2.filter2D(img, cv2.CV_64F, sobely)

plt.imshow(dx)
plt.show()
plt.imshow(dy)
plt.show()
plt.imshow(dy+dx)
