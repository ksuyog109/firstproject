import cv2
import numpy as np
from matplotlib import pyplot as plt
imgname='vihangcap.jpg'
imginput = cv2.imread(imgname)
imginput=cv2.resize(imginput,(595,842))
imgproc = cv2.imread(imgname)
imgproc=cv2.resize(imgproc,(595,842))


image=imginput
print(image.shape)


ori=image
finimg=image
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
kernel = np.ones((8,100), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
cv2.imshow('dilated',img_dilation)
cv2.waitKey(0)
im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
#print(ctrs)
#print(sorted_ctrs)
'''
for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)
    # Getting ROI
    roi = image[y:y+h, x:x+w]

    # show ROI
    cv2.imshow('segment no:'+str(i),roi)
    cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),1)
    cv2.waitKey(0)
titles = ['gray','final']
images = [gray,  image]
'''
words=[]
for i, ctr in enumerate(ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)
    #print(x, " ", y, " ", w, " ", h)
    # show ROI
    roi = imgproc[y:y + h, x:x + w]
    #cv2.imshow('segment no:' + str(i), roi)

    #cv2.waitKey(0)
    # Getting ROI
    grayroi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    ret, threshroi = cv2.threshold(grayroi, 127, 255, cv2.THRESH_BINARY_INV)
    kernelroi = np.ones((10, 5), np.uint8)
    img_dilationroi = cv2.dilate(threshroi, kernelroi, iterations=1)
    cv2.imshow('dilated',img_dilationroi)
    cv2.waitKey(0)
    #cv2.imshow('DILATED no:' + str(i), img_dilationroi)
    #cv2.waitKey(0)
    # find contours
    sumwroi=0
    wordsbyline = []

    im2roi, ctrsroi, hierroi = cv2.findContours(img_dilationroi.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for iroi, ctrroi in enumerate(ctrsroi):
        # Get bounding box
        xroi, yroi, wroi, hroi = cv2.boundingRect(ctrroi)
        # Getting ROI
        roiroi = roi[yroi:yroi + hroi, xroi:xroi + wroi]
        if hroi > 2 and wroi > 2:
            vect = [xroi + x, yroi + y, wroi, hroi]
            wordsbyline.append(vect)

        #print("inner ",xroi, " ", yroi, " ", wroi, " ", hroi)
        #cv2.imshow('innersegment no:' + str(iroi), roiroi)
            cv2.rectangle(finimg, (x+xroi, y+yroi), (x+xroi + wroi, y+yroi + hroi), (0 , 255, 0), 2)
        #cv2.waitKey(0)
        sumwroi=sumwroi+wroi

    wordsbyline = sorted(wordsbyline, key=lambda x: x[0])
    words.append(wordsbyline)
    nparray = np.matrix(wordsbyline)
    #print(nparray)
    print("nparr :", nparray.shape)
    #for i,alpha in enumerate(nparray):
        #print(alpha.item((0,0)) )
        #letter=image[alpha.item((0,1)):alpha.item((0,1))+alpha.item((0,3)),alpha.item((0,0)):alpha.item((0,0))+alpha.item((0,2))]
        #cv2.imshow('letter',letter)
        #cv2.waitKey(0)
    cv2.rectangle(finimg, (x, y), (x + w, y + h), (90, 0, 255), 2)
    freespace=w-sumwroi
    #print("freespace for seg "+str(i),freespace )

#print(spc_add/cnt)
#cv2.imshow('marked areas',image)
#cv2.waitKey(0)

titles = ['gray','final']
images = [gray,  finimg]
print("words : ",words)
words.reverse()
imgfordisplay = cv2.imread(imgname,0)
ret, imgfdthresh = cv2.threshold(imgfordisplay, 127, 255, cv2.THRESH_BINARY_INV)
print("imgford",imgfdthresh )
imgfordisplay=cv2.resize(imgfdthresh,(595,842))
lettercount=1
for cnt,word in enumerate(words):
    print(cnt,word)
    for i,alpha in enumerate(word):
        #print(alpha )
        letter=imgfordisplay[alpha[1]:alpha[1]+alpha[3],alpha[0]:alpha[0]+alpha[2]]
        cv2.imshow('letter',letter)
        cv2.waitKey(0)
        cv2.imwrite('letter_'+str(lettercount)+'.jpg',letter)
        lettercount=lettercount+1

sumI=0
sumCap=0
for i in range(1,11):
    letterlnt=cv2.imread("letter_"+str(i)+".jpg",0 )
    row,col=letterlnt.shape
    sumI += row
    sumCap += row

for i in range(11,15):
    letterlnt=cv2.imread("letter_"+str(i)+".jpg",0 )
    row,col=letterlnt.shape
    sumCap += row

sizeI=sumI/10
print("I SIZE",sizeI)
sizeCap=sumCap/15
print("Cap SIZE",sizeCap)


'''
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()'''