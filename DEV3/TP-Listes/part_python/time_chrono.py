import time

global timeStart

def start():
    global timeStart
    timeStart = time.time()

def stop():
    global timeStart
    period = time.time() - timeStart
    print(period)
    return period
