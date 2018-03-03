import cv2
import numpy as np


img1= cv2.imread('ba.jpg')
img2= cv2.imread('ba2.jpg')



difference = cv2.subtract(img1,img2)

result= not np.any(difference)


cv2.imshow('difference',difference)
