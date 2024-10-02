import cv2 as cv
import utlis
# broken
webcam = False
path = ''
cap = cv.VideoCapture(0)
cap.set(10, 160)  # Set brightness
cap.set(3, 1920)  # Set width
cap.set(4, 1080)  # Set height
scale = 3
wP = 210 * scale
hP = 297 * scale

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ok, frame = cap.read()
    
    if not ok:
        print("Error: Failed to read frame.")
        break

    frame, finalContours = utlis.getContours(frame, showCanny=False, minArea=50000, filter=4)
      
    if len(finalContours) != 0:
        biggest = finalContours[0][2]
        print(biggest)
        if len(biggest) == 4:  # Ensure we have 4 points
            imgWarp = utlis.warpImg(frame, biggest, wP, hP)
            frame2, finalContours2 = utlis.getContours(imgWarp, minArea=2000, cThr=[50, 50], showCanny=False, filter=4, draw=False)
            
            if len(finalContours2) != 0:
                for obj in finalContours2:
                    cv.polylines(frame2, [obj[2]], True, (0, 255, 0), 2)
                    nPoints = utlis.reorder(obj[2])
                    
                    if nPoints.shape == (4, 2):  # Ensure nPoints has the correct shape
                        nw = round(utlis.findDis(nPoints[0], nPoints[1]) / 30, 1)
                        nh = round(utlis.findDis(nPoints[0], nPoints[2]) / 30, 1)
                        cv.arrowedLine(frame2, (int(nPoints[0][0]), int(nPoints[0][1])), (int(nPoints[1][0]), int(nPoints[1][1])),
                                        (255, 0, 255), 3, 8, 0, 0.05)
                        cv.arrowedLine(frame2, (int(nPoints[0][0]), int(nPoints[0][1])), (int(nPoints[2][0]), int(nPoints[2][1])),
                                        (255, 0, 255), 3, 8, 0, 0.05)
                        x, y, w, h = obj[3]
                        cv.putText(frame2, '{}cm'.format(nw), (x + 30, y - 10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                                    (255, 0, 255), 2)
                        cv.putText(frame2, '{}cm'.format(nh), (x - 70, y + h // 2), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                                    (255, 0, 255), 2)
                    else:
                        print("nPoints does not have the correct shape:", nPoints.shape)

            cv.imshow('A4', frame2)
    frame = cv.resize(frame, (0,0), None, 0.5, 0.5)
    cv.imshow('original', frame)
    
    # Add a condition to break the loop (e.g., press 'q' to quit)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv.destroyAllWindows()