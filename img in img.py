import cv2
import numpy as np
from matplotlib import pyplot as plt
#import image
import cv2
image = cv2.imread('input1 (2).png')
#cv2.imshow('orig',image)
#cv2.waitKey(0)
line=[]
word=[]
image=image[678:2733,166:2469]
#grayscale
finimg=image
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

for i, ctr in enumerate(ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)
    print(x, " ", y, " ", w, " ", h)
    # show ROI
    roi = image[y:y + h, x:x + w]
    cv2.imshow('segment no:' + str(i), roi)

    cv2.waitKey(0)
    # Getting ROI
    grayroi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    ret, threshroi = cv2.threshold(grayroi, 127, 255, cv2.THRESH_BINARY_INV)
    kernelroi = np.ones((5, 15), np.uint8)
    img_dilationroi = cv2.dilate(threshroi, kernelroi, iterations=1)
    # cv2.imshow('dilated',img_dilation)
    # cv2.waitKey(0)
    #cv2.imshow('DILATED no:' + str(i), img_dilationroi)
    #cv2.waitKey(0)
    # find contours
    sumwroi=0
    im2roi, ctrsroi, hierroi = cv2.findContours(img_dilationroi.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for iroi, ctrroi in enumerate(ctrsroi):
        # Get bounding box
        xroi, yroi, wroi, hroi = cv2.boundingRect(ctrroi)
        # Getting ROI
        roiroi = roi[yroi:yroi + hroi, xroi:xroi + wroi]
        print("inner ",xroi, " ", yroi, " ", wroi, " ", hroi)
        cv2.imshow('innersegment no:' + str(iroi), roiroi)
        cv2.rectangle(finimg, (x+xroi, y+yroi), (x+xroi + wroi, y+yroi + hroi), (0 , 255, 0), 8)
        cv2.waitKey(0)
        sumwroi=sumwroi+wroi
    cv2.rectangle(finimg, (x, y), (x + w, y + h), (90, 0, 255), 8)
    freespace=w-sumwroi
    print("freespace for seg "+str(i),freespace )

#print(spc_add/cnt)
#cv2.imshow('marked areas',image)
#cv2.waitKey(0)

titles = ['gray','thresholdbinary','dialated','final']
images = [gray, thresh, img_dilation, finimg]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()