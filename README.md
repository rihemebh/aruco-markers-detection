# Aruco Markers Detection

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



## Detecting ArUco markers with OpenCV and Python 

### Prerequists & tools

- Python 3  
- opencv package : ``pip install opencv-contrib-python``

### Steps 

1. Load the image 
2. Load the appropriate Dictionnary
3. Define arucro parameters
4. Detect aruco


#### 1. Load the image 

```python

image = cv2.imread(path)
image = imutils.resize(image, width=600)

```
#### 2. Load the appropriate Dictionnary 

Use the ``cv2.aruco.Dictionary_get`` function to grab the dictionary of ArUco markers we’re using.

```python
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
```

#### 3. Define arucro parameters

Define the ArUco detection parameters using ``cv2.aruco.DetectorParameters_create``.

```python

arucoParams = cv2.aruco.DetectorParameters_create()

```
#### 4. Detect Aruco 

We will use the ```cv2.aruco.detectMarker``` function, it accepts 3 arguments:

- **image**: The input image that we want to detect ArUco markers in
- **arucoDict**: The ArUco dictionary we are using
- **parameters**: The ArUco parameters used for detection (unless you have a good reason to modify the parameters, the default parameters returned by cv2.aruco.DetectorParameters_create are typically sufficient)

```python

(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict,
	parameters=arucoParams)
```

And it returns 3 values: 

- **corners**: A list containing the (x, y)-coordinates of our detected ArUco markers
- **ids**: The ArUco IDs of the detected markers
- **rejected**: A list of potential markers that were found but ultimately rejected due to the inner code of the marker being unable to be parsed (visualizing the rejected markers is often useful for debugging purposes)


### Result

<img src="https://github.com/rihemebh/aruco-markers-detection/blob/main/impl/assets/detection_result.PNG" />

