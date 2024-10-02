import cv2 as cv
import numpy as np



circles = np.zeros((4,2), np.int32)
counter = 0


def mousePoints(event, x, y, flags, param):
    global counter
    if event == cv.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        print(circles)
        cv.circle(img, (x, y), 20, (0,0,225), cv.FILLED)
        counter += 1
        cv.imshow("Orimage", img)

img = cv.imread(r"C:\Users\zeyad\Pictures\Saved Pictures\pexels-pixabay-534181.jpg")       
# img = cv.imread(r"C:\Users\zeyad\Pictures\Saved Pictures\Latin_dictionary.jpg")


cv.namedWindow("Orimage", cv.WINDOW_NORMAL) # nessesary if photo resolution is greater than screen resolution
cv.imshow("Orimage", img)
cv.setMouseCallback("Orimage", mousePoints)


while True:
    if counter == 4:
        width, height = 500, 700
        pts = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv.getPerspectiveTransform(pts,pts2)
        newImg = cv.warpPerspective(img, matrix, (width, height))
        cv.namedWindow("Output Image", cv.WINDOW_NORMAL) # nessesary if photo resolution is greater than screen resolution
        cv.imshow("Output Image", newImg)
    
    
    if cv.waitKey(1) & 0xFF == ord('q'): 
            break
        
        
cv.destroyAllWindows()