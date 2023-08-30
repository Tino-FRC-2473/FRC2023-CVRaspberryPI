from simple_pid import PID
from target import Target

class Alignment:
  #Method that returns whether the robot is aligned to the overall Pipeline system
  def alignedToPipeline():
    if Target.get_yaw_degrees() > 4 OR Target.get_yaw_degrees() < -4:
      return false
    else:
      return true

  def getTurnSpeed():
    pid = PID(1, 0.1, 0.05, setpoint=0) #I'm guessing setpoint is the goal yaw angle (0 degrees)

    v = Target.get_yaw_degrees()

    while True:
    # this returns the new motor power
    control = pid(v)

    # Feed the PID output to the system and get its current value
    v = Target.get_yaw_degrees