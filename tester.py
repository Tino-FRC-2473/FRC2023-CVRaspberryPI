from apriltag import AprilTag
import cv2

tag_module = AprilTag()
CALIBRATION_DATA_DIRECTORY = '6x10'
CHECKERBOARD_DIMENSIONS = (5,9)
CHECKERBOARD_SIZE_INCHES = 0.625
tag_module.calibrate_camera(CALIBRATION_DATA_DIRECTORY, CHECKERBOARD_DIMENSIONS, CHECKERBOARD_SIZE_INCHES)

cap = cv2.VideoCapture(0)
while True:
        ret, frame = cap.read()
        pose_data = tag_module.estimate_3d_pose(frame)
        print(pose_data)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()