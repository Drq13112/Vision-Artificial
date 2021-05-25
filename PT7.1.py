"""
Created on Sat Apr 10 16:08:19 2021

@author: david

Clasificación por la forma 
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def show_num_etiquetas(img_bin,identificador):
    num_labels, img_labels, stats, centroids = cv2.connectedComponentsWithStats(
        img_bin)

    font = cv2.FONT_HERSHEY_SIMPLEX
    #Se pasa la imagen de gray a RGB para poner el texto en color
    img_color = cv2.merge([img_bin, img_bin, img_bin])
    for i in range(1, num_labels): 
        
        cg = (int(centroids[i][0]), int(centroids[i][1]))
        cg_cg=(int(centroids[i][0]), int(centroids[i][1]+60))
        cv2.circle(img_color, cg, 3, (255, 0, 0), -1)
        if identificador==0:
            cv2.putText(img_color, 'rectangular', cg, font,4, (255, 0, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(img_color, 'circular', cg, font,4, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(img_color, str(cg), cg_cg, font,2, (255, 0, 0), 2, cv2.LINE_AA)
    
    return img_color
    
#--------------------------------------------------------------------------

img=cv2.imread('../imagenes/cuadradas-redondas.jpg',0)

#Filtro de Gauss para suavizar
img=cv2.GaussianBlur(img,(5,5),0)

#Filtro de Otsu para binarizar
img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#Defino el kernel y hago una apertura y un cierre a la imagen
#para evitar posibles agujeros en las galletas
#debido a la diferencia del brillo
kernel3 = np.ones((9, 9), np.uint8)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel3,iterations=3)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel3)

#Obtengo la cantidad de objetos 
num_labels,labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin)

img_not_circles = np.zeros_like(labels, np.uint8)
img_circles = np.zeros_like(labels, np.uint8)

# Discrimino por circularididad, las galletas circulares tienen una circulariad 
# mucho mayor que las rectangulares
for i in range(1,num_labels):
    img_aux = np.zeros_like(labels, np.uint8)
    img_aux[labels == i] = 255
    
    # Obtengo los contornos
    contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for j in contours:
        perimeter = cv2.arcLength(j, True)# pongo true por que el contorno es cerrado
        area = cv2.contourArea(j)
        if perimeter == 0:
            break
        circularity = 4*np.pi*(area/(perimeter*perimeter))
        if 0.7 < circularity:
            
            img_circles=img_aux+img_circles
        else :
            
            img_not_circles=img_aux+img_not_circles

#Genero el imagen con el etiquetado de las piezas circulares
img_circles=show_num_etiquetas(img_circles,1)

#Genero el etiquetado con el etiquetado de las piezas rectangulares
img_not_circles=show_num_etiquetas(img_not_circles,0)

#Junto las dos imagenes
img_final=img_circles+img_not_circles

plt.imshow(img_final)
plt.axis(False)

        

