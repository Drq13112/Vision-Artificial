
import cv2
import numpy as np
from numpy.linalg import inv 
import matplotlib.pyplot as plt

img=cv2.imread('../Imagenes/Estanteria.bmp',0)

#Función que realiza la transforma directa
def OperacionDirecta(Sx,Sy,img):
    
    M=np.array([[Sx,0,0],[0,Sy,0],[0,0,1]])
   
    fil,col=img.shape
    
    img_resultado=img*0
    
    for y in range(fil):
        
        for x in range(col):
            
            matrix=np.float32([[x],[y],[1]])
            
            xT,yT,z=M@matrix
            
            if yT<fil and xT<col:
                
                img_resultado[int(yT)][int(xT)]=img[y][x]
                
            else :
                img_resultado[fil-1][col-1]=img[y][x]                
    return img_resultado
   
    
#Función que realiza la función inversa
def OperacionInversa(Sx,Sy,img):
    
    fil,col=img.shape
    img_resultado=img*0
    M=np.float32([[Sx,0,0],[0,Sy,0],[0,0,1]])   
    M_inv=inv(M)
    for xT in range(col):
        for yT in range(fil):
            
            matrix= np.array([[xT],[yT],[1]])
            x,y,z=M_inv@matrix
            
            if y<fil and x<col:
                
                img_resultado[yT][xT]=img[int(y)][int(x)]
            
            else:
                img_resultado[yT][xT]=img[fil-1][col-1]
                
    return img_resultado
                

#Ejecuto las dos operaciones
Img_Directa=OperacionDirecta(0.8,0.8,img)
plt.show()
Img_Inversa=OperacionInversa(0.8,0.8,img)

#Imprimo por pantalla los resultados
plt.subplot(1,2,1),plt.imshow(Img_Directa,'gray')
plt.title('Imagen en directa')   
plt.axis(False)
plt.subplot(1,2,2),plt.imshow(Img_Inversa,'gray')
plt.title('Imagen en inversa')   
plt.axis(False)
            
    





