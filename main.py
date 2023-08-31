import cv2
import numpy as np
from detector import Detector
# from networktables import NetworkTables
from detector import Detector
from vision_input import VisionInput
# from alignment import Alignment

# NetworkTables.initialize(server='10.24.73.6')
FOV = (55, 45)
RES = (1280, 720)
d = Detector()
input = VisionInput(FOV, RES)
# a = Alignment()

while True:
    #datatable = NetworkTables.getTable('datatable')
    frame = input.getFrame()
    d.detectGameElement(np.asarray(frame), ["CUBE", "CONE"])
    # turnSpeed = a.getTurnSpeed()
    # datatable.putNumber('turn speed', turnSpeed)
    # isAligned = a.alignedToPipeline()
    # datatable.putNumber('aligned', isAligned)