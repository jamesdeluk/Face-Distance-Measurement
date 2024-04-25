import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import winsound
import time

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        # Drawing
        # cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        # cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3

        # # Finding the Focal Length
        # d = 50
        # f = (w*d)/W
        # print(f)

        # Finding distance
        f = 700
        d = (W * f) / w
        print(d)

        if d < 50:
            winsound.Beep(6000, 100)  # Beep at 440 Hz for 1000 milliseconds
            time.sleep(0.1)

        # cvzone.putTextRect(img, f'Depth: {int(d)}cm',
        #                    (face[10][0] - 100, face[10][1] - 50),
        #                    scale=2)

    # cv2.imshow("Image", img)
    # cv2.waitKey(1)
