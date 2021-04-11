import cv2
import numpy as np
from matplotlib import pyplot as plt

#Esta función la he copiado del codigo de ayuda
def show_num_etiquetas(img_bin):
    num_labels, img_labels, stats, centroids = cv2.connectedComponentsWithStats(
        img_bin)

    font = cv2.FONT_HERSHEY_SIMPLEX
    img_color = cv2.merge([img_bin, img_bin, img_bin])
    for i in range(1, num_labels): 
        # quito el 0 porque es el fondo
        #quitar comentario si se quiere visualizar bounding boxes
        # cv2.rectangle(img_color, (stats[i][0], stats[i][1]), (
        #     stats[i][0]+stats[i][2], stats[i][1]+stats[i][3]), (0, 255, 0))
        cg = (int(centroids[i][0]), int(centroids[i][1]))
        cv2.circle(img_color, cg, 3, (255, 0, 0), -1)
        cv2.putText(img_color, str(i), cg, font,
                    1, (255, 0, 0), 2, cv2.LINE_AA)
    plt.imshow(img_color)
    plt.axis('off')
    plt.title("Imagen")
    plt.show()
    
#--------------------------------------------------------------------------

img=cv2.imread('../imagenes/cuadradas-redondas.jpg',0)

#Filtro de Gauss para suavizar
img=cv2.GaussianBlur(img,(5,5),0)

#Filtro de Otsu para binarizar
img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#Defino el kernel y hago una apertura y un cierre a la imagen
kernel3 = np.ones((9, 9), np.uint8)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel3,iterations=3)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel3)

#Obtengo la cantidad de objetos 
num_labels,labels, stats, centroids = cv2.connectedComponentsWithStats(
        img_bin)

plt.imshow(img_bin,'gray')
show_num_etiquetas(img_bin)

contours_circles = [0]*num_labels
contours_not_circles = [0]*num_labels

# Discrimino por circularididad
for i in range(1,num_labels):
    img_aux = np.zeros_like(labels, np.uint8)
    img_aux[labels == i] = 1
    
    # Obtengo los contornos
    contours, hierarchy = cv2.findContours(img_aux, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for j in contours:
        perimeter = cv2.arcLength(j, True)# pongo true por que el contorno es cerrado
        area = cv2.contourArea(j)
        if perimeter == 0:
            break
        circularity = 4*np.pi*(area/(perimeter*perimeter))
        if 0.7 < circularity:
            contours_circles.insert(i,i)
        else :
            contours_not_circles.insert(i,i)

print('el primer grupo (objetos circulares) está formado por los objetos:')
for i in range(len(contours_circles)):
    if contours_circles[i]!=0:
        print(i,' y su centroide es:',centroids[i][0],',',centroids[i][1])
                      
print('el segundo grupo (objetos NO circulares) está formado por los objetos:')
for i in range(len(contours_not_circles)):
    if contours_not_circles[i]!=0:
        print(i,' y su centroide es:',centroids[i][0],',',centroids[i][1])
        

