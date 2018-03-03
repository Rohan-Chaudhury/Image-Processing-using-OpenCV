import numpy as np
import cv2
img=cv2.imread('book.jpg')
retval,threshold= cv2.threshold(img,100,255,cv2.THRESH_BINARY)


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


retval2,threshold2= cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
gauss=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,50)
retval3,otsu=cv2.threshold(gray,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('ori',img)
cv2.imshow('thre',threshold)
cv2.imshow('thre2',threshold2)
cv2.imshow('gauss',gauss)
cv2.imshow('otsu',otsu)



cv2.waitKey(0)
cv2.destroyAllWindows()
