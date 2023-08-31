import cv2
import numpy as np
from detector import Detector
from vision_input import VisionInput

cam = cv2.VideoCapture(0)
d = Detector()
while True:
    ret,frame = cam.read()
    d.detect(np.asarray(frame), ["CUBE", "CONE"])