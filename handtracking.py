import cv2
import mediapipe as mp

feed = cv2.VideoCapture(0, cv2.CAP_DSHOW) #if you have only one webcam- 0 reads feed fom that one
feed.set(3,640) #setting up its width - id 3 refers to width
feed.set(4,480) #setting up its height - id 4 refers to height
feed.set(10,100) #id 10 is for BRIGHTNESS 

#DEFAULT FORMALITY!!!!
mphands=mp.solutions.hands
hands=mphands.Hands()

while True:
    success,img=feed.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #Converting BGR color coded img to RGB as it is the one supported!
    results=hands.process(imgrgb)       #"process" is an inbuilt function that gives the necessart details automatically

    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break