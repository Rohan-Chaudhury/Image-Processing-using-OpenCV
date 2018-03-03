import numpy as np
import cv2

img= cv2.imread('b.jpg')

row,col,ch= img.shape
mean = 0
var = 2
sigma = var**2
noise = np.random.normal(mean,sigma,(row,col,ch))
noise = noise.reshape(row,col,ch)
noisy = img + noise
cv2.imwrite('noisy2.jpg',noisy)

a=cv2.imread('noisy2.jpg')



result = cv2.fastNlMeansDenoisingColored(a,None,10,10,7,21)



cv2.imshow('img',img)
cv2.imshow('noise',noise)
cv2.imshow('noisy',noisy)
cv2.imshow('result',result)


cv2.waitKey(0)
cv2.destroyAllWindows()
