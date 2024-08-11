import cv2
import os
import time
import numpy as np
import autopy
import mediapipe
import HandTrackingModule as htm
# setting the width and height of the window

# prop id of the width is 3 and height is 4

cap = cv2.VideoCapture(0)

###############################################
wScr, hScr = autopy.screen.size()
frameR = 200
smoothening = 5
pTime = 0
plocx, plocy = 0, 0
clocx, clocy = 0, 0
##############################################


print(wScr, hScr)


detector = htm.handDetector(mode=False, maxHands=1, detectionCon=0.5, trackCon=0.5)

while True:
    # 1. Find hand landmarks
    success, frame = cap.read()
    # frame = cv2.resize(frame, (wScr - 2, hScr - 2))
    img = detector.findHands(frame)
    lmList, bbox = detector.findPosition(img)

    hCam, wCam, channel = frame.shape

    # 2. Get the tip of the index and middle fingers
    fingers = [0, 0, 0, 0, 0]
    if(len(lmList) != 0):
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        print(fingers)

        # 4. Only Index finger : Moving Mode
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert our coordinateswScr

            x1 = max(frameR + 1, x1)
            y1 = max(frameR + 1, y1)

            x1 = min(wCam - 1 - frameR, x1)
            y1 = min(hCam - 1 - frameR, y1)

            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

        # 6. Smoothen the values
            clocx = plocx + (x3 - plocx) / smoothening
            clocy = plocy + (y3 - plocy) / smoothening

            # 7. Move Mouse
            autopy.mouse.move(max(0, wCam - clocx), clocy)
            cv2.circle(img, (x1, y1), 15, (255,0, 255), cv2.FILLED)
            plocx, plocy = clocx, clocy

        if fingers[1] == 1 & fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            print(length)

            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
    # 8. Both index and middle fingers are up : clicking mode
    # 9. Find the distance between fingers
    # 10. Click mouse if distance is short

    # 11. Frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0))

    # 12. Display
    if(success):
        cv2.imshow('frame', img)
    if cv2.waitKey(40) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()