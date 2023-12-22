import time_chrono
from memory_profiler import profile

l = list()

#@profile
def solution1(l):
    for i in range(65536):
        l.append(i)
    return l.reverse()
#@profile
def solution2(l):
    for i in range(65536):
        l.insert(0, i)
    return l

time_chrono.start()
solution1(l)
time_chrono.stop()

del l

l = list()

time_chrono.start()
solution2(l)
time_chrono.stop()

del l