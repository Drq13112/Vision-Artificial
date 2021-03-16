# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:45:12 2021

@author: david
"""

import cv2

#umbral1=umbral2
img=cv2.imread("../imagenes/llave.jpg",0)
edgesSobel=cv2.Canny(img,100,100)

