import cv2
import numpy as np

#DUMMY VISION INPUT (does not include fov and res calib)

cclass VisionInput:
    frame = None
    
    def __init__(self, fov, res: tuple):
        self.fov = fov
        self.w = res[0]
        self.h = res[1]
        
        self.cap = cv2.VideoCapture(0)

    def calibrate(self):
        pass

    #for demo
    def start(self):
        global frame

        while True:
            if not self.cap.isOpened():
                print("failed to init camera")
                exit
            
            cv2.imshow('frame', self.getFrame())

            if (cv2.waitKey(1) == ord('q')):
                break
            
            if (cv2.waitKey(1) == ord('p')):
                print(self.getFrame())
            
        self.cap.release()
        cv2.destroyAllWindows()
    

    def getFrame(self):
        ret, frame = self.cap.read()
        
        if not ret: print('frame malf'); exit
        
        fr = cv2.resize(frame, (self.w, self.h), interpolation=cv2.INTER_AREA)
        return fr
    
    def getGrayFrame(self):
        return cv2.cvtColor(self.getFrame(self), cv2.COLOR_BGR2GRAY)
