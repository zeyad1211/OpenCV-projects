import numpy as np
import cv2 as cv

img = np.zeros([512, 512, 3], np.uint8) #black image(512x512 pixels), each pixel 3x3 zeros

img = cv.line(img, (0,0), (256,256), (0, 255, 0), 1)
img = cv.arrowedLine(img, (0,512), (256,256), (0, 255, 0), 1)

img = cv.rectangle(img, (384,0), (510, 128), (0, 0, 255),  -1,) # -1 for filled, +ve num for thinkness of line

img = cv.circle(img, (100,100), 50, (100,100,20), 2)

font = cv.FONT_HERSHEY_COMPLEX_SMALL
img = cv.putText(img,'Zeyad',(10,210), font, 2, (0, 255, 255), 3)

pts = np.array([[10,5], [20, 30], [70, 20], [50, 10]], np.int32)
img = cv.polylines(img, [pts], True, (0, 240, 100), 4)




cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()