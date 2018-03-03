import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while True:
    _, frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hue saturation value


    lower_red=np.array([150,150,100])
    upper_red=np.array([179,255,150])


    mask=cv2.inRange(hsv, lower_red, upper_red)

    rest= cv2.bitwise_and(frame,frame,mask=mask)
    
    kernel=np.ones((15,15),np.float32)/225
    smoothed=cv2.filter2D(rest,-1,kernel)

    gblur=cv2.GaussianBlur(rest,(15,15),0)
    median=cv2.medianBlur(rest,15)
    bilateral=cv2.bilateralFilter(rest,15,75,75)

    

    
    cv2.imshow('rest',rest)

    cv2.imshow('frame',frame)
    cv2.imshow('kernel',kernel)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('gblur',gblur)
    cv2.imshow('median',median)
    cv2.imshow('bilateral',bilateral)

    
    k= cv2.waitKey(1) & 0xFF
    if k==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
