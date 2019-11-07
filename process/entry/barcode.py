
class Barcode(object):
    
    def __init__(self, rect, barcode):
        self.rect = rect
        self.data = barcode.data.decode("utf-8")
        self._type = barcode.type