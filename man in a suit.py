import numpy as np
import cv2

img= cv2.imread('ca.jpg')
rest=img



bilateral=cv2.bilateralFilter(rest,6,40,200)

    

    
cv2.imshow('rest',rest)




cv2.imshow('bilateral',bilateral)

cv2.imwrite('ca2.jpg',bilateral)








cv2.waitKey(0)
cv2.destroyAllWindows()
