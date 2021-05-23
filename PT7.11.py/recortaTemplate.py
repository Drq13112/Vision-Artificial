# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 13:24:31 2020
RECORTA ROI (region of interest) 
Permite marcar la ROI sobre la imagen con el raton
Hasta que no se pulse ESC no guarda la ROI

@author: eusebio 
"""

import cv2

drawing = False # true if mouse is pressed
ix,iy = -1,-1 #coordenadas iniciales rectangulo
fx,fy = -1,-1 #coordenadas finales rectangulo


# mouse callback function
def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,img,fx,fy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
                img = cv2.imread('../imagenes/dibujosanimados.png',0)
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
        fx,fy = x,y


img = cv2.imread('../imagenes/dibujosanimados.png',0)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rectangle)
print ("Marca la ROI con el raton")
print ("Puedes marcar varias veces")
print ("Cuando tengas la ROI correcta pulsa ESC para grabar en \'recorte.png\'")

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:#hasta pulsar ESC
        break
cv2.destroyAllWindows()
img = cv2.imread('../imagenes/dibujosanimados.png',0)
ROI=img[iy:fy, ix:fx]    #OJO: las y son las filas y las x las columnas
cv2.imwrite('../imagenes/template.png', ROI)
print ("Recorte grabado en en \'template.png\' ")

