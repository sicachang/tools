import requests
import urllib.parse
import sys
import os 

# Time 
import datetime
import time
import calendar

import cv2
path= os.path.dirname(os.path.realpath(__file__))
"""
發送 Line Notify 訊息
"""
def lineNotify(token, msg, picURI):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token
    }
   
    payload = {'message': msg}
    files = {'imageFile': open(picURI, 'rb')}
    print('==異物狀態資訊傳送 (5G Hub)==')
    print('傳送時間: ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    starttime = datetime.datetime.now()

    r = requests.post(url, headers = headers, params = payload, files = files)
    endtime = datetime.datetime.now()
    print('接收時間: ', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print('上傳延遲共：', (endtime - starttime).seconds, '秒')
    
    return r.status_code
 
token = "RerG0OaGfdnjuMZLV5rUaHadViVr3cJFoftcrkNeLs3"

# 修改為你要傳送的訊息內容
data =  { 'terminal' : 'T1', 
'camera' : 'D10-02', 
'fod' : '老虎鉗', 
'classification' : '未知', 
'area': 'A1',
'time' : str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
'msg': '請FOD盡速前往清除'
} 

# 第一組圖文
msg1 = [
'\n 偵測到老虎鉗'
]
picURI = path+ "/ff1.jpg"
lineNotify(token, msg1, picURI)

# 第二組圖文
msg2 = [
'\n 請人員盡速前往處理'
]
picURI = path+ "/ff2.jpg"
lineNotify(token, msg2, picURI)