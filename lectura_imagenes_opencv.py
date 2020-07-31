import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = ("imagenes/ruby.png")
ph = cv2.imread(imagen)
 
imagencor = cv2.cvtColor(ph, cv2.COLOR_RGB2BGR)

imagengrises = cv2.cvtColor(imagencor, cv2.COLOR_RGB2GRAY)
cv2.imshow('Imagen',imagengrises)
cv2.imshow('Imgane 2', imagencor)
cv2.imshow('imagen 3', ph)
cv2.waitKey(0)


   
