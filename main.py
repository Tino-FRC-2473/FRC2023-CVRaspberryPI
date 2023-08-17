import time
from networktables import NetworkTables
from visionInput import VisionInput
from detector import Detector

#table = NetworkTablesInstance(server='10.24.73.6')
NetworkTables.initialize(server='10.24.73.6')
#datatable = NetworkTables.getTable('datatable')
#datatable = NetworkTables.getTable('SmartDashboard')
input = VisionInput(70, 1920, 1080)
detector = Detector()

num = 1

if __name__ == "__main__":

    while True:
        img = input.get_frame_gray()
        datatable = NetworkTables.getTable('datatable')
        result = detector.detectAprilTag(img)
        print(img.sum())
        datatable.putNumber('x', img.sum())

        x = datatable.getNumber('x', -1)
        print(x)
        num = num + 1

        time.sleep(0.05)
    # while True:
    #     time.sleep(10)
    

    #print(xPub.getTopic().getProperties())

    # visionInput = VisionInput(70, 960, 720)
    # img = visionInput.get_frame()
    # print(img)

    # network tables system is set up --> problem: datatable connection not working, client is not retrieving data 
    # todo: need to test uploading multiple zipped files to frcvision (this means including the visionInput class)

