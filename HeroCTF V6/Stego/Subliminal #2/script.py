import cv2
import numpy as np

video = cv2.VideoCapture("salida.mp4")

width, height = int(video.get(3)), int(video.get(4))

salida = np.zeros((height,width,3),np.uint8)

i = 0
j = 0
while True:
    end,frame = video.read()
    
    if not end:
        break
    
    
    y = i % (height // 20) * 20
    x = i // (height // 20) * 20
    salida[y:y+20, x:x+20] = frame[y:y+20, x:x+20]
    i += 1
    
    
cv2.imwrite("salida2.bmp",salida)
video.release()
    
