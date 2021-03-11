# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:06:50 2021

@author: usuario
"""
import matplotlib.pyplot as plt
#podemos importar las funciones individualmente
# from noiselib import add_gaussian_noise
# from noiselib import add_speckle_noise
# from noiselib import add_salt_and_pepper_noise
#podemos importar todas las funciones de golpe
#from noiselib import *
import noiselib as nl

import cv2
img = cv2.imread('../imagenes/caja06.png', 0)

# img_gauss = add_gaussian_noise(img,0,5)
# img_speck = add_speckle_noise(img)
# img_sal_p = add_salt_and_pepper_noise(img)

img_gauss = nl.add_gaussian_noise(img,0,5)
img_speck = nl.add_speckle_noise(img)
img_sal_p = nl.add_salt_and_pepper_noise(img)

plt.subplot(221),plt.imshow(img,cmap='gray'),plt.title('Img. Original'), plt.axis(False)
plt.subplot(222),plt.imshow(img_gauss,cmap='gray'),plt.title('Con ruido Gaussiano'), plt.axis(False)
plt.subplot(223),plt.imshow(img_sal_p,cmap='gray'),plt.title('Con ruido sal y pimienta'), plt.axis(False)
plt.subplot(224),plt.imshow(img_speck,cmap='gray'),plt.title('Con ruido speckle'), plt.axis(False)

plt.show()