import time
import datetime

class Date(object):
    def __init__(self):
        self.date = str(datetime.datetime.fromtimestamp\
            (time.time()).strftime('%d-%m-%Y %H:%M:%S'))
    def __repr__(self):
        return self.date
if __name__ == "__main__":
    print(Date())
