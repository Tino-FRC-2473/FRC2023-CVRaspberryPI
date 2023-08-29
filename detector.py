class Detector:

    def __init__(self):
        pass
    
    def detectGameElement(self, array, objectsToDetect: list):
        
        eps = 0.015

        frame = cv2.resize(array, (500, int(500*array.shape[0]/array.shape[1])))
        results = dict(zip(objectsToDetect, [None for i in range(len(objectsToDetect))]))

        print(results)


        #CUBE AND CONE DETECTION

        colors = {
            "CUBE": [[158, 255, 255], [90, 50, 70]],
            "CONE": [[25, 255, 255], [22, 50, 70]]
        }
<<<<<<< Updated upstream
        
=======

>>>>>>> Stashed changes
        for object in objectsToDetect:
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv_frame, np.array(colors[object][1]), np.array(colors[object][0]))

            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
            morph = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

<<<<<<< Updated upstream

            if (object == "CUBE"):
                contours, hier = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

                x = 0
                y = 0
                w = 0
                h = 0
                for contour in contours:  
                        tx,ty,tw,th = cv2.boundingRect(contour)
                        #print(tx, ty, tw, th)
                        if (tw * th > w * h and not (tx == 0 and ty == 0 and tw == frame.shape[1] and th == frame.shape[0])):
                            x = tx
                            y = ty
                            w = tw
                            h = th

                if (object in objectsToDetect): results[object] = [x, y, w, h]

                #print("X: %2d, Y: %2d, W: %2d, H: %2d" % (x, y, w, h))

                #annotate contour
                cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 255), 2)
                cv2.circle(frame, (int(x + w/2), int(y + h/2)), radius = 0, color = (0, 0, 255), thickness=5)
                cv2.putText(frame, object, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2, cv2.LINE_AA)
                results[object] = Target([x, y, w, h], object)

            if (object == "CONE"):
                straight_contours, hier = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

                temp_ctr_max = None
                x = 0
                y = 0
                w = 0
                h = 0

                for contour in straight_contours:
                        tx,ty,tw,th = cv2.boundingRect(contour)
                        #print(tx, ty, tw, th)
                        if (tw * th > w * h and not (tx == 0 and ty == 0 and tw == frame.shape[1] and th == frame.shape[0])):
                            x = tx
                            y = ty
                            w = tw
                            h = th
                            temp_ctr_max = contour

                epsilon = eps * cv2.arcLength(temp_ctr_max, True)
                approx = cv2.approxPolyDP(temp_ctr_max, epsilon, True)
                
                i = 0

                tl = None
                tr = None
                bl = None
                br = None

                for vertex in approx:
                    cv2.circle(frame, vertex[0], 2, (0, 0, 255), 5)

                    x, y = vertex[0]

                    if (tl == None or (x < tl[0] and y < tl[1])):
                        tl = (x, y)
                    elif (tr == None or (x > tr[0] and y < tr[1])):
                        tr = (x, y)
                    elif (bl == None or (x < bl[0] and y > bl[1])):
                        bl = (x, y)
                    elif (br == None or (x > br[0] and y > br[1])):
                        br = (x, y)

                cv2.drawContours(frame, [approx], -1, (0, 0, 255), 2)

                cv2.circle(frame, tl, 2, (0, 255, 0), 5)
                cv2.circle(frame, tr, 2, (0, 255, 0), 5)
                cv2.circle(frame, bl, 2, (0, 255, 0), 5)
                cv2.circle(frame, br, 2, (0, 255, 0), 5)


                #https://docs.revrobotics.com/frc-kickoff-concepts/charged-up-2023/game-elements - dimension uncertainty factored in 
                #NEED TO CHECK IF VERTEX POINTS TL and TR and BL and BR are collinear (this is easy, i am lazy, someone else do it)

                if ((tl[1] - tr[1])/(bl[1] - br[1]) < (45/213) and (tl[1] - tr[1])/(bl[1] - br[1]) < (26/213) and tl[0] > bl[0] and tr[0] < br[0]):
                    results[object] = Target([tl, tr, bl, br], object)


            while True:
                cv2.imshow("o", frame)
                if cv2.waitKey(0):
                    break
            
            cv2.destroyAllWindows()

        return results

    def detectColoredShape(self, array, rgb_col):
        color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red1': [[180, 255, 255], [159, 50, 70]],
              'red2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}
        
        #================================================================================

        frame = cv2.resize(array, (500, int(500*array.shape[0]/array.shape[1])))
        results = dict(zip(rgb_col, [None for i in range(len(rgb_col))]))

        print(rgb_col)

        for object in rgb_col:
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv_frame, np.array(color_dict_HSV[object][1]), np.array(color_dict_HSV[object][0]))

            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
            morph = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
=======
>>>>>>> Stashed changes
            contours, hier = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            x = 0
            y = 0
            w = 0
            h = 0

            for contour in contours:
                tx,ty,tw,th = cv2.boundingRect(contour)
                print(tx, ty, tw, th)
                if (tw * th > w * h and not (tx == 0 and ty == 0 and tw == frame.shape[1] and th == frame.shape[0])):
                    x = tx
                    y = ty
                    w = tw
                    h = th

            results[object] = [x, y, w, h]

            print("X: %2d, Y: %2d, W: %2d, H: %2d" % (x, y, w, h))

            #annotate contour
            cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 255), 2)
            cv2.circle(frame, (int(x + w/2), int(y + h/2)), radius = 0, color = (0, 0, 255), thickness=5)
            cv2.putText(frame, object, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2, cv2.LINE_AA)

            while True:
                cv2.imshow("o", frame)
                if cv2.waitKey(0):
                    break
<<<<<<< Updated upstream
            
=======

>>>>>>> Stashed changes
            cv2.destroyAllWindows()

            results[object] = Target([x, y, w, h], object)

<<<<<<< Updated upstream
        return results
    


    #will be handled, i assume?
    def detectAprilTag(self, array):
        results = []
        return results

=======
            return results
>>>>>>> Stashed changes
