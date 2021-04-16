# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:46:05 2021
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
@author: eusebio
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../imagenes/Carriles.jpg',0)
output = img_color=cv2.merge([img,img,img])
edges = cv2.Canny(img,50,150)
#llamaos a houghlines con la imagen de contornos
#1 es la resolucion en rho
#pi/180 es un grado de resolucion en tita
#el ultimo parametro es el umbral del contador para considerar recta
#cuanto mas bajo más rectas saldrán
lines = cv2.HoughLines(edges,1,np.pi/180, 270)
if lines is None:
    print('No se han encontrado rectas. Baja el umbral')
else:
    #dibuja las lineas encontradas
    print(f'Se han encontrado {len(lines)} rectas')
    for k in range(len(lines)):
        for rho,theta in lines[k]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
        
            cv2.line(output,(x1,y1),(x2,y2),(255,0,0),2)
        
    plt.imshow(output)
    plt.axis('off')
    plt.title("rectas Hough")
    plt.show()