import cv2
import numpy
import sys

from process.usecase import FrameUsecase, Cv2Usecase, LogUsecase 

def screen_display():
    cv2.namedWindow("camera", cv2.WINDOW_NORMAL)
    camera = cv2.VideoCapture(0)

    while True:

        ret, frame = camera.read()

        frame_uc = FrameUsecase(frame)
        frame_uc.threading()

        if(cv2.waitKey(5)==27):
            break

    camera.release()
    cv2.destroyAllWindows()
