from cscore import CameraServer, VideoSource, UsbCamera, MjpegServer
from ntcore import NetworkTableInstance, EventFlags

class testNetworkTables:
    inst = NetworkTableInstance.getDefault()
    inst.startServer()

    if __name__ == "__main__":
        table = inst.getTable("datatable")
        
        xPub = table.getDoubleTopic("x").publish()
        xPub.set(1)

