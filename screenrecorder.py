import cv2
import pyautogui
import numpy as np

resolution=(1680,1050)

codec=cv2.VideoWriter_fourcc(*"XVID")
filename="recording.avi"

fps=120.0

output=cv2.VideoWriter(filename,codec,fps,resolution)
cv2.namedWindow("Live",cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live",720,270)

while True:
    
    img=pyautogui.screenshot()
    
    frame=np.array(img)
    
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    output.write(frame)
    
    cv2.imshow('Live',frame)
    
    if cv2.waitKey(1) ==ord('q'):
        break

output.release()

cv2.destroyAllWindows()