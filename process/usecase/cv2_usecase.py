import cv2
from PIL import Image, ImageDraw

class Cv2Usecase(object):
    def __init__(self, frame, barcode):
        self.frame = frame
        self.barcode = barcode
    
    def rectangle(self):
        barcode = self.barcode

        x = barcode.rect[0]
        y = barcode.rect[1]
        w = barcode.rect[2]
        h = barcode.rect[3]

        cv2.rectangle(self.frame, (x, y),
                     (x + w ,y + h), (0, 255, 0), 2)

        text = "{} ({})".format(barcode.data, barcode._type)
        cv2.putText(self.frame, text, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,5, (0, 0, 125), 2)

    def text(self, font):
        str = self.barcode.data
        img_PIL = Image.fromarray(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))

        draw = ImageDraw.Draw(img_PIL)
        draw.text(font.position, str, font=font.imagefont, fill=font.fillColor)
        return img_PIL