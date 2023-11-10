cal_tester = callibration()
cal_tester.load_images("C:\Users\nandi\Downloads\arduco")
print(cal_tester.callibrate_camera(2.54, 6, 9))