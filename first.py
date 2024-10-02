import cv2

#print(cv2.__version__)
cv2.namedWindow("firstimage", cv2.WINDOW_KEEPRATIO) # nessesary if photo resolution is greater than screen resolution
cv2.namedWindow("secondimage", cv2.WINDOW_KEEPRATIO) # nessesary if photo resolution is greater than screen resolution

img = cv2.imread(r'C:\Users\zeyad\Pictures\Camera Roll\adha24.jpg')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(101,101),0)
print(img[0][0])
cv2.imshow('secondimage', imgGray)
cv2.imshow('firstimage', imgBlur)
#k = cv2.waitKey(0) # waits for key 0 to close the image
k = cv2.waitKey(5000) # waits for 5 seconds
#cv2.destroyAllWindows()

if k == 27: #escape key
    cv2.destroyAllWindows()
    
elif k == ord('s'):
    cv2.imwrite('second_image.jpg', img)
    cv2.destroyAllWindows()