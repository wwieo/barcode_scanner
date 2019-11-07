from PIL import ImageFont

class Font(object):
    
    def __init__(self, x, y):      
       
        self._type = 'NotoSansCJK-Medium.ttc'
        self.size = 1
        self.imagefont = ImageFont.truetype(self._type, 1, encoding='utf-8')
        self.fillColor = (0,255,255)
        self.position = (x, y-10)
