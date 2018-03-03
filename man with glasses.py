import numpy as np
import cv2

img= cv2.imread('ba.jpg')
rest=img


result = cv2.fastNlMeansDenoisingColored(img,None,4,4,7,21)



def adjust_gamma(img, gamma):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	res = cv2.LUT(img, table)
	return res

    
res= adjust_gamma(result,1.3)

hsv=cv2.cvtColor(res, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
v +=255
h-=5
s+=30
final_hsv=cv2.merge((h,s,v))
image=cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
cv2.imshow('res',image)



    

    
cv2.imshow('original',rest)

cv2.imwrite('ba3.jpg',image)

c=cv2.imread('ba2.jpg')
cv2.imshowpair(c,image)


#cv2.imshow('result',res)








cv2.waitKey(0)
cv2.destroyAllWindows()
