from callibration import callibration 

cal_tester = callibration()
cal_tester.load_images(r"apriltag_pics/")
print(cal_tester.calibrate_camera(2.54, 6, 9))