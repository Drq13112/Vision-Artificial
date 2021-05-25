# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:32:18 2021

@author: david

Reconocimiento de objetos diversos
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_num_etiquetas(img_bin):
    num_labels, img_labels, stats, centroids = cv2.connectedComponentsWithStats(
        img_bin)

    font = cv2.FONT_HERSHEY_SIMPLEX
    img_color = cv2.merge([img_bin, img_bin, img_bin])
    for i in range(1, num_labels): 
        
        cg = (int(centroids[i][0]), int(centroids[i][1]))
        cv2.circle(img_color, cg, 3, (255, 0, 0), -1)
        cv2.putText(img_color, str(i), cg, font,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
    plt.imshow(img_color)
    plt.axis('off')
    plt.title("Imagen")
    plt.show()
    
    
    
    
    
#img=cv2.imread('../Imagenes/tuercas_tornillo2.bmp',0)
img=cv2.imread('../Imagenes/tuercas_tornillos3.bmp',0)
img=cv2.imread('../Imagenes/llave_tornillos.png',0)
img=cv2.imread('../Imagenes/llaves1.bmp',0)
img=cv2.imread('../Imagenes/pinon1.png',0)
img=cv2.imread('../Imagenes/corona1.bmp',0)
img=cv2.imread('../Imagenes/corona0.bmp',0)
img=cv2.imread('../Imagenes/brida.png',0)


#Filtro de Gauss para suavizar
img=cv2.GaussianBlur(img,(3,3),0)

#Filtro de Otsu para binarizar
img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#Defino el kernel y hago una apertura y un cierre a la imagen
kernel3 = np.ones((3, 3), np.uint8)

#img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel3)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel3)

#Obtengo la cantidad de objetos 
num_labels,labels, stats, centroids = cv2.connectedComponentsWithStats(img_bin)

show_num_etiquetas(img_bin)

#Defino todos los arrays donde voy a insertar el número que corresponde a cada objeto
#Cada array tiene el tamaño de la cantidad de objetos que hya en la imagen
#y esta lleno de ceros.
#De esta forma  los objetos se colocaran en la posición del array que concuerda con el número
# que le ha dado la función connectedComponents
Arandelas=[0]*num_labels
Tuercas=[0]*num_labels
Tornillos=[0]*num_labels
Llave_fija=[0]*num_labels
Llave_estrella=[0]*num_labels
Bridas=[0]*num_labels
Piñones=[0]*num_labels
Coronas=[0]*num_labels

#Clasifico
for i in range(1,num_labels):
    img_aux = np.zeros_like(labels, np.uint8)
    img_aux[labels == i] = 255
    
    # Obtengo los contornos
    contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    cnt=contours[0]
    for j in range(len(contours)):
        x,y,w,h = cv2.boundingRect(cnt)
        perimeter = cv2.arcLength(cnt, True)# pongo true por que el contorno es cerrado
        area = cv2.contourArea(cnt)
        _,_,_,_, marco_area = stats[i]
        area_relativa=area/marco_area
        circularity = 4*np.pi*(area/(perimeter*perimeter))
        
        #Para mostrar el contorno que toma la 
        """
        imgcontoursRGB=cv2.cvtColor(img_aux,cv2.COLOR_GRAY2RGB)
        imgcontoursRGB=cv2.drawContours(imgcontoursRGB,contours, -1, (255,0,0),5)
        cv2.imshow(' ',imgcontoursRGB)
        cv2.waitKey(0)
        """
        _,y,_=hierarchy.shape
        if perimeter == 0:
            break
        if y>3:
            if 0.8<circularity:
                Bridas.insert(i,i)
                break
            else :
                Coronas.insert(i,i)
                break
        if y==3:
            Llave_estrella.insert(i,i)
            break
        if y==2:
            if 0.7<circularity and area_relativa>0.9:
                Arandelas.insert(i,i)
                break
            if 0.7<circularity and area_relativa<0.5:
                Tuercas.insert(i,i)
                break
            if 0.5<circularity and area>10000:
                Piñones.insert(i,i)
                break
            if 0.8<circularity and area_relativa<0.1:
                Bridas.insert(i,i)
                break
            
        if y==1 and area>3500 and 0.8>circularity:
            Llave_fija.insert(i,i)
            break
        if y==1 and area<=3500 and 0.8>circularity:
            Tornillos.insert(i,i)
            break 



#------------------------------------------------------------------------------

#Muestro por pantalla
Lista_objetos_letra=['Cantidad de arandelas','Cantidad de tuercas',
               'Cantidad de llaves estrella','Cantidad de llaves fijas'
               ,'Cantidad de tornillos','Cantidad de piñones','Cantidad de coronas','Cantidad de bridas']

Lista_objetos2=[Arandelas,Tuercas,Llave_estrella,Llave_fija,Tornillos,Piñones,
               Coronas,Bridas]

Lista_Aux=[]
Lista_Aux2=[]

for i in range(len(Lista_objetos_letra)):
    Lista_Aux=Lista_objetos2[i]
    for j in range(len(Lista_objetos2[i])):
        if Lista_Aux[j]!=0:
            Lista_Aux2.append(j)
            
    print(Lista_objetos_letra[i],len(Lista_Aux2))
    
    if len(Lista_objetos2[i])!=num_labels:  
        print('Está formado por los objetos:',Lista_Aux2)
    print(' ')    
    Lista_Aux2=[]
        

            
            
        
            
        
        
        
        
