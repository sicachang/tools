import cv2
 
capture = cv2.VideoCapture(0)
 
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
videoWriter = cv2.VideoWriter('./video.avi', fourcc, 30.0, (640,480))
 
while (True):
 
    ret, frame = capture.read()
    #frame= cv2.rectangle(frame, (50, 80), (600, 400),  (255, 255, 200), 2)
     
    if ret:
        cv2.imshow('video', frame)
        videoWriter.write(frame)
 
    if cv2.waitKey(1) == 27:
        break
 
capture.release()
videoWriter.release()
 
cv2.destroyAllWindows()