# -*- coding: utf-8 -*-
"""
Created on Sat May 22 18:32:12 2021

@author: david
Programa que clasifica objetos presentes en la imagen emdinate el método K-means
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from imutils.contours import sort_contours




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
    
    
    
#Importo la imagen
img = cv2.imread('../imagenes/tuercas_tornillos3.bmp', 0)

#Binarizo lla imagen
img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)[1]

#Identifico los objetos en la imagen
num_labels, labels,stats,centroids = cv2.connectedComponentsWithStats(img_bin)
show_num_etiquetas(img_bin)

#Creo un array por cada caraterística que vaya a medir
#Cada array inicialmente está relleno de ceros y con 
#tamaño igual a la cantidad de objetos detectados en la imagen
perim=np.zeros((num_labels,1),np.float32)
circularidad=np.zeros((num_labels,1),np.float32)
perim=np.zeros((num_labels,1),np.float32)
hull_area=np.zeros((num_labels,1),np.float32)
aspect_ratio=np.zeros((num_labels,1),np.float32)
Centros_gravedad_x=np.zeros((num_labels,1),np.float32)
Centros_gravedad_y=np.zeros((num_labels,1),np.float32)

for etiq in range(1,num_labels):
    img_aux = np.zeros_like(labels, np.uint8)
    img_aux[labels == etiq] = 1
    cnt, _ = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    """
    #Para ver los objetos seleccionados
    imgcontoursRGB=cv2.cvtColor(img_aux,cv2.COLOR_GRAY2RGB)
    imgcontoursRGB=cv2.drawContours(imgcontoursRGB,cnt, -1, (255,0,0),5)
    cv2.imshow(' ',imgcontoursRGB)
    cv2.waitKey(0)
    """
    
    for i in range(len(cnt)):
        
        #circularidad
        a = cv2.contourArea(cnt[i])
        p= cv2.arcLength(cnt[i], True)  # true porque cont es cerrado
        if p!=0:
            circularidad[etiq][0]= (4.0*np.pi*a)/(p*p)
        
        #Area
        hull = cv2.convexHull(cnt[i])
        hull_area[etiq][0] = cv2.contourArea(hull)
        perim[etiq][0] = cv2.arcLength(cnt[i], True)  # true porque cont es cerrado
        
        #Aspecto
        x, y, w, h = cv2.boundingRect(cnt[i])
        aspect_ratio[etiq][0]=w/h
        
        #Calculo el centro de gravedad a traves de los momentos
        
        momentos = cv2.moments(cnt[i])
        cx = int(momentos['m10']/momentos['m00'])
        cy = int(momentos['m01']/momentos['m00'])
        Centros_gravedad_x[etiq][0]=cx
        Centros_gravedad_y[etiq][0]=cy
        
        
        
        
#Lo coloco en dos columnas quitando el primer elemento
Z = np.hstack((perim[1:,:],hull_area[1:,:]))
z= np.hstack((circularidad[1:,:],aspect_ratio[1:,:]))
Z= np.concatenate((Z,z),axis=1)


#Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1)
_,clases,center=cv2.kmeans(Z,3,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)




img_color = cv2.merge([img_bin, img_bin, img_bin])
print('el primer grupo está formado por los objetos:')
for i in range (len(Z)):
    
    if clases[i]==0:
        print(i+1) #sumo 1 a los índices pues he quitado el 0 (fondo)
        cx=int(Centros_gravedad_x[i+1])
        cy=int(Centros_gravedad_y[i+1])
        cv2.circle(img_color,(cx, cy), 5, (0,0,255), -1)

    
print('el segundo grupo está formado por los objetos:')
for i in range (len(Z)):
    if clases[i]==1:
        print(i+1) #sumo 1 a los índices pues he quitado el 0 (fondo)
        cx=int(Centros_gravedad_x[i+1])
        cy=int(Centros_gravedad_y[i+1])
        cv2.circle(img_color,(cx, cy), 5, (0,255,0), -1)
        
print('el tercer grupo está formado por los objetos:')
for i in range (len(Z)):
    if clases[i]==2:
        print(i+1) #sumo 1 a los índices pues he quitado el 0 (fondo)
        cx=int(Centros_gravedad_x[i+1])
        cy=int(Centros_gravedad_y[i+1])
        cv2.circle(img_color,(cx, cy), 5, (255,0,0), -1)
        


plt.imshow(img_color)
plt.axis('off')
plt.title("Imagen")
plt.show()



