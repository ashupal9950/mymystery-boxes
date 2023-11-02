import cv2 

cam = cv2.VideoCapture(0)

while True:
    ign, frame= cam.read()
    cv2.imshow("window", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break 
