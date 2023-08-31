import cv2
import numpy as np
from detector import Detector
# from networktables import NetworkTables
from detector import Detector
# from alignment import Alignment

# NetworkTables.initialize(server='10.24.73.6')

cam = cv2.VideoCapture(0)
d = Detector()
# a = Alignment()

while True:
    #datatable = NetworkTables.getTable('datatable')
    ret,frame = cam.read()
    d.detectGameElement(np.asarray(frame), ["CUBE", "CONE"])
    # turnSpeed = a.getTurnSpeed()
    # datatable.putNumber('turn speed', turnSpeed)
    # isAligned = a.alignedToPipeline()
    # datatable.putNumber('aligned', isAligned)