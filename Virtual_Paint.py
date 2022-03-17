import cv2
#import mediapipe as mp
import os
import handTrackingModule as htm
import numpy as np

path = 'header'
mylist = os.listdir(path)
print(mylist)
overlay = []
xp,yp = 0,0
imgCanvas = np.zeros((720,1280,3),np.uint8)

for imgPath in mylist:
    image = cv2.imread(f'{path}/{imgPath}')
    overlay.append(image)


header = overlay[0]
color = (0,255,0)

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = htm.handDetector(detectionCon=0.5)
while cap.isOpened():
    success , img = cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    lmlist,_ = detector.findPosition(img,draw=False)

    if len(lmlist) != 0:
        #print(lmlist)
        # tip  of index and  middle finger
        x1,y1 = lmlist[8][1:]
        x2,y2 = lmlist[12][1:]

        # check which fingers are  up
        fingers = detector.fingersUp()
        #print(fingers)
        if fingers[1] == False and fingers[2] == True:
            print('drawing mode')
            cv2.circle(img,(x1,y1),15,color,cv2.FILLED)
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            if color == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), color,50)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), color,50)
            else:
                cv2.line(img, (xp, yp), (x1, y1), color, 15)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), color, 15)

            xp, yp = x1, y1
        elif fingers[1] == False and fingers[2] == False:
            print('selection mode')
            xp, yp = 0,0
            if 0 < y1 < 125:
                if 400 < x1 <500:
                    header = overlay[1]
                    color = (200,0,0)
                elif 170 < x1 < 250:
                    header = overlay[2]
                    color = (255, 0, 255)
                elif 650 < x1 < 750:
                    header = overlay[0]
                    color = (0, 255, 0)
                elif 850 < x1 < 950:
                    header = overlay[3]
                    color = (0, 0, 0)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), color, cv2.FILLED)

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    img[0:125,0:1280] = header
    #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("image",img)
    #cv2.imshow("imageCanvas",imgCanvas)
    #cv2.imshow("imageInv",imgInv)
    k = cv2.waitKey(3)
    if k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()


