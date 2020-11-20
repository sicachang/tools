import cv2
import threading
import dlib
import imutils
import datetime
from imutils import face_utils
import time
import pandas as pd


print('run program')
rtmp_str = 'rtmp://sicachang.ddns.net/live/test'  # 

cap = cv2.VideoCapture(rtmp_str)

fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)
print(size)

num= 0
while(1):
    if num%1==0:
        ret, image = cap.read()
        try:
            frame = imutils.resize(image, width=800)
            #frame= image*
            datetime_dt = datetime.datetime.today() # 獲得當地時間
            time_delta = datetime.timedelta(hours=12) #時差
            new_dt = datetime_dt + time_delta #本地時間加3小時
            datetime_format = new_dt.strftime("%S")  # 格式化日期
            text= str(datetime_format)
            cv2.putText(frame, text, (150, 190), cv2.FONT_HERSHEY_PLAIN,2, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow("Frame", frame)
            fps = cap.get(cv2.CAP_PROP_FPS)
            #cv2.imwrite("D:/OneDrive - iii.org.tw/NGINX/html/capture1.jpg", frame)
            #cv2.waitKey(int(100 / int(fps)))  # 延迟
            cv2.waitKey(1)
        except:
            cap = cv2.VideoCapture(rtmp_str)

            fps = cap.get(cv2.CAP_PROP_FPS)
            print(fps)
        
    num= num+ 1
    
