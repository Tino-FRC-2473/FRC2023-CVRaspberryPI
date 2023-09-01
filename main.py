import cv2
import numpy as np
from detector import Detector
from networktables import NetworkTables
from detector import Detector
from vision_input import VisionInput
import time

NetworkTables.initialize(server='10.24.73.6')
FOV = (55, 45)
RES = (1280, 720)
CAM_HEIGHT = 0.4
CAM_ANGLE = -15
d = Detector()
input = VisionInput(FOV, RES, CAM_HEIGHT, CAM_ANGLE)
while True:
    datatable = NetworkTables.getTable('datatable')
    frame = input.getFrame()
    results = d.detectGameElement(np.asarray(frame), ["CUBE", "CONE"])
    datatable.putNumber('x', frame.sum())
    for type, target in results.items():
        if target is not None:
            yaw = target.get_yaw_degrees()
            distance = target.get_distance_meters()
            if target.getType() == "CONE":
                datatable.putNumber('cone_yaw', yaw)
                datatable.putNumber('cone_distance', distance)
            elif target.getType() == "CUBE":
                datatable.putNumber('cube_yaw', yaw)
                datatable.putNumber('cube_distance', distance)
    time.sleep(0.05)

