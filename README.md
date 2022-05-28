# aruco-markers-detection

## What’s an Aruco marker ?

|<img src= "https://github.com/rihemebh/aruco-markers-detection/blob/main/aruco-axis.png" width="" height=""/>|An ArUco marker is a fiducial marker(reference object) that is placed on the object or scene being imaged. It’s composed of a wide black border, which helps making their detection easier, and an inner binary matrix that determines its identifier (id).|
|---|---|




They can be also generated in a variety of sizes, which are chosen based on the object size and the scene, for a successful detection.
Depending on the dictionary, there are markers with more or fewer bits (size of the internal matrix). For instance, a marker size of 4x4 is composed of 16 bits. The more bits, the smaller the chance of confusion. However, more bits means that more resolution is required for correct detection. 

<img src= "https://github.com/rihemebh/aruco-markers-detection/blob/main/aruco-sizes.PNG" />

## What information does Aruco provide ?
- The position of its four corners in the image.
- The id of the marker.
- The marker’s top left corner, that is represented by the small red square.
- If the camera is calibrated, the pose (X,Y,Z axis) of the markers can be obtained as well.


## What are they used for ?
The ArUco markers were primarily developed to solve the problem of camera pose estimation, which is based on finding correspondences between points in the real environment and their 2D image projection. 
And thus, it is used in many computer vision systems such as:

- Camera calibration
- Augmented reality
- Object size estimation
- Measuring the distance between the camera and an object
- 3D positioning 
- Object orientation
- Robotics and autonomous navigation


## Benefits 


The primary benefits of using ArUco markers are:

- They are robust, allowing the possibility of applying error detection and correction techniques.
- ArUco markers are built into the OpenCV library via the cv2.aruco submodule.
- The OpenCV library itself can generate ArUco markers via the cv2.aruco.drawMarker function.
- There are online ArUco generators that can be used.
- There are ROS (Robot Operating System) implementations of ArUco markers.
- And from an implementation perspective, ArUco marker detections tend to be accurate, even when using the default parameters.




