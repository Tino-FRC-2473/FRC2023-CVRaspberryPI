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

    def get_yaw_degrees(self, result, img):
        FOV_X = 70
        FOV_Y = 70
        #get the 4 points of the april tag
        (ptA, ptB, ptC, ptD) = result.corners
        #find the center point of the tag
        center_tag = ((ptA[0]+ptC[0])/2, (ptA[1]+ptC[1])/2)
        #find the center point of the camera
        center_cam = (len(img[0])/2, len(img)/2)
        #calculate the horizontal difference between the center point of the tag and the point of the camera
        B = center_tag[0] - center_cam[0]
        #calculate horizontal center of camera
        A = len(img[0])/2
        #calculate yaw (look at the diagram below to understand the calculation)
        theta = math.atan(B * math.tan(math.radians(FOV_X / 2)) / A)
        return math.degrees(theta)

    def get_pitch_degrees(self, result, img):
      #WRITE CODE HERE
      FOV_X = 70
      FOV_Y = 70
      #get the 4 points of the april tag
      (ptA, ptB, ptC, ptD) = result.corners
      #find the center point of the tag
      center_tag = ((ptA[0]+ptC[0])/2, (ptA[1]+ptC[1])/2)
      #find the center point of the camera
      center_cam = (len(img[0])/2, len(img)/2)
      #calculate the vertical difference between the center point of the tag and the point of the camera
      B = (ptA[1]+ptC[1])/2 - len(img[0])/2
      #calculate vertical center of camera
      A = len(img)/2
      #calculate pitch
      theta = math.atan(B * math.tan(math.radians(FOV_Y / 2)) / A)
      return math.degrees(theta)
