# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:14:52 2021

@author: david
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../../imagenes/a380.jpg',0 )
img1=cv2.imread('../../imagenes/cojinetes.bmp',0)
img2=cv2.imread('../../imagenes/llavefija1.bmp',0)
img3=cv2.imread('../../imagenes/perritos.jpg',0)

#Uso una función que permite calcular directamente a binarización de Otsu
#La propia función calcula el valor del umbral por ella misma
otsu_threshold, img_bin = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("Umbral de binarizacion Otsu: ", otsu_threshold)
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])

#Visualizacion original
plt.subplot(1, 3, 1)
plt.imshow(img1, cmap='gray')
plt.title('Original',fontsize=25)
plt.axis(False)
#Visualizacion binaria
plt.subplot(1, 3, 2)
plt.imshow(img_bin, cmap='gray')
plt.title(f'Binaria con umbral {otsu_threshold}',fontsize=25)
plt.axis(False)
plt.subplot(1, 3, 3)
plt.plot(hist1)
plt.title(f'Binaria con umbral {otsu_threshold}',fontsize=25)

cv2.destroyAllWindows()
