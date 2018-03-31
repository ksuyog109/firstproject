import cv2
import numpy as np
from matplotlib import pyplot as plt
#import image
image = cv2.imread('input1 (4).png')
#cv2.imshow('orig',image)
#cv2.waitKey(0)
line=[]
word=[]

image=image[678:2733,166:2469]
#grayscale
shapex,shapey,dntknw=image.shape
#print(shapey)
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
xyleft=[]
xyright=[]
slopeleft=[]
sloperight=[]
marginleft=[]
marginright=[]
freespace=[]
flag = 1
for i, ctr in enumerate(ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)
    #print(x, " ", y, " ", w, " ", h)
    # show ROI
    roi = image[y:y + h, x:x + w]
    #######################################cv2.imshow('segment no:' + str(i), roi)

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
    #print("ctrs",ctrsroi)
    wordsbyline = []
    #Matrix = [[0 for x in range(w)] for y in range(h)]
    for iroi, ctrroi in enumerate(ctrsroi):
        # Get bounding box

        xroi, yroi, wroi, hroi = cv2.boundingRect(ctrroi)
        # Getting ROI
        roiroi = roi[yroi:yroi + hroi, xroi:xroi + wroi]
        #print("inner ",xroi, " ", yroi, " ", wroi, " ", hroi)
        #print("xaxis,yaxis",xroi,"+",x,"=",xroi+x,yroi,"+",y,"=",yroi+y)
        #vect=np.array([xroi,yroi,wroi,hroi])
        vect=[xroi+x,yroi+y,wroi,hroi]
        flag = 0
        if wroi>35:
            if hroi>35:
                flag=1
                #print("flag1")
                wordsbyline.append(vect)
        #print("vect", vect)

        #print("wordbylent", wordsbyline)
        ##########################################cv2.imshow('innersegment no:' + str(iroi), roiroi)
        roiroigray=cv2.cvtColor(roiroi, cv2.COLOR_BGR2GRAY)
        slantroi=255-roiroigray
        #print(roiroi)
        img_row_sum=np.sum(slantroi,axis=0).tolist()

        plt.subplot(2,1,1),plt.plot(img_row_sum)
        plt.subplot(2, 1, 2), plt.imshow(roiroigray)
        plt.show()
        cv2.rectangle(finimg, (x+xroi, y+yroi), (x+xroi + wroi, y+yroi + hroi), (0 , 255, 0), 8)

        cv2.waitKey(0)
        sumwroi=sumwroi+wroi

    #print("npt", wordsbyline)

    wordsbyline=sorted(wordsbyline,key=lambda x:x[0])

    nparray = np.matrix(wordsbyline)
    #print("nptsort", wordsbyline)
    if len(wordsbyline)!=0:
        xyleft.append(wordsbyline[0])
        xyright.append(wordsbyline[-1])
        totlenline = wordsbyline[-1][0] + wordsbyline[-1][3] - wordsbyline[0][0]
        ocupiedspace=0
        for itr in range(0,len(wordsbyline)):
            ocupiedspace=ocupiedspace+wordsbyline[itr][3]
        freespace.append(totlenline-ocupiedspace)
        #print("freespace",freespace)
    xyleft=sorted(xyleft,key=lambda x:x[1])
    xyright=sorted(xyright,key=lambda x:x[1])


    cv2.rectangle(finimg, (x, y), (x + w, y + h), (90, 0, 255), 8)
    #freespace=w-sumwroi
    #print("freespace for seg "+str(i),freespace )

for itr in range(0,len(xyleft)):
    marginleft.append(xyleft[itr][0])
    marginright.append(shapey-xyright[itr][0])

#print(spc_add/cnt)
#cv2.imshow('marked areas',image)
#cv2.waitKey(0)
avgfreespace=sum(freespace) / float(len(freespace))
avgmarleft=sum(marginleft) / float(len(marginleft))
avgmarright=sum(marginright) / float(len(marginright))
print("totalfreespacebyline",freespace)
print("avgfree",avgfreespace)
print("avgwidthleft",avgmarleft)
print("avgwidthright",avgmarright)
for itr in range(0, len(xyleft)-1):
    yl1=xyleft[itr][1]
    yl2=xyleft[itr+1][1]
    xl1 = xyleft[itr][0]
    xl2 = xyleft[itr + 1][0]
    yr1 = xyright[itr][1]
    yr2 = xyright[itr + 1][1]
    xr1 = xyright[itr][0]
    xr2 = xyright[itr + 1][0]
    if(xl2-xl1==0):
        #slopeleft.append(999999999)
        print("skip")
    else:
        slopeleft.append((yl2-yl1)/(xl2-xl1))
    if (xl2 - xl1 == 0):
        print("skip")
        #sloperight.append(99999999)
    else:
        sloperight.append((yr2 - yr1) / (xr2 - xr1))
#print("slopeleft",slopeleft)
#print("sloperight",sloperight)
avgslopeleft=sum(slopeleft) / float(len(slopeleft))
avgsloperight=sum(sloperight) / float(len(sloperight))
print("avgslopeleft",avgslopeleft)
print("avgsloperight",avgsloperight)
titles = ['gray','thresholdbinary','dialated','final']
images = [gray, thresh, img_dilation, finimg]
cv2.imwrite("aa.png",finimg)
cv2.imshow('orig',finimg)
cv2.waitKey(0)
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

#plt.show()