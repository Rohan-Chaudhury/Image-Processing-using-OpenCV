import numpy as np
import cv2

img= cv2.imread('ba.jpg')
rest=img


result = cv2.fastNlMeansDenoisingColored(img,None,4,4,7,21)





    
cv2.imshow('original',rest)

cv2.imwrite('ba4.jpg',result)

c=cv2.imread('ba2.jpg')



cv2.imshow('result',result)








cv2.waitKey(0)
cv2.destroyAllWindows()
