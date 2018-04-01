import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('abcdre.jpg')
print(image.shape)

image=cv2.resize(image,(595,842))
cv2.imshow('orig',image)
cv2.waitKey(0)
cv2.imwrite('abcresized.jpg',image)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',gray)
#cv2.waitKey(0)

#binary
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('second',thresh)
#cv2.waitKey(0)

#dilation
kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
cv2.imshow('dilated',img_dilation)
cv2.waitKey(0)
im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
print(ctrs)
print(sorted_ctrs)