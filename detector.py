import cv2
import apriltag
class Detector():
    def __init__(self):
        options = apriltag.DetectorOptions(families="tag16h5")
        self.aprilTagDetector = apriltag.Detector(options)

    def detectAprilTag(self, img):
        return self.aprilTagDetector.detect(img)
    
    

    
