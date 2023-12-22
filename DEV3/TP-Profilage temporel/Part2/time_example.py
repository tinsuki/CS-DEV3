import time
from time_chrono import start 
from time_chrono import stop

def countdown():
    for i in range(10):
        time.sleep(1)
        print(i,"s\n")


start()
countdown()
stop()