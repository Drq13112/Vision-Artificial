# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:58:50 2021

@author: david

Diseño un agloritmo que detecta si los objetos de la imagen son iguales
"""
import cv2 
import numpy as np
import matplotlib.pyplot as plt

def SACA_OBJETO(img,num_labels,img_labels):
    
    #Defino el contorno del objeto y su orientación 
    
    list_imagenes=[]
    list_contours=[]
    for j in range(1,num_labels):
        img_aux = np.zeros_like(img_labels, np.uint8)
        img_aux[img_labels == j] = 1
        
        contours,_ = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       
        list_imagenes.append(img_aux)
        list_contours.append(contours[0])
        
        #plt.imshow(img_aux,'gray')
    return list_imagenes,list_contours

def SeparaObjetos(img):
    
    # Primero filtramos la imagen y luego la binarizamos con Otsu
    img_suavizada = cv2.medianBlur(img,7)
    _, img_bin = cv2.threshold(img_suavizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    
    #Defino el kernel y hago una apertura y un cierre a la 
    #Con esto trato de limpiar la imagen y elimiar pequeños agujeros o ruidos
    kernel3 = np.ones((5, 5), np.uint8)
    img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel3)
    img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel3)
    
    #Obtengo la cantidad de objetos, los mismos y sus stats
    num_labels, img_labels, stats, cg = cv2.connectedComponentsWithStats(img_bin)
    
    
        
    List_imagenes,List_contours=SACA_OBJETO(img_bin, num_labels, img_labels)
    List_imagenes_corregidas=[]
    
    for i in range(num_labels-1):
        img_bin=List_imagenes[i]
        cnt=List_contours[i]
        
        ((centx,centy), (width,height), angle)=cv2.fitEllipse(cnt)
        
        #Giro la imagen de tal forma que la llave quede verticalmente en una nueva foto
        M=cv2.getRotationMatrix2D((int(cg[1][0]),int(cg[1][1])),angle,1)
        
        img_bin= cv2.warpAffine(img_bin,M,(img_bin.shape[0],img_bin.shape[1]))
        
        contours2,_= cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            
        #Recorto la imagen 
        x,y,w,h = cv2.boundingRect(contours2[0])
        img_bin = img_bin[y:y+h,x:x+w]
        
        #Compruebo que la imagen esta colocada correctamente
        img_abajo=img_bin[int(img_bin.shape[0]/2.1):img_bin.shape[0]]
        img_arriba=img_bin[0:int(img_bin.shape[0]/2.1)]
        
        contours3, hierarchy = cv2.findContours(img_abajo, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        
        #Lo imprimo por pantalla
        imgcontoursRGB=cv2.cvtColor(img_bin,cv2.COLOR_GRAY2RGB)
        imgcontoursRGB=cv2.drawContours(imgcontoursRGB,contours3, -1, (255,0,0),5)
        cv2.imshow(' ',imgcontoursRGB)
        cv2.waitKey(0)
        
        plt.subplot(1, 2, i+1),plt.imshow(img_bin,'gray')
        if hierarchy.shape[1]>1:
            print('esta al reves')   
            ((centx,centy), (width,height), angle)=cv2.fitEllipse(contours2[0])
            img_bin=cv2.rotate(img_bin,cv2.cv2.ROTATE_180)
            
        List_imagenes_corregidas.append(img_bin)    
        plt.subplot(1, 2, i+1),plt.imshow(img_bin,'gray')
                
    return List_imagenes_corregidas
    


img=cv2.imread('../imagenes/parllaves1.JPG',0)
#Invierto la imagen
img=cv2.bitwise_not(img)

#La funcion separa objetos devuelve un array
#con todos los objetos de la imagen separados en 
#imagenes independientes y con los objetos correctamente orientados
List_imagenes_corregidas=SeparaObjetos(img) 

plt.show()
img1=List_imagenes_corregidas[0]
img2=List_imagenes_corregidas[1]

#Normalizo el tamaño de las imagenes, 
#siendo la más pequeña la que marca el tamaño de los marcos
if img1.shape[1]>img2.shape[1]:
    x=img1.shape[1]
else:
    x=img2.shape[1]
    
if img1.shape[0]>img2.shape[0]:
    y=img1.shape[0]
else:
    y=img2.shape[0]
    
#Rescalo las imagenes a losnuevos marcos
img1 = cv2.resize(img1,(x,y), interpolation=cv2.INTER_CUBIC)
img2 = cv2.resize(img2,(x,y), interpolation=cv2.INTER_CUBIC)
#img2=cv2.bitwise_not(img2)
img_resta1=img1-img2
img_resta2=-img1+img2

#Saco las areas de cada uno de los objetos
contours,_= cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
area1 = cv2.contourArea(contours[0])

contours,_= cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
area2 = cv2.contourArea(contours[0])

print(area1,'and', area2,'resta:', area2-area1)
plt.subplot(1,2,1), plt.imshow(img_resta1,'gray')
plt.subplot(1,2,2), plt.imshow(img_resta2,'gray')
    

