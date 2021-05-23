# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:02:35 2021
TEMPLATE MATCHING
https://www.geeksforgeeks.org/template-matching-using-opencv-in-python/
@author: eusebio
"""

# Python program to illustrate 
# template matching
import cv2
import numpy as np
  
# Read the main image
img_gray = cv2.imread('../imagenes/dibujosanimados.png',0)
  
  
# Read the template
template = cv2.imread('../imagenes/template.png',0)
  
# Store width and height of template in w and h
w, h = template.shape[::-1]
  
# Perform match operations.
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
  
# Specify a threshold
threshold = 0.9
  
# Store the coordinates of matched area in a numpy array
loc = np.where( res >= threshold) 
  
img_rgb=cv2.merge([img_gray,img_gray,img_gray])
# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
  
# Show the final image with the matched area.
cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()