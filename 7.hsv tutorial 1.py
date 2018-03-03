import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
    _, frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hue saturation value


    lower_red=np.array([160,100,100])
    upper_red=np.array([179,255,255])

    lower_red2=np.array([0,100,100])
    upper_red2=np.array([10,255,255])

    #dark_red=np.uint8([[[12,22,121]]])
    #dark_red=cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv, lower_red, upper_red)
    mask2=cv2.inRange(hsv, lower_red2, upper_red2)
    
    rest= cv2.bitwise_and(frame,frame,mask=mask)
    rest2= cv2.bitwise_and(frame,frame,mask=mask2)
                         #applied to the frame #input 1 #input 2
    add=cv2.add(rest,rest2)
    cv2.imshow('add',add)
    cv2.imshow('rest',rest)
    cv2.imshow('rest2',rest2)
    cv2.imshow('mask',mask)
    cv2.imshow('frame',frame)

    
    k= cv2.waitKey(1) & 0xFF
    if k==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
