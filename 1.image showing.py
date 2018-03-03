import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('b.jpg',cv2.IMREAD_GRAYSCALE)#number for grayscale -0 instead of imread_grayscale you can just write 0
#IMREAD_COLOR -1
#IMREAD_UNCHANGED - (-1)

cv2.imshow('abd',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()

cv2.imwrite('c.png',img)
