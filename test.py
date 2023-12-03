import cv2
import numpy as np
from detector import Detector
from apriltag import AprilTag
from vision_input import VisionInput
import time


tag_module = AprilTag()
# CALIB_DIR = 'images'
# CALIB_SIZE_METERS = 0.0301625
# CALIB_WIDTH = 5
# CALIB_HEIGHT = 7
# tag_module.calibrate(CALIB_DIR, CALIB_SIZE_METERS, CALIB_WIDTH, CALIB_HEIGHT)
#UNCOMMENT ABOVE IF CALIBRATION DATA is not in /calibration_data direcotry

FOV = (50.28, 29.16)
RES = (640, 480)
CAM_HEIGHT = 0.4
CAM_ANGLE = -15
color_data = {'CUBE': [[110, 100, 100], [158, 255, 255]], 'CONE': [[18.060000000000002, 161.43, 168.63], [31.26, 294.83, 258.07]]}
d = Detector(color_data)
input = VisionInput(FOV, RES, CAM_HEIGHT, CAM_ANGLE)
while True:
    frame = input.getFrame()
    annotated_frame = frame.copy()
    pose_data = tag_module.estimate_3d_pose(frame, annotated_frame)
    colored_objects = d.detectGameElement(frame, annotated_frame)
    #print(pose_data)
    for target in colored_objects:
        type = target.getType()
        yaw = target.get_yaw_degrees()
        distance = target.get_distance_meters()
        #print(type)
        #print(yaw)
        #print(distance)
    cv2.imshow('result', annotated_frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    time.sleep(0.02)
