import numpy as np
import cv2
import matplotlib.pyplot as plt

#basically fixes the intrinsic parameters and is the class that returns the 3D stuff
class apriltag:

    def __init__(self, image):
        self.image = cv.readImage(image)
        #from the april tag notebook double check if causing errors
        self.grayscale = cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)

    #method that gets the corner of an image that is taken by the camera of the april tag
    def findAprilTagCorners():
        return self.image.corners

    def specificAprilTagCorners():
        #defines the termination criteria for corner sub-pixel refinement
        #cv.Term_CRITERIA_EPS ---> desired accuracy in this case 0.001
        #cv.TERM_CRITERIA_MAX_ITER ---> maximum number of iterations code has to do before terminating
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        
        #cornerSubPix takes the grayscale image
        return cv.cornerSubPix(self.grayscale,findAprilTagCorners(),(11,11),(-1,-1), criteria)
    
    def drawBoundingBox():
        (ptA, ptB, ptC, ptD) = self.image.corners
        ptB = (int(ptB[0]), int(ptB[1]))
        ptC = (int(ptC[0]), int(ptC[1]))
        ptD = (int(ptD[0]), int(ptD[1]))
        ptA = (int(ptA[0]), int(ptA[1]))

        # draw the bounding box of the AprilTag detection
        cv2.line(img_bgr, ptA, ptB, (0, 255, 0), 2)
        cv2.line(img_bgr, ptB, ptC, (0, 255, 0), 2)
        cv2.line(img_bgr, ptC, ptD, (0, 255, 0), 2)
        cv2.line(img_bgr, ptD, ptA, (0, 255, 0), 2)

        # draw the center (x, y)-coordinates of the AprilTag
        (cX, cY) = (int(self.image.center[0]), int(self.image.center[1]))
        cv2.circle(self.image, (cX, cY), 5, (0, 0, 255), -1)

        # draw the tag family on the image
        tagFamily = self.image.tag_family.decode("utf-8")
        cv2.putText(img_bgr, tagFamily, (ptA[0], ptA[1] - 15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print("[INFO] tag family: {}".format(tagFamily))

        # show the output image after AprilTag detection
        #resize later if necessary
        plt.imshow(self.image)

    def getRotation(mtx, dist):
        
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        objp = np.zeros((24*17,3), np.float32)
        objp[:,:2] = np.mgrid[0:24,0:17].T.reshape(-1,2)


        ret, corners = cv.findChessboardCorners(self.grayscale, (24,17),None)

        if ret == True:

            corners2 = cv.cornerSubPix(self.grayscale,corners,(11,11),(-1,-1), criteria)

            # Find the rotation and translation vectors.
            ret, rvecs, tvecs = cv.solvePnP(objp, corners2, mtx, dist)


