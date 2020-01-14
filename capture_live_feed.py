import cv2 

cap = cv2.VideoCapture("rtsp://admin:adminadmin1@192.168.1.250:554/cam/realmonitor?channel=1&subtype=0")
ret = True
while(ret):
    ret,frame = cap.read()
    # cv2.moveWindow("Parque Space", 500, 400)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()   
cv2.DestroyAllWindows()