import cv2
import numpy as np

#fix the distoriton parameters of the camera 
class callibration:

    def calibrate_camera(chessboard_images, square_size, width, height):

        # use at least 10 images of the chessboard at different angles
        # square_size: the size of each square of the actual chessboard in cm
        # width and height are the dimensions of the chessboard
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # termination criteria to be passed into the algorithm that extracts the camera calibration parameters
        objp = np.zeros((height*width, 3), np.float32)
        objp[:, :2] = np.mgrid[0:width, 0:height].T.reshape(-1, 2)
        # prepares object points defined in a 3D space (Z coordinates set to 0)
        objp = objp * square_size
        objpoints = []  # 3d point in real world space
        imgpoints = []  # 2d points in image plane.
        # arrays from object points and image points from all images

        cap = cv2.VideoCapture(0)
        found = 0
        while(found < 10):  # Here, 10 can be changed to whatever number you like to choose
            ret, img = cap.read() # Capture frame-by-frame
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Find the chess board corners
            #ret, corners = cv2.findChessboardCorners(gray, (7,6),None)

            # If found, add object points, image points (after refining them)
            if ret == True:
                objpoints.append(objp)   # Certainly, every loop objp is the same, in 3D.
                corners2 = cv2.cornerSubPix(gray.corners,(11,11),(-1,-1),criteria)
                imgpoints.append(corners2)

                # Draw and display the corners
                img = cv2.drawChessboardCorners(img, (7,6), corners2, ret)
                found += 1

            cv2.imshow('img', img)
            cv2.waitKey(10)

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

        return ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
