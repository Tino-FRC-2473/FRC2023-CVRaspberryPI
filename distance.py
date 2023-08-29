CUBE_TO_CAM = 0 #default
CONE_TO_CAM = 0 #default
class Distance:
  def getDistance(target, result, img):
    if( target == 'Cube'):
      height = CUBE_TO_CAM
    else:
      height = CONE_TO_CAM
    return height/math.tan(np.radians(Detector.get_pitch_degrees(result, img)))