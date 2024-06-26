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

    # Sleep to slow meaasurement to save resources/power
    time.sleep(0.2)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3

        # Find distance
        f = 700
        d = (W * f) / w
        print(d)

        # Beep at 6000 Hz for 100 milliseconds if under 50cm
        limit = 50
        if d < limit:
            winsound.Beep(6000, 100)