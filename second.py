
# importing libraries 
import cv2 
import numpy as np 



# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture(0) 
fourcc = cv2.VideoWriter.fourcc(*'XVID')

out = cv2.VideoWriter("output.avi", fourcc, 20.0,(640,480),True)

frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(frameWidth)
print(frameHeight)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)

# Check if camera opened successfully 
if (cap.isOpened()== False): 
    print("Error opening video file") 
  
# Read until video is completed 
while(cap.isOpened()): 
      
# Capture frame-by-frame 
    ret, frame = cap.read() 
    # print(frame)
    if ret == True: 
        frameflip = cv2.flip(frame,1)
    # Display the resulting frame 
        cv2.imshow('Frame', frameflip) 
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
          
    # Press Q on keyboard to exit 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
  
# Break the loop 
    else: 
        break
  
# When everything done, release 
# the video capture object 
cap.release() 
out.release()
# Closes all the frames 
cv2.destroyAllWindows()