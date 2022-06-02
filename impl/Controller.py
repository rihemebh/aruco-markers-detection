from fastapi import FastAPI, File, UploadFile, Form
from starlette.responses import JSONResponse
import cv2
import cv2.aruco as aruco
import imutils
import numpy as np

from impl.Service import detect_aruco

app = FastAPI()


@app.post("/detect")
async def detect(cornerid: int = Form(...), robotid: int = Form(...), endid: int = Form(...),
                 file: UploadFile = File(...)):
    print(cornerid, robotid, endid)
    path = "impl/assets/image.png"
    with open(path, 'wb') as image:
        content = await file.read()
        image.write(content)
        image.close()
    dict4 = aruco.Dictionary_get(aruco.DICT_4X4_1000)

    image = cv2.imread(path)
    image = imutils.resize(image, width=600)

    state = detect_aruco(image, dict4)

    if len(np.where(state == cornerid)[0]) < 4:
        return JSONResponse(content={"message": "state : You should take the picture of the whole map"})
    elif len(np.where(state == robotid)[0]) == 0:
        return JSONResponse(content={"message": "state : There is no robot in this map"})

    elif (len(np.where(state == endid)[0]) == 0) and (len(np.where(state == robotid)[0]) == 1) and (
            len(np.where(state == cornerid)[0]) == 4):
        return JSONResponse(content={"message": "state : Valid"})
    else:
        return JSONResponse(content={"message": "state : You should complete the mission"})
