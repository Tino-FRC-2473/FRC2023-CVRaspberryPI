from calibration import calibration 

cal_tester = calibration()
cal_tester.load_images(r"apriltag_pics/")
# cal_tester.load_images(r"pic_test/")
print(cal_tester.calibrate_chessboard(2.5, 9, 7))
cal_tester.undistortImage(cal_tester.images[0], 2.5, 9, 7)