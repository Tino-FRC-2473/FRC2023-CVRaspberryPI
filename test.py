import cv2
import numpy as np
from detector import Detector
from apriltag import AprilTag
from vision_input import VisionInput
import time

CALIBRATION_DATA_DIRECTORY = '6x10'
CHECKERBOARD_DIMENSIONS = (5,9)
CHECKERBOARD_SIZE_INCHES = 0.625
tag_module = AprilTag()
tag_module.calibrate_camera(CALIBRATION_DATA_DIRECTORY, CHECKERBOARD_DIMENSIONS, CHECKERBOARD_SIZE_INCHES)


FOV = (50.28, 29.16)
RES = (320, 240)
CAM_HEIGHT = 0.4
CAM_ANGLE = -15
d = Detector()
input = VisionInput(FOV, RES, CAM_HEIGHT, CAM_ANGLE)
while True:

    frame = input.getFrame()

    pose_data = tag_module.estimate_3d_pose(frame)
    colored_objects = d.detectGameElement(np.asarray(frame), ["CUBE", "CONE"])

    for type, target in colored_objects.items():
        if target is not None:
            yaw = target.get_yaw_degrees()
            distance = target.get_distance_meters()

    time.sleep(0.02)
