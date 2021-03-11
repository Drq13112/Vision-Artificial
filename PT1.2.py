# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:25:40 2021

@author: 71325085s
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread('../Imagenes/caramelos.jpg')
img2=cv2.imread('../Imagenes/pastillas.jpg')
img3=cv2.imread('../Imagenes/Parrots.jpg')

def Planos_RGB(img):
    #Compruebo que se ha encontrado la imagen 
    assert not isinstance(img,type(None)), 'image not found'
    
    #Separo la imagen en los 3 planos
    B,G,R = cv2.split(img)
    
    #Junto los 3 planos para generar la imagen en formato RGB
    img_RGB = cv2.merge([R,G,B])
    
    #Obtengo la imagen en formato de grises
    img_gris=cv2.cvtColor(img_RGB, cv2.COLOR_RGB2GRAY)
    
    #Muestro por pantalla en formato de celdas
    plt.subplot(1,5,1),plt.imshow(B,'gray')
    plt.title("Azul")
    plt.axis(False) # to hide tick values on X and Y axis

    plt.subplot(1,5,2),plt.imshow(G,'gray')
    plt.title("Verde")
    plt.axis(False) # to hide tick values on X and Y axis

    plt.subplot(1,5,3),plt.imshow(R,'gray')
    plt.title("Rojo")
    plt.axis(False) # to hide tick values on X and Y axis

    plt.subplot(1,5,4),plt.imshow(img_RGB)
    plt.title("Original")
    plt.axis(False) # to hide tick values on X and Y 
    
    plt.subplot(1,5,5),plt.imshow(img_gris,'gray')
    plt.title("Original en grises")
    plt.axis(False) # to hide tick values on X and Y axis

def Planos_HSV(img):
    #Compruebo que se ha encontrado la imagen 
    assert not isinstance(img,type(None)), 'image not found'

    #Transformo la imagen BGR en formato HSV
    img_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    #Separo la imagen en los 3 planos HSV
    
    H,S,V=cv2.split(img_HSV)
    
    #Imprimo por pantalla
    plt.subplot(1,5,1),plt.imshow(H,'gray')
    plt.title("H")
    plt.axis(False) # to hide tick values on X and Y axis

    plt.subplot(1,5,2),plt.imshow(S,'gray')
    plt.title("S")
    plt.axis(False) # to hide tick values on X and Y axis

    plt.subplot(1,5,3),plt.imshow(V,'gray')
    plt.title("V")
    plt.axis(False) # to hide tick values on X and Y axis

    plt.subplot(1,5,4),plt.imshow(img_HSV)
    plt.title("HSV")
    plt.axis(False) # to hide tick values on X and Y axis

if __name__ == "__main__":
    Planos_RGB(img3)
    plt.show()
    Planos_HSV(img3)
