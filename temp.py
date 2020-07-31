import cv2
import numpy
import matplotlib


imagen = cv2.imread("image/carro.jpg")

#cv2.imshow("Ventana De imagen", imagen)

imagen = cv2.imread("image/carro.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow("Imagen Grises", imagen)

cv2.imwrite("Carro_grises.png", imagen)


cv2.waitKey(0)
   
