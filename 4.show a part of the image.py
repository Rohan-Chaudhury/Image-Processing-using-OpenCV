import numpy as np
import cv2

img=cv2.imread('b.jpg',cv2.IMREAD_COLOR)

img[55,55]=[255,255,255]
px=img[55,55]
print(px)

roi=img[100:150,100:150]=[255,255,255]

print(roi)
#cv2.imshow('roi',roi)

fafa=img[55:105,100:150]
img[0:50,0:50]=fafa


cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()






















































