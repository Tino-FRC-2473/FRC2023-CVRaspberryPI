#from cscore import CameraServer, VideoSource, UsbCamera, MjpegServer
import time
from ntcore import NetworkTableInstance, EventFlags
from visionInput import VisionInput

inst = NetworkTableInstance.getDefault()
inst.startClient4("python")
inst.setServerTeam(2473)
input = VisionInput(70, 1920, 1080)
# inst.startServer('10.24.73.2')
num = 1

if __name__ == "__main__":

    while True:
        table = inst.getTable("datatable")
        img = input.get_frame_gray()
        print("here")
        xPub = table.getDoubleTopic("x").publish()
        xPub.set(num)
        num = num + 1

        xSub = table.getDoubleTopic("x").subscribe(0)
        print(xSub.get())
        time.sleep(0.05)

    # while True:
    #     time.sleep(10)
    

    #print(xPub.getTopic().getProperties())

    # visionInput = VisionInput(70, 960, 720)
    # img = visionInput.get_frame()
    # print(img)

    # network tables system is set up --> problem: datatable connection not working, client is not retrieving data 
    # todo: need to test uploading multiple zipped files to frcvision (this means including the visionInput class)

