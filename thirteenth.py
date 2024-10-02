import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode
import os
os.chdir(r"C:\Users\zeyad\Pictures\Saved Pictures")

# img = cv.imread("employee-card.png")
cap = cv.VideoCapture(0)

while True:
    ok, frame = cap.read()

    for barcode in decode(frame):
        # print(barcode.data) # can also say barcode.rect for rectangle coordinates
        myData = barcode.data.decode('utf-8') 
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape(-1, 1, 2)
        cv.polylines(frame,[pts], True, (255,0, 255), 5)
        pts2 = barcode.rect
        cv.putText(frame, myData, (pts2[0], pts2[1]), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 2)
        
        
        
        
    cv.imshow("Result", frame)
    cv.waitKey(1)
    # cv.destroyAllWindows()
    code = decode(frame)
    print(code) 
