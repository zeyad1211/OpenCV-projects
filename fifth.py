import numpy as np
import cv2 as cv

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        font = cv.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv.putText(img, strXY, (x,y), font, .5, (0, 255, 255), 1)
        cv.imshow("image", img)
    if event == cv.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]   # the reason it seems fliped is cause the image is a matrix(array) which means it takes row,column and x is colums since it's the width, and y is rows since it's the hight
        red = img[y, x, 2]
        
        font = cv.FONT_HERSHEY_SIMPLEX
        strBGR = f"{blue}, {green}, {red}"
        cv.putText(img, strBGR, (x,y), font, .5, (255, 0, 255), 1)
        cv.imshow('image', img)
        
img = cv.imread(r"C:\Users\zeyad\Pictures\Camera Roll\adha24.JPG")
#cv.namedWindow("image", cv.WINDOW_NORMAL) # nessesary if photo resolution is greater than screen resolution
img = cv.resize(img, (1280, 720))

cv.imshow('image', img)
#print(cv.setMouseCallback('image', click_event))
cv.setMouseCallback('image', click_event)
cv.waitKey(0)
cv.destroyAllWindows()
