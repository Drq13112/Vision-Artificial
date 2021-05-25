# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 09:45:11 2021

@author: david

Detección de circunferencias mediante transformada de Hough
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('../imagenes/pelotas.jpg',0)
output = img_color=cv2.merge([img,img,img])
# detect circles in the image
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.5, 10)
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle in yellow
		cv2.circle(output, (x, y), r, (255, 0, 0), 2)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (255, 255, 0), -1)

plt.imshow(output)
plt.axis('off')
plt.title("circulos")
plt.show()