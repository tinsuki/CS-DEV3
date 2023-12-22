import time_profiler

import numpy
from math import pi, sin
from cmath import exp
from fourier import fourier

def dft(frame):
    N = len(frame)
    spectrum = [0 for _ in range(int(N/2+1))]
    for m in range(int(N/2+1)):
        for n in range(N):
            spectrum[m]+=frame[n]*exp(-2*1j*pi*n*m/N)
    return numpy.array(spectrum)

def essai(N):
    signal = list()
    for n in range(N):
        signal.append(sin(2*pi*440*n/44100))
    return numpy.array(signal)

s = essai(2048)
#s = essai(1024*2)

time_profiler.start()

S = dft(s)

time_profiler.stop()
time_profiler.start()

S = fourier(s)

time_profiler.stop()

#print(abs(S))

# End Of File
