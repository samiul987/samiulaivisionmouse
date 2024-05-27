import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time
import pyautogui

class HandTrackingMouseControl:
    def __init__(self, wCam=640, hCam=480, frameR=100, smoothening=7):
        self.wCam = wCam
        self.hCam = hCam
        self.frameR = frameR
        self.smoothening = smoothening
        self.pTime = 0
        self.plocX, self.plocY = 0, 0
        self.clocX, self.clocY = 0, 0
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, wCam)
        self.cap.set(4, hCam)
        self.detector = HandDetector(maxHands=1)
        self.wScr, self.hScr = pyautogui.size()

    def run(self):
        while True:
            success, img = self.cap.read()
            if not success:
                continue
            hands, img = self.detector.findHands(img)
            if hands:
                lmList = hands[0]['lmList']
                x1, y1 = lmList[8][:2]
                x2, y2 = lmList[12][:2]

                fingers = self.detector.fingersUp(hands[0])

                if fingers[1] == 1 and fingers[2] == 0:
                    x3 = np.interp(x1, (self.frameR, self.wCam - self.frameR), (0, self.wScr))
                    y3 = np.interp(y1, (self.frameR, self.hCam - self.frameR), (0, self.hScr))

                    self.clocX = self.plocX + (x3 - self.plocX) / self.smoothening
                    self.clocY = self.plocY + (y3 - self.plocY) / self.smoothening

                    pyautogui.moveTo(self.wScr - self.clocX, self.clocY)
                    cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                    self.plocX, self.plocY = self.clocX, self.clocY

                if fingers[1] == 1 and fingers[2] == 1:
                    length, _, _ = self.detector.findDistance(lmList[8][:2], lmList[12][:2], img)
                    if length < 40:
                        cv2.circle(img, ((x1 + x2) // 2, (y1 + y2) // 2), 15, (0, 255, 0), cv2.FILLED)
                        pyautogui.click()

            cTime = time.time()
            fps = 1 / (cTime - self.pTime)
            self.pTime = cTime
            cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            cv2.imshow("Image", img)
            cv2.waitKey(1)

def main():
    htmc = HandTrackingMouseControl()
    htmc.run()

if __name__ == "__main__":
    main()
