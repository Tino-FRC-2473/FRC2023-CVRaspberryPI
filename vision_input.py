import cv2
import numpy as np

#DUMMY VISION INPUT (does not include fov and res calib)

class VisionInput:
    frame = None
    
    def __init__(self, res, FOV): #a little confused abt the importance of FOV and resolution w/out calibration in the detection pipeline...? - Bhargav
        self.res = res
        self.FOV = FOV
        
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("failed to init camera")
            exit

    def calibrate():
        pass

    def start(self):
        global frame

        while True:
            cv2.imshow('frame', self.getFrame())
            if (cv2.waitKey(1) == ord('q')):
                break
            
            #for testing purposes
            if (cv2.waitKey(1) == ord('p')):
                print(self.getFrame())
            
        self.cap.release()
        cv2.destroyAllWindows()
    

    def getFrame(self):
        ret, frame = self.cap.read()
        
        
        if not ret:
            print('frame not reached')
            exit
        
        #frame = cv2.resize(frame, (600, int(600*frame.shape[1]/frame.shape[0])))

        return np.asarray(frame)