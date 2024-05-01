import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import time

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    # Sleep to slow meaasurement
    time.sleep(0.2)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        # Draw line between eyes (pupillary distance)
        cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)

        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3

        # Find the focal length
        d = 50
        f = (w*d)/W
        print(f)

    # Display face
    cv2.imshow("Image", img)
    cv2.waitKey(1)