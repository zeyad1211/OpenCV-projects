import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode


# img = cv.imread(r"C:\Users\zeyad\Pictures\Saved Pictures\employee-card.png")
cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
while True:
    success, img = cap.read()
    for func in decode(img):
        print(func.rect)
        print(func.data)
        myData = func.data.decode('utf-8')
        print(myData)
        pts = np.array([func.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv.polylines(img,[pts], True, (255, 0, 255), 5)
        pts2 = func.rect
        cv.putText(img, myData, (pts2[0], pts2[1]), cv.FONT_HERSHEY_COMPLEX, 0.9, (255, 0, 23), 2)
    cv.imshow('Result', img)
    cv.waitKey(1)

