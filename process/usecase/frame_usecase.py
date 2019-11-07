import cv2
import sys
import numpy
import threading
import pyzbar.pyzbar as pyzbar

from process.entry import Font, Barcode
from .cv2_usecase import Cv2Usecase
from .log_usecase import LogUsecase

class FrameUsecase(object):

    def __init__(self, frame):
        self.frame = frame
        self.barcodes = pyzbar.decode(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

    def threading(self):
        i = 1
        threads = []
        for barcode_original in self.barcodes:       
            threads.append(threading.Thread(target = self.process(barcode=barcode_original), args = (i,)))
            threads[i-1].start()  
            print(i) 
            i+=1
        cv2.imshow("camera", self.frame)   

    def process(self, barcode):
        (x, y, w, h) = barcode.rect
        barcode = Barcode(rect=(x, y, w, h), barcode=barcode)
        
        cv2_uc = Cv2Usecase(frame=self.frame, barcode=barcode)
        cv2_uc.rectangle()
        font = Font(x=x, y=y)
        img_PIL = cv2_uc.text(font=font)

        messages="result=>\n classfied:{0}   content: {1}\n".format(barcode._type, barcode.data)
        LogUsecase().log_write(messages=messages)
        log_bool = self.log_check(barcode=barcode)

        self.frame = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)

    def log_check(self, barcode):
        if((int(barcode.data)>30) or (int(barcode.data)<0)):
            print("barcode has out of range")
            #sys.exit(0) 
        else:
            return True
