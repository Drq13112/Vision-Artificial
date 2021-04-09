# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:13:13 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Importo la imagen
img=cv2.imread('../imagenes/calculadora3.png',0)
#Filtro de Otsu para binarizar
img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
img_bin=cv2.bitwise_not(img_bin)
#Defino el kernel 
Mat=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5),(-1,-1))
    
#Someto a la imagen a proceso de erosión y dilaton 
#para poder diferenciar adecuamente cada tirafondos
img_bin=cv2.dilate(img_bin,Mat,iterations=5)
img_bin=cv2.erode(img_bin,Mat,iterations=2)

#Obtengo las caracteristicas 
num_labels, img_labels, stats, cg = cv2.connectedComponentsWithStats(img_bin)
#Defino el contorno de la calculadora
contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]
cv2.drawContours(img_bin,[cnt], 0, (0,255,0), 3)
((centx,centy), (width,height), angle)=cv2.fitEllipse(cnt)


#(int(cg[1][1]),int(cg[1][0]
#img_bin.shape[1],img_bin.shape[0]


M=cv2.getRotationMatrix2D((int(cg[1][0]),int(cg[1][1])),angle,1)
img = cv2.warpAffine(img,M,(img_bin.shape[1],img_bin.shape[0]))

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
img=cv2.resize(())
plt.imshow(img,'gray')



"""
ellipse = cv2.fitEllipse(contours)
centerE = ellipse[0]
# Gets rotation of ellipse; same as rotation of contour
rotation = ellipse[2]


"""
