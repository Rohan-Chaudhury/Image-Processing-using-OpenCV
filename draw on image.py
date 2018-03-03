import numpy as np
import cv2
img=cv2.imread('b.jpg',cv2.IMREAD_COLOR)

cv2.line(img, (0,0) ,(150,150),(255,255,255),15)

cv2.rectangle(img , (14,35) ,(166,133) ,(0,255,0) ,5)

cv2.circle(img , (100,100),56 ,(0,0,255), -2)
               #  center  radius  color  fill it up
 
pts= np.array([[23,32],[24,54],[34,35],[54,6],[34,34],[13,13],[56,78],[87,98]],np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img ,[pts],True,(0,255,255),3)
#                        true to join first and last point
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'referfefwefwer',(0,130),font,1,(23,234,323),2,cv2.LINE_AA)
#                                                             thickness                                                              

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
