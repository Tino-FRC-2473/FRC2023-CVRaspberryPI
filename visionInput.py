import cv2
class VisionInput():
    def __init__(self, FOV, PIXELS_WIDTH, PIXELS_HEIGHT):
        self.FOV = FOV
        self.PIXELS_WIDTH = PIXELS_WIDTH
        self.PIXELS_HEIGHT = PIXELS_HEIGHT
        self.cap = cv2.VideoCapture(0)
    
    def get_frame(self):
        ret, frame = self.cap.read()
        resize = cv2.resize(frame, (self.PIXELS_WIDTH, self.PIXELS_HEIGHT), interpolation = cv2.INTER_AREA)
        return resize
