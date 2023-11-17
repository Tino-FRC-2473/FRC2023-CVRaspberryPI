import cv2
import numpy as np
from detector import Detector
from apriltag import AprilTag
from vision_input import VisionInput
import time
import ntcore

inst = ntcore.NetworkTableInstance.getDefault()
inst.startClient4("python")
inst.setServerTeam(2473)

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
    table = inst.getTable("datatable")
    xPub = table.getDoubleTopic("fps_incremented_value").publish()
    xPub.set(frame.sum())

    coneY = table.getDoubleTopic("cone_yaw").publish()
    coneD = table.getDoubleTopic("cone_distance").publish()
    cubeY = table.getDoubleTopic("cube_yaw").publish()
    cubeD = table.getDoubleTopic("cube_distance").publish()

    results = d.detectGameElement(np.asarray(frame), ["CUBE", "CONE"])
    #POSE ESTIMATION APRIL TAG
    pose_data = tag_module.estimate_3d_pose(frame)

    for type, target in results.items():
        if target is not None:
            yaw = target.get_yaw_degrees()
            distance = target.get_distance_meters()

            print("detection: ", time.time() - curr)
            curr = time.time()

            if target.getType() == "CONE":
                coneY.set(yaw)
                coneD.set(distance)
            elif target.getType() == "CUBE":
                cubeY.set(yaw)
                cubeD.set(distance)
    time.sleep(0.02)
