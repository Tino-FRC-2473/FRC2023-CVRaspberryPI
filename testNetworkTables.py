#from cscore import CameraServer, VideoSource, UsbCamera, MjpegServer
import time
from ntcore import NetworkTableInstance, EventFlags

# from visionInput import VisionInput
print("hello")
inst = NetworkTableInstance.getDefault()
inst.startClient4("python")
inst.setServerTeam(2473)
# inst.startServer('10.24.73.2')
num = 1

if __name__ == "__main__":

    while True:
        table = inst.getTable("datatable")
        
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

