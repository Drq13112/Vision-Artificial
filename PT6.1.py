# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:13:13 2021

@author: david
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Importo la imagen
img_bin=cv2.imread('../imagenes/calculadora.png')

#
num_labels, img_labels, stats, cg = cv2.connectedComponentsWithStats(img_bin)

#
(x,y),(MA,ma),angle = cv2.fitEllipse()
contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img_holes, contours, i, 255, cv2.FILLED)
