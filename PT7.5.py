# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 13:19:04 2021

@author: david

Nivel botellas Hough

README:
Se presupone que al tratarse de una linea de botellas todas las botellas serán
igual de altas y que la camara estará situada siempre a la misma altura y a la 
misma distancia de las botellas.
Para hacer el ejercicio he hido dividiendo la imagen en mitades para filtrar 
todas las lineas que no me interesaban.
Resulta que el llenaod nunca supera la mitad inferior de todas las fotos, por
lo que resulta interesante analizar solo esa parte, de este modo eliminamos gran 
parte de las lineas que molestaban.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

#img = cv2.imread('../imagenes/Botella3.bmp',0)
#img = cv2.imread('../imagenes/Botella1.bmp',0)
#img = cv2.imread('../imagenes/Botella5.bmp',0)
#img = cv2.imread('../imagenes/Botella10.bmp',0)
#img = cv2.imread('../imagenes/Botella17.bmp',0)
img = cv2.imread('../imagenes/Botella18.bmp',0)
 
def Detecta_lineas(img,cantidad_lineas):
    
    output=cv2.merge([img,img,img])
    img=img[int(img.shape[0]/2):img.shape[0]]
    
    #Saco los contornos con Canny
    edges = cv2.Canny(img,200,250)
    
    #fijo el umbral a 0 porque sera la propia función la que encuentre el umbral idoneo
    umbral=0
    
    #La variable bandera me sirve para coger solo la primera recta que detecte.
    #Lo hago para simplificar el resultado, además las rectas que no he tenido en cuenta
    #están muy cercanas entre sí, de modo que no importa si las desprecio.
    bandera=False
    
    lines_1 = cv2.HoughLines(edges,1,np.pi/180, umbral)
    Distancia=0
    for i in range(len(lines_1)):
        
        #Auto gestion del umbral
        lines = cv2.HoughLines(edges,2,np.pi/180, umbral)
        umbral=umbral+5
            
        if  len(lines)>cantidad_lineas:    
            print(f'Se han encontrado {len(lines)} rectas')
    
        else:
            
            #Dibujo y filtrado de rectas por secciones de la imagen
            print(f'Se han encontrado {len(lines)} rectas')
            for k in range(len(lines)):
                
                for rho,theta in lines[k]:
                    fil,col=img.shape
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a*rho
                    y0 = b*rho
                    x1 = int(x0 + 1000*(-b))
                    y1 = int(y0 + 1000*(a))
                    x2 = int(x0 - 1000*(-b))
                    y2 = int(y0 - 1000*(a))
                    
                    if 0<y1<fil/2 and 0<y2<fil/2 and bandera==False:
                        bandera=True
                        cv2.line(output,(x1,int(y1+fil)),(x2,y2+int(fil)),(255,0,0),2)
                        Distancia=fil-y1
                        
            plt.imshow(output)
            plt.axis('off')
            plt.title('rectas Hough, Distancia:%i'% Distancia)
            plt.show()
            break
#Pongo que el limite de rectas son 40, para darle holgura al algoritmo,
#da igual que encuentre muchas rectas, luego las filtro y me quedo 
#solo con la que me interesa
Detecta_lineas(img,40)

