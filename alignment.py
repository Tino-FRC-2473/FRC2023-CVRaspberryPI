from simple_pid import PID

class Alignment:
  #Method that returns whether the robot is aligned to the overall Pipeline system
  def alignedToPipeline():

  def getTurnSpeed():
    pid = PID(1, 0.1, 0.05, setpoint=1)

    v = controlled_system.update(0)

    while True:
    # Compute new output from the PID according to the systems current value
    control = pid(v)

    # Feed the PID output to the system and get its current value
    v = controlled_system.update(control)