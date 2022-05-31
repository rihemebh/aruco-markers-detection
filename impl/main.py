import cv2
import cv2.aruco as aruco
import imutils
import numpy as np


def detect_aruco(image, dict):
    state = np.array([], int)
    aruco_params = cv2.aruco.DetectorParameters_create()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(image, dict,
                                                       parameters=aruco_params)

    if len(corners) > 0:
        ids = ids.flatten()

        # loop over the detected ArUCo corners
        for (markerCorner, markerID) in zip(corners, ids):
            # extract the marker corners (which are always returned in
            # top-left, top-right, bottom-right, and bottom-left order)
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            # draw the bounding box of the ArUCo detection
            cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)

            # compute and draw the center (x, y)-coordinates of the ArUco
            # marker
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)

            # draw the ArUco marker ID on the image
            cv2.putText(image, str(markerID),
                        (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)
            state = np.append(state, [markerID])

            print("[INFO] ArUco marker ID: {}".format(markerID))

        # show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(0)
    return state


# validated_state = np.array([10, 20, 30, 40, 150])
# not_validated_state = np.array([10, 20, 30, 40, 150, 150])

dict4 = aruco.Dictionary_get(aruco.DICT_4X4_100)
dict5 = aruco.Dictionary_get(aruco.DICT_5X5_100)

path_1 = "assets/validated.png"
path_2 = "assets/not_validated.png"

image_1 = cv2.imread(path_1)
image_1 = imutils.resize(image_1, width=600)

image_2 = cv2.imread(path_2)
image_2 = imutils.resize(image_2, width=600)

print(detect_aruco(image_2, dict4))
print(detect_aruco(image_1, dict4))
