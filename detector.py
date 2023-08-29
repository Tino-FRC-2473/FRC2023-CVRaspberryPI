import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
from target import Target

class Detector:

    def __init__(self):
        pass
    
    def detectGameElement(self, array, objectsToDetect: list):
        
        eps = 0.015

        frame = cv2.resize(array, (500, int(500*array.shape[0]/array.shape[1])))
        results = dict(zip(objectsToDetect, [None for i in range(len(objectsToDetect))]))

        print(results)


        #CUBE AND CONE DETECTION

        colors = {
            "CUBE": [[158, 255, 255], [90, 50, 70]],
            "CONE": [[25, 255, 255], [22, 50, 70]]
        }
        for object in objectsToDetect:
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv_frame, np.array(colors[object][1]), np.array(colors[object][0]))

            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
            morph = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            contours, hier = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            x = 0
            y = 0
            w = 0
            h = 0

            for contour in contours:
                tx,ty,tw,th = cv2.boundingRect(contour)
                print(tx, ty, tw, th)
                if (tw * th > w * h and not (tx == 0 and ty == 0 and tw == frame.shape[1] and th == frame.shape[0])):
                    x = tx
                    y = ty
                    w = tw
                    h = th

            results[object] = [x, y, w, h]

            print("X: %2d, Y: %2d, W: %2d, H: %2d" % (x, y, w, h))

            #annotate contour
            cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 255), 2)
            cv2.circle(frame, (int(x + w/2), int(y + h/2)), radius = 0, color = (0, 0, 255), thickness=5)
            cv2.putText(frame, object, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2, cv2.LINE_AA)

            while True:
                cv2.imshow("o", frame)
                if cv2.waitKey(0):
                    break
            cv2.destroyAllWindows()

            results[object] = Target([x, y, w, h], object)

            return results
