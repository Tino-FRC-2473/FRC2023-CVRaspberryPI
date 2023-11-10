from callibration import callibration 

cal_tester = callibration()
cal_tester.load_images(r"C:\Users\nandi\Downloads\arduco")
print(cal_tester.calibrate_camera(2.54, 6, 9))