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

CALIBRATION_DATA_DIRECTORY = 'checkerboards'
CHECKERBOARD_DIMENSIONS = (6,8)
CHECKERBOARD_SIZE_INCHES = 1
tag_module = AprilTag()
tag_module.calibrate_camera(CALIBRATION_DATA_DIRECTORY, CHECKERBOARD_DIMENSIONS, CHECKERBOARD_SIZE_INCHES)


FOV = (50.28, 29.16)
RES = (320, 240)
CAM_HEIGHT = 0.4
CAM_ANGLE = -15
color_data = {'CUBE': [[110, 100, 100], [158, 255, 255]], 'CONE': [[18.060000000000002, 161.43, 168.63], [31.26, 294.83, 258.07]]}
d = Detector(color_data)
input = VisionInput(FOV, RES, CAM_HEIGHT, CAM_ANGLE)
while True:
    frame = input.getFrame()
    annotated_frame = frame.copy()
    table = inst.getTable("datatable")
    xPub = table.getDoubleTopic("fps_incremented_value").publish()
    xPub.set(frame.sum())

    coneY = table.getDoubleTopic("cone_yaw").publish()
    coneD = table.getDoubleTopic("cone_distance").publish()
    cubeY = table.getDoubleTopic("cube_yaw").publish()
    cubeD = table.getDoubleTopic("cube_distance").publish()

    poseTX = table.getDoubleTopic("pose_tvec_x").publish()
    poseTY = table.getDoubleTopic("pose_tvec_y").publish()
    poseTZ = table.getDoubleTopic("pose_tvec_z").publish()
    poseRX = table.getDoubleTopic("pose_rvec_x").publish()
    poseRY = table.getDoubleTopic("pose_rvec_x").publish()
    poseRZ = table.getDoubleTopic("pose_rvec_x").publish()

    pose_data = tag_module.estimate_3d_pose(frame, annotated_frame)
    colored_objects = d.detectGameElement(frame, annotated_frame)
    
    print(pose_data)

    poseTX = pose_data[0][0]
    poseTY = pose_data[0][1]
    poseTZ = pose_data[0][2]
    poseRX = pose_data[1][0]
    poseRY = pose_data[1][1]
    poseRZ = pose_data[1][2]

    for target in colored_objects:
        type = target.getType()
        yaw = target.get_yaw_degrees()
        distance = target.get_distance_meters()
        if type == "CONE":
            coneY.set(yaw)
            coneD.set(distance)
        elif type == "CUBE":
            cubeY.set(yaw)
            cubeD.set(distance)
        print(type)
        print(yaw)
        print(distance)
    cv2.imshow('result', annotated_frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    time.sleep(0.02)

