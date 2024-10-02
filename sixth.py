import cv2 as cv
import numpy as np

width, height = 500, 700
img = cv.imread(r"C:\Users\zeyad\Pictures\Saved Pictures\pexels-pixabay-534181.jpg")

pts = np.float32([[3948, 716], [5141, 1154], [3296, 2254], [4657,2843]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv.getPerspectiveTransform(pts,pts2)
newImg = cv.warpPerspective(img, matrix, (width, height))


print(pts)
for i in range(len(pts)):
    cv.circle(img, (int(pts[i][0]), int(pts[i][1])), 15, (0,0,225), cv.FILLED)



cv.namedWindow("Original Image", cv.WINDOW_NORMAL) # nessesary if photo resolution is greater than screen resolution
cv.namedWindow("Output Image", cv.WINDOW_NORMAL) # nessesary if photo resolution is greater than screen resolution
cv.imshow("Output Image", newImg)
cv.imshow("Original Image", img)
cv.waitKey(0)
cv.destroyAllWindows()