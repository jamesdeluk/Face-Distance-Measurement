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

        # Draw line between eyes (pupillary distance)
        # cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        # cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)

        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3

        # Find the focal length
        # d = 50
        # f = (w*d)/W
        # print(f)

        # Find distance
        f = 680
        d = (W * f) / w
        print(d)

        # Beep at 6000 Hz for 100 milliseconds if distance under 
        limit = 48
        if d < limit:
            winsound.Beep(6000, 100)

        # Draw text box with depth measurement
        # cvzone.putTextRect(img, f'Depth: {int(d)}cm',
        #                    (face[10][0] - 100, face[10][1] - 50),
        #                    scale=2)

    # Display face (also required for finding the focal length)
    # cv2.imshow("Image", img)
    # cv2.waitKey(1)
