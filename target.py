#NOT DONE

class Target:
    def __init__(self, contour, target_type):
        self.contour = contour
        self.target_type = target_type
    
    def __str__(self):
        return self.target_type + " coords - " + self.contour

    def getType(self):
        return self.target_type

    def getContour(self):
        return self.contour
    
    def computeYawAngle(R):
        pass

    def computePitchAngle(R):
        pass