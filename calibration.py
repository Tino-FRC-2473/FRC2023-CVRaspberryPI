import cv2 
import os 
import glob 
import numpy as np
import cv2
import matplotlib.pyplot as plt

#fix the distoriton parameters of the camera 
class calibration:

    def __init__(self):
        self.images = []
        self.objpoints = []  # 3d point in real world space
        self.imgpoints = []  # 2d points in image plane.

    def load_images(self, directory):
        img_dir = directory# Enter Directory of all images  
        data_path = os.path.join(img_dir,'*g') 
        files = glob.glob(data_path) 
        for f1 in files: 
            img = cv2.imread(f1) 
            self.images.append(img) 

        print(len(self.images))
            
    def calibrate_chessboard(self, square_size, width, height):
        # chessboard_images = self.images
        # use at least 10 images of the chessboard at different angles
        # square_size: the size of each square of the actual chessboard in cm
        # width and height are the dimensions of the chessboard
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # termination criteria to be passed into the algorithm that extracts the camera calibration parameters
        objp = np.zeros((height*width, 3), np.float32)
        objp[:, :2] = np.mgrid[0:width, 0:height].T.reshape(-1, 2)
        # prepares object points defined in a 3D space (Z coordinates set to 0)
        objp = objp * square_size
        
        # # arrays from object points and image points from all images
        # self.objpoints = [] # 3d points in the real world space
        # self.imgpoints = [] # 2d points in the image plane

        #Iterate through all images
        for img in self.images:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #cv2.imshow('',gray)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            #cv2.imwrite('gray_image.png', gray)

            # Find the chess board corners
            ret, corners = cv2.findChessboardCorners(gray, (width, height), None)
            print(ret)

            # If found, add object points, image points (after refining them)
            if ret:
                print("in the if statement")
                self.objpoints.append(objp)   # Certainly, every loop objp is the same, in 3D.
                corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
                self.imgpoints.append(corners2)
                
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(self.objpoints, self.imgpoints, gray.shape[::-1], None, None)
        return [mtx, dist]
    
    def undistortImage(self, img, square_size, width, height):
        mtx, dist = self.calibrate_chessboard(square_size, width, height)

        # img = cv2.imread(image)
        h,  w = img.shape[:2]
        newCameraMatrix, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))


        # Undistort
        dst = cv2.undistort(img, mtx, dist, None, newCameraMatrix)

        # crop the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]
        cv2.imwrite('caliResult1.png', dst)

        # Undistort with Remapping
        mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newCameraMatrix, (w,h), 5)
        dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

        # crop the image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]
        cv2.imwrite('caliResult2.png', dst)
