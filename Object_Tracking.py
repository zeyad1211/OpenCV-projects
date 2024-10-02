import cv2 as cv

cap = cv.VideoCapture(0)

tracker = cv.legacy.TrackerMOSSE_create()
# tracker = cv.legacy.TrackerCSRT_create()   more accurate but alot slower

ret, frame = cap.read()
# frame = cv.flip(frame,1) 
bbox = cv.selectROI("Tracking", frame, True)  # selects region of interest
tracker.init(frame, bbox)

def drawBox(frame, bbox):
    x, y, w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv.rectangle(frame,(x,y), ((x+w),(y+h)), (255, 0, 255), 3, 1)
    cv.putText(frame, "Tracking", (75, 75), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
while(cap.isOpened()): 
    ret, frame = cap.read()
    # fraqme = cv.flip(frame,1) 
    timer = cv.getTickCount()
    success, bbox = tracker.update(frame)
    if success:
        drawBox(frame, bbox)
    else:
        cv.putText(frame, "LOST", (75, 75), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    fps = cv.getTickFrequency()/(cv.getTickCount() - timer)
    cv.putText(frame, str(int(fps)), (75, 50), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
        
    cv.imshow('Tracking', frame) 

    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  