# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:45:20 2021

@author: david
"""

import cv2
import numpy as np
from numpy.linalg import inv 
from matplotlib import pyplot as plt

#Genero las matrices con las que voy a trabajar
S=np.float32([[0.5,0,0],[0,0.5,0],[0,0,1]])
U=np.float32([[2,0,0],[0,2,0],[0,0,1]])
T=np.float32([[1,0,100],[0,1,10],[0,0,1]])
R=np.float32([[0.707,-0.707,0],[0.707,0.707,0],[0,0,1]])
Q=np.float32([[1,0,320],[0,1,240],[0,0,1]])
Y=np.float32([[1,0,-320],[0,1,-240],[0,0,1]])
Total=Q@R@Y

lista=[S,U,T,R,Q,Y,Total]
lista_nombres=['S','U','T','R','Q','Y','Total']

#importo la imagen
img=cv2.imread('../Imagenes/caja06.png',0)

#Defino la funcion
def Transforma(img,S):
    fil,col=img.shape
    S_inv=inv(S)
    img_resultado=img*0
    for xT in range(col):
        for yT in range(fil):
            
            matrix= np.float32([[xT],[yT],[1]])
            x,y,z=S_inv@matrix
            
            if y<fil and x<col:
                
                img_resultado[yT][xT]=img[int(y)][int(x)]
            
            else:
                img_resultado[yT][xT]=img[fil-1][col-1]
            
            
    return img_resultado
#Ejucto la funcion y imprimo los resultados por pantalla
"""
for i in range(7):
    
   img2=Transforma(img,lista[i])
   plt.subplot(3,3,i+1)
   plt.imshow(img2,'gray')
   plt.axis(False)
   plt.title(lista_nombres[i])

plt.subplot(3,3,7),plt.imshow(img,'gray')
plt.axis(False)
plt.title('Originial')


#Aplico las 3 matrices secuencialmente
img3=Transforma(img,Q)
img4=Transforma(img3,R)
img5=Transforma(img4,Y)
img6=Transforma(img,Total)

plt.subplot(2,2,1),plt.imshow(img6,'gray')
plt.axis(False)
plt.title('Transfromación No sequencial')

plt.subplot(2,2,2),plt.imshow(img3,'gray')
plt.axis(False)
plt.title('Aplico Q')

plt.subplot(2,2,3),plt.imshow(img4,'gray')
plt.axis(False)
plt.title('')

plt.subplot(2,2,4),plt.imshow(img5,'gray')
plt.axis(False)
plt.title('Aplico Q, R y después Y')
"""

fil,col=img.shape
height=int(fil/2)
width=int(col/2)
dsize=(width,height)

#resize()
img_rescalada=cv2.resize(img,dsize)

#rotate()
img_rotada=cv2.rotate(img,cv2.cv2.ROTATE_90_CLOCKWISE)

#Imprimo por pantalla
plt.subplot(2,1,1),plt.imshow(img_rotada,'gray')
plt.axis(False)
plt.title('rotate')

plt.subplot(2,1,2),plt.imshow(img_rescalada,'gray')
plt.axis(False)
plt.title('resize')


cv2.destroyAllWindows()


