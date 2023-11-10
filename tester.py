from calibration import calibration 

cal_tester = calibration()
cal_tester.load_images(r"apriltag_pics/")
print(cal_tester.calibrate_camera(2.54, 6, 9))