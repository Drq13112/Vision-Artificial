# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 15:26:37 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

ptos1=[]

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global num_puntos, ptos1
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(limg,(x,y),5,(10,0,10),0)
        num_puntos +=1
        ptos1.append([x,y])

# Create a black image, a window and bind the function to window

#img = cv2.imread('../imagenes/caja_persp.png')
img = cv2.imread('../Imagenes/equal-foreshortening.png')

#Guardo el valor del tamaño de la imagen
fil=img.shape[0]
col=img.shape[1]
"""
Segun que imagen son demasiado grandes para la pantalla del pc.
De modo que reduzco la imagen a conveniencia de su tamaño.
Para ello uso la funcion cv2.resize()
"""
height=int(fil/2)
width=int(col/2)
dsize=(width,height)
limg= cv2.resize(img,dsize)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
num_puntos=0

while(num_puntos<4):
    
    cv2.imshow('image',limg)
    cv2.waitKey(10) 
    
ptos1 = np.float32(ptos1)
# ptos2 son los puntos donde mapeo ptos1. Es un rectangulo que empieza por
# la esquina superior izda y va en sentido horario
#ptos2 = np.float32([[200,125],[470,125],[470,315],[200,315]])

#"Automatizo" las dimensiones de la imagen para que se ajuste adecuadamente a cualquiera imagen
ptos2 = np.float32([[int(width/7),int(height/7)],[int(width-width/7),int(height/7)],[int(width-width/7),int(height-height/7)],[int(width/7),int(height-height/7)]])

#------cv2.getPerspectiveTransform()
M=cv2.getPerspectiveTransform(ptos1,ptos2)
#------cv2.warpPerspective()
dst=cv2.warpPerspective(limg,M,(width,height))


#Imprimo por pantalla
cv2.imshow('salida',dst)
cv2.waitKey(0) 


#Visualizar resultados con matplotlib
plt.subplot(1,2,1),plt.imshow(limg),plt.title('Input')
plt.axis(False)
plt.subplot(1,2,2),plt.imshow(dst),plt.title('Output')
plt.axis(False)
plt.show()

cv2.destroyAllWindows()




