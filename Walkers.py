import cv2


# Create our body classifier


# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# Loop once video is successfully loaded
while True:
    
    # Read first frame

    
    ret, frame = cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(grey,1.2,5)
    for(x,y,w,h)in faces:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,157),2)
    # Display the resulting frame
    cv2.imshow("video", frame)
      
    
    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
