# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:05:11 2021

@author: david
"""

import cv2
import numpy as np


img_bin=cv2.imread("../imagenes/sodoku_bin.png")


def numeros_soduku(img_bin):
    
img_numeros=numeros_soduku(img_bin)
num_labels, img_labels, stats, cg = cv2.connectedComponentsWithStats(img_bin)