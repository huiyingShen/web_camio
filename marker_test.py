import cv2
from cv2 import aruco

dictionary = aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)

def cap1(cam=0):
    cap = cv2.VideoCapture(c)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

    while True:
        ret, frame =cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        res = cv2.aruco.detectMarkers(gray,dictionary)
        c = cv2.waitKey(30) & 0xFF
        if c==ord('s'):
            cv2.imwrite("cap.jpg",frame)

        aruco.drawDetectedMarkers(frame,res[0],res[1])
        cv2.imshow('detection',frame)

    
# frame = cv2.imread("marker.jpg")
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# res = cv2.aruco.detectMarkers(gray,dictionary)
# print(res[0])

[195., 285.],
        [205., 192.],
        [300., 208.],
        [294., 298.]