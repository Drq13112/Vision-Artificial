# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:54:03 2021

@author: david
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Importo las imagenes del directorio
img=cv2.imread('../Imagenes/caja.bmp')
img_0=cv2.imread('../Imagenes/caja.bmp',0)



# Funcion de binarizacion
def binaria_maker(img):
    umbral=128
    
    #creo una matriz uint8 donde escribiré la imag binaria. La pongo a ceros.
    binaria=np.zeros(img.shape, np.uint8) 
    
    filas,columnas=img.shape
    
    """
    Recorro la imagen y modifico los valores de la matriz binaria 
    en base a los resulatdos de la comparación
    """
    for i in range(filas):
        for j in range(columnas):
            if img[i][j] > umbral:
                binaria[i][j]=255
                
    return binaria

def Rectificador(img,p,q):
    filas,columnas=img.shape
    
    img_mod=img*0
    
    for i in range(filas):
        for j in range(columnas):
            
            if img[i][j]<255:
                
                img_mod[i][j]=img[i][j]*p+q
                
            if img[i][j]>=255:
                
                img_mod[i][j]=255
                
    return img_mod
                
#Paso la imagen a RGB para luego imprimirla por la terminal
img_RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Aplico las operaciones

#Invierte la imagen de grises
img1=255-img

#Oscurece la foto. Es necesario pasar el formato de nuevo a uint8
img2=img/2
img2 = img2.astype(np.uint8)

#Aclara la imagen
img3=img+50

#Binarizo la imagen
img4=binaria_maker(img_0)

#Invierto la imagen
img5=~img

#Imprimo los resulatdos por panatlla
plt.subplot(2,3,1),plt.imshow(img_RGB)
plt.title('Original')
plt.axis(False)

plt.subplot(2,3,2),plt.imshow(img1)
plt.title('Img1')
plt.axis(False)

plt.subplot(2,3,3),plt.imshow(img2)
plt.title('Img2')
plt.axis(False)

plt.subplot(2,3,4),plt.imshow(img3)
plt.title('Img3')
plt.axis(False)

plt.subplot(2,3,5),plt.imshow(img4,'gray')
plt.title('Img4')
plt.axis(False)

plt.subplot(2,3,6),plt.imshow(img5)
plt.title('Img5')
plt.axis(False)

#Importo la imagen
Im_color=cv2.imread('../Imagenes/toysflash.png')

#Separo los canales
R_=Im_color[:, :, 2]               #Canal R
R=Rectificador(R_,1,0)
R_C=np.clip(R,0,255)

G_= Im_color[:, :, 1] 
G=Rectificador(G_,1.1, 20)        #* 1.1 + 20  #Canal G
G_C=np.clip(G,0,255)
 
B_= Im_color[:, :, 0] 
B=Rectificador(B_, 1.3, 20)       #* 1.3 + 20   #Canal B
B_C=np.clip(B,0,255)

#Paso la imagen de BGR a RGB
Im_color=cv2.cvtColor(Im_color,cv2.COLOR_BGR2RGB)

#Modifico la imagen
img_corregida=img*0

img_corregida = cv2.merge([R_C,G_C,B_C])

#Imprimo por pantalla
plt.show()

plt.subplot(1,2,1),plt.imshow(Im_color)
plt.title('Imagen Original')
plt.axis(False)

plt.subplot(1,2,2),plt.imshow(img_corregida)
plt.title('Imagen Corregida')
plt.axis(False)


