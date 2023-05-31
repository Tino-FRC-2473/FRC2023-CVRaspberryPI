#from cscore import CameraServer, VideoSource, UsbCamera, MjpegServer
from ntcore import NetworkTableInstance, EventFlags

# from visionInput import VisionInput
inst = NetworkTableInstance.getDefault()
inst.startServer()

if __name__ == "__main__":
    table = inst.getTable("datatable")
    
    print("here")
    xPub = table.getDoubleTopic("x").publish()
    xPub.set(1)

    xSub = table.getDoubleTopic("x").subscribe(0)
    print(xSub.get())

    #print(xPub.getTopic().getProperties())

    # visionInput = VisionInput(70, 960, 720)
    # img = visionInput.get_frame()
    # print(img)

    # network tables system is set up --> problem: datatable connection not working, client is not retrieving data 
    # todo: need to test uploading multiple zipped files to frcvision (this means including the visionInput class)

