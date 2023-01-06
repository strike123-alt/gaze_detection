import cv2 as cv
import datetime


time = datetime.datetime.now().second
vidcap = cv.VideoCapture(0)
sec = 0
frameRate = 2
seconds = 0
while True:

    hasFrames, image = vidcap.read()
    vidcap.set(cv.CAP_PROP_POS_MSEC, sec*1000)
    # it will capture image in each 5.00 second

    if hasFrames:
        sec = round(sec + frameRate, 2)
        print(datetime.datetime.now().second, ' ',
              datetime.datetime.now().second - time)
        if abs(datetime.datetime.now().second - time) > 2:
            cv.imwrite("images/"+str(sec)+" userName.png", image)
            time = datetime.datetime.now().second
        cv.imshow('video_cap', image)
        if cv.waitKey(1) & 0xFF == ord('q') or not(hasFrames):
            break
    else:
        break
