import numpy as np
import cv2
import matplotlib.pyplot as plt

def getCallibration():
    ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, frameSize, None, None)
    return rect, cameraMatrix, dist, revecs, tvecs

def findCorners(image):
    return image.corners
	
def drawBoundingBox(image):
    (ptA, ptB, ptC, ptD) = image.corners
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
	(cX, cY) = (int(image.center[0]), int(image.center[1]))
	cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)

	# draw the tag family on the image
	tagFamily = image.tag_family.decode("utf-8")
	cv2.putText(img_bgr, tagFamily, (ptA[0], ptA[1] - 15),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
	print("[INFO] tag family: {}".format(tagFamily))

    # show the output image after AprilTag detection
    #resize later if necessary
    plt.imshow(image)

def undistort(image):
    #slicing the datea from image.shape() to only get the height and width
    h,  w = image.shape[:2]

    newCameraMatrix, roi = cv.getOptimalNewCameraMatrix(cameraMatrix, dist, (w,h), 1, (w,h))

    # Undistort
    dst = cv.undistort(img, cameraMatrix, dist, None, newCameraMatrix)