import cv2
import numpy as np
from matplotlib import pyplot as plt
#import image
image = cv2.imread('input.png')
#cv2.imshow('orig',image)
#cv2.waitKey(0)
image=image[678:2733,166:2469]
#grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',gray)
#cv2.waitKey(0)

#binary
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('second',thresh)
#cv2.waitKey(0)

#dilation
kernel = np.ones((5,200), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
#cv2.imshow('dilated',img_dilation)
#cv2.waitKey(0)

#find contours
im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
height_add=0
prevx=0
cnt=0

maxspc = 240
prevy=0
for aa in ctrs:
    x, y, w, h = cv2.boundingRect(aa)
    print(x," ",y," ",w," ",h)
    height_add += h
    #prevx = x
    cnt += 1
print("size:",height_add/cnt)
for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)
    # Getting ROI
    roi = image[y:y+h, x:x+w]

    # show ROI
    #cv2.imshow('segment no:'+str(i),roi)
    cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),8)
    #cv2.waitKey(0)

#print(spc_add/cnt)
#cv2.imshow('marked areas',image)
#cv2.waitKey(0)

titles = ['gray','thresholdbinary','dialated','final']
images = [gray, thresh, img_dilation, image]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()