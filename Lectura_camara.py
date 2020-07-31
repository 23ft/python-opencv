import cv2

#Prueba camara

cap = cv2.VideoCapture(0)
    #Habilitar camara o video

while True:
    OK, img = cap.read()
    
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Ventana',gris)
    
    if cv2.waitKey(1) == ord(' f'):
        break           
        
cap.release()
cv2.destroyAllWindows()    


