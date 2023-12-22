#import time_profiler

from numpy import array
from math import pi, sin
from cmath import exp
from fourier import fourier
import time_profiler
import time

def dft(frame):
    spectrum = list()
    N = len(frame)
    for k in range(N):
        value = 0
        for n in range(N):
            value = value + frame[n] * exp(-2*pi*1j*k*n/N)
        spectrum.append(value)
    return array(spectrum)

def essai(N):
    signal = list()
    for n in range(N):
        signal.append(sin(2*pi*440*n/44100))
    return array(signal)

s = essai(1024*2)

start = time.time()

time_profiler.start()

S = dft(s)

time_profiler.stop()
print(time.time()-start)

print(abs(S))


start = time.time()
time_profiler.start()
S = fourier(s)

time_profiler.stop()
print(time.time()-start)

print(abs(S))

# End Of File
