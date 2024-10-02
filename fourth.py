import cv2 as cv
import numpy as np

img = np.zeros((600, 900, 3), dtype = np.uint8)

#background

cv.rectangle(img, (0,0),(900,500),(255,225,85), -1) #draw rectangle

cv.rectangle(img, (0,500),(900,600),(75,180,70), -1) #draw rectangle



#sun

cv.circle(img, (200,150), 60, (0,255,255), -1) #draw circle

cv.circle(img, (200,150), 60, (220,255,255), 10) #draw circle



# *** TREE 1 ***



#tree stem

cv.line(img, (710, 500), (710, 420), (30,65,155), 15) #darw line



#tree leafs

triangle2 = np.array([[640,460],[780,460], [710,200]], dtype=np.int32) #array to darw fillpoly

cv.fillPoly(img, [triangle2], (75,180,70))



# *** TREE 2 ***

#tree stem

cv.line(img, (600, 500), (600, 420), (30,65,155), 25) #darw line

#tree leafs

triangle = np.array([[500,440],[700,440], [600,75]], dtype=np.int32) #array to darw the second fillpoly

cv.fillPoly(img, [triangle], (75,200,70))



#text

font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX #text type

cv.putText(img, "I Love Python", (120,490), font, 1.5, (255,255,255), 2) #write text on image



cv.imwrite("tree.png", img) #save image

cv.imshow("tree", img) #show image



cv.waitKey(0) #waitkey from keyboard

cv.destroyAllWindows() #close any opened window

#=======================#