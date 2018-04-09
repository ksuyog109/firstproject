import cv2
import numpy as np
#import image
image = cv2.imread('input1 (1).png')
#print(image.shape[0])
image=image[1000:3542,1000:2479]
#cv2.imshow('orig',image)
#cv2.waitKey(0)
#a=np.array(1,2,3,4)
#print(image[1][1][1])
#grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
cv2.waitKey(0)

#binary
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('second',thresh)
cv2.waitKey(0)

#dilation
kernel = np.ones((5,20), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
cv2.imshow('dilated',img_dilation)
cv2.waitKey(0)

#find contours
im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
pix=[]
for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)

    # Getting ROI
    roi = image[y:y+h, x:x+w]

    # show ROI

    cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)

    roibin = thresh[y:y + h, x:x + w]
    roigray = gray[y:y + h, x:x + w]
    dimroi = roibin.shape
    #cv2.imshow('segment no:'+str(i),roi)
    #cv2.waitKey(0)



    #print(roi)
    #code for pressure
    #print(i,roibin.shape)
    dimroi=roibin.shape
    #print(dimroi[1])
    if(dimroi[0]>25 and dimroi[1]>30 ):
        #print(roibin.shape)

        for row in range(dimroi[0]):
            #print("row",row)
            for col in range(dimroi[1]):
                #print("col", col)
                #print(row,col)

                if(roibin[row,col]==255):
                    #print(roigray[row,col])
                    pix.append(roigray[row,col])
                a=1
            #print(row)
            #print("\n\n")
        #print("pix len",len(pix))








pixnp=np.array(pix)
print(np.std(pixnp))
cv2.imshow('marked areas',image)
cv2.waitKey(0)