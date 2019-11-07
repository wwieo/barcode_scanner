
class LogUsecase(object):
    def __init__(self):
        self.file = open('log.txt','a')
    
    def log_write(self, messages):
        self.file.write(messages)