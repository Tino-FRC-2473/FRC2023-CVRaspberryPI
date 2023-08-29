import cv2
import numpy as np
from detector import Detector


cam = cv2.VideoCapture(0)
d = Detector()
while True:
    ret,frame = cam.read()
    d.detectGameElement(np.asarray(frame), ["CUBE", "CONE"])
