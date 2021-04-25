# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 09:45:11 2021

@author: david
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('../imagenes/monedas.jpg',0)

#output = img_color=cv2.merge([img,img,img])

img=cv2.bitwise_not(img)

#Filtro de Gauss para suavizar
img=cv2.GaussianBlur(img,(5,5),0)

#Binarizacion adaptativa
ret3,th3 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Determino la cantidad de circulos que hay 
#ret, labels=cv2.connectedComponents(th3,connectivity=4)

#Itero
img_final=np.zeros_like(img.shape, np.uint8)
circles = cv2.HoughCircles(th3, cv2.HOUGH_GRADIENT, 1.2, 100)
for (x, y, r) in circles:  
        
        cv2.circle(img_final, (x, y), r, (255, 0, 0), 2)
        cv2.rectangle(img_final, (x - 5, y - 5), (x + 5, y + 5), (255, 255, 0), -1)
        
plt.imshow(img_final,'gray')
plt.axis('off')
plt.title("rectas")
plt.show()
"""
for j in range(len(circles)):
    
#    img_aux = np.zeros_like(labels, np.uint8)
#    img_aux[labels == j] = 1
    circles = cv2.HoughCircles(img_aux, cv2.HOUGH_GRADIENT, 1.2, 100)
    
    if circles is not None:
    	circles = np.round(circles[0, :]).astype("int")
    
    for (x, y, r) in circles:  
        
        cv2.circle(img_final, (x, y), r, (255, 0, 0), 2)
        cv2.rectangle(img_final, (x - 5, y - 5), (x + 5, y + 5), (255, 255, 0), -1)
"""        

