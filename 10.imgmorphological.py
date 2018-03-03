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
    
    kernel=np.ones((5,5),np.uint8)
    erosion= cv2.erode(mask,kernel,iterations=1)
    dilation= cv2.dilate(mask,kernel,iterations=1)

    opening=cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing=cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    #top hat gives the diff bet input image and opening of the image and blackhat gives the diff bet closing of the input image and input image
    #cv2.imshow('Tophat',tophat)
    #cv2.imshoe('blackhat',blackhat)
    

    
    cv2.imshow('rest',rest)

    cv2.imshow('frame',frame)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('closing',closing)
    cv2.imshow('opening',opening)
    
    k= cv2.waitKey(1) & 0xFF
    if k==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
