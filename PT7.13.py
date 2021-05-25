# -*- coding: utf-8 -*-
"""
Created on Sun May 23 14:03:54 2021

@author: david

Detector de fichas de dominó
"""

import cv2 
import numpy as np

def SACA_OBJETO(img):
    num_labels, img_labels= cv2.connectedComponents(img)
    for j in range(1,num_labels):
        img_aux = np.zeros_like(img_labels, np.uint8)
        img_aux[img_labels == j] = 255
        
        contours,_ = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        """
        #Lo imprimo por pantalla
        imgcontoursRGB=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
        imgcontoursRGB=cv2.drawContours(imgcontoursRGB,contours, -1, (255,0,0),5)
        cv2.imshow(' ',imgcontoursRGB)
        cv2.waitKey(0)
        """
        
    return num_labels
        
def Elimina_restos(img_bin):
    #Obtengo la cantidad de objetos, los mismos y sus stats
    num_labels, img_labels, stats, cg = cv2.connectedComponentsWithStats(img_bin)
    sizes = stats[1:, -1]; num_labels = num_labels - 1

    #Defino el size minimo
    #Todo aquello que tenga un tamaño menor se ese valor es eliminado
    min_size = 1000    
    img_bin_filtrada = np.zeros((img_labels.shape),np.uint8)
    for i in range(0, num_labels):
        if sizes[i] >= min_size:
            img_bin_filtrada[img_labels == i + 1] = 255 

    cv2.imshow('img_bin_filtrada',img_bin_filtrada)
    cv2.waitKey(0)  
    
    return img_bin_filtrada
        

def SeparaObjetos(img):
    """
    Las fichas de dominó estan muy proximas entre si, de modo que no voy a
    aplicar ningún filtro, pues esto me podría dar problemas a la hora de 
    identificar cada una de las fichas por separado.
    """
    # Binarizamos con Otsu
    _, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    #Trato de separar un poco más las fichas del dominó
    #Defino el kernel 
    Mat=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3),(-1,-1))
    img_bin=cv2.erode(img_bin,Mat,iterations=2)
    img_bin=cv2.dilate(img_bin,Mat,iterations=1)
    
    cv2.imshow('img_bin',img_bin)
    cv2.waitKey(0) 
    
    #Con esta función elimno los restos que hayan quedado depués 
    #de haber hecho un erode
    
    img_bin_filtrada=Elimina_restos(img_bin)
    cantidad=SACA_OBJETO(img_bin_filtrada)
    return cantidad

#-----------------------------------------------------------------------------
img=cv2.imread('../imagenes/domino-65136_1280.jpg',0)

cantidad=SeparaObjetos(img) 

print('La cantidad de piezas detectadas es: ',cantidad)