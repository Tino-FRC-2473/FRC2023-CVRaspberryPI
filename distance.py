CAM_HEIGHT = 0 #default
CUBE_TO_CAM = math.abs(CAM_HEIGHT - 0.24/2) #default
CONE_TO_CAM = math.abs(CAM_HEIGHT - 0.33/2) #default
class Distance:
  def getDistance(target, result, img):
    if( target == 'Cube'):
      height = CUBE_TO_CAM
    else:
      height = CONE_TO_CAM
    print("pitch: ", Detector.get_pitch_degrees(result, img))
    return height/math.tan(np.radians(Detector.get_pitch_degrees(result, img)))