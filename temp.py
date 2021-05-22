
import cv2
import numpy as np
from matplotlib import pyplot as plt

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ordenar_puntos(puntos):
    n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()
    y_order = sorted(n_puntos, key=lambda n_puntos: n_puntos[1])
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key=lambda x1_order: x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])
    
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

#------------------------------------------------------------------------------------------------


#importamos la imagen
image = cv2.imread('../imagenes/hoja-papel-sobre-mesa-madera_93675-13089.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Obtenemos los contornos en la imagen umbral=10 y 150 tras experimentar un poco
canny = cv2.Canny(gray, 250, 255)
img_filtrada = cv2.medianBlur(canny,15)
#Hacemos una dilate para unir ciertas areas que no lo estuvieran 
#canny = cv2.dilate(canny, None, iterations=1)

#Detectamos los contornos externos de los objetos->RETR_EXTERNAL
contours = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnt=contours[0]
imgcontoursRGB=cv2.cvtColor(canny,cv2.COLOR_GRAY2RGB)
imgcontoursRGB=cv2.drawContours(imgcontoursRGB,cnt, -1, (255,0,0),5)
cv2.imshow(' ',imgcontoursRGB)
cv2.waitKey(0)

#Ordenamos los contornos y ponemos el primero como el más grande y el último como el más pequeño
cnt = sorted(cnt, key=cv2.contourArea, reverse=True)[:1]

for i in cnt:
    epsilon = 0.01*cv2.arcLength(i,True)
    approx = cv2.approxPolyDP(i,epsilon,True)
    
    
    
"""    
    if len(approx)==4:
        cv2.drawContours(image, [approx], 0, (0,255,255),2)
        
        puntos = ordenar_puntos(approx)
        cv2.circle(image, tuple(puntos[0]), 7, (255,0,0), 2)
        cv2.circle(image, tuple(puntos[1]), 7, (0,255,0), 2)
        cv2.circle(image, tuple(puntos[2]), 7, (0,0,255), 2)
        cv2.circle(image, tuple(puntos[3]), 7, (255,255,0), 2)
        
        pts1 = np.float32(puntos)
        pts2 = np.float32([[0,0],[270,0],[0,310],[270,310]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(gray,M,(270,310))
        
        plt.imshow(dst,'gray')
        print('paso ')
        texto = pytesseract.image_to_string(dst, lang='spa')
        print('texto: ', texto)
"""      
