import cv2 as cv
import os
os.chdir(r"C:\Users\zeyad\Pictures\Camera Roll")

img = cv.imread("adha24.jpg")
img2 = cv.imread(r"C:\Users\zeyad\Pictures\Saved Pictures\pexels-pixabay-534181.jpg")
print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv.split(img)
img = cv.merge((b,g,r))

omarHead = img[1065:2245, 2807:3747]
img[2761:3941,4175:5115] = omarHead
image2 = cv.resize(img, (1500, 1000))
img2 = cv.resize(img2, (1500, 1000))
dst = cv.addWeighted(image2, 0.8, img2, 0.2, 0)

cv.imshow("frame", dst)
cv.waitKey(0)
cv.destroyAllWindows()