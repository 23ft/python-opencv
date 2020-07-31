import cv2

cap = cv2.VideoCapture(0)
#cap.set(3, 600)
#cap.set(4, 600)


while True:    
    mat, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        cap.release(q)
        break