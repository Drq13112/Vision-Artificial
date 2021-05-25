# -*- coding: utf-8 -*-
"""
Created on Sat May 22 22:35:03 2021

@author: david

Detector de esquinas de Harris
"""

import cv2
import	numpy	as	np
img  =	cv2.imread('../Imagenes/sierra4.jpg')
img2  =	cv2.imread('../Imagenes/ajedrez.jpg')
img3  =	cv2.imread('../Imagenes/parking.jpg')

def generate_corners(img):
    img = cv2.medianBlur(img, 9)
    gray =	cv2.cvtColor(img,	cv2.COLOR_BGR2GRAY)
    gray =	np.float32(gray)
    
    """
    Blocksize->It is the size of neighbourhood considered for the corner detectionr
    Blocksize=2
    Ksize->Aperuture parameter for the Sobel operator
    Ksize=3
    K->Harris detector free parameter in the equation
    K=0.04
    """
    dst  =	cv2.cornerHarris(gray,	4,	9,	0.05)
    img[dst>0.01 *	dst.max()]   =	[0,	0,	255]
    cv2.imshow("HarrisCorner Detection",img)
    cv2.waitKey()
 
    
generate_corners(img)
generate_corners(img2)
generate_corners(img3)
cv2.destroyAllWindows()