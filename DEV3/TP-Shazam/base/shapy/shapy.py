#!/ IMPORTANT: add the shebang for Python version 3 (#!/...)

import sys
import wave
from array import *

from settings import *
from fourier import *
from table import *
from hits import *
from histogram import *

table_name = "database"  # name of the database on disk

Moff = int(44/2)  # avoid starting from 1...
M = 44*3  # keep approx. 3 seconds of peaks in the input buffer

# the input buffer (short-term memory): index 0 is the most recent (present)

def buffer_new():
    buffer = []
    for m in range(M):
        buffer.append([])
    return buffer

def buffer_shift(buffer):
#    assert(len(buffer) == M)
    buffer.pop()  # remove last element
    buffer.insert(0, [])  # add empty ahead
    return buffer

def check_wav_header(file):
    assert(file.getnchannels() == 1)
    assert(file.getframerate() == get_sampling_rate())
    assert(file.getsampwidth() == 2)

def frame_read(file):
    frame = array('d', [])
    window_size = get_window_size()
    for n in range(window_size):
        data = file.readframes(1)
        if data == b'':
            return None  # End Of File
        value = int.from_bytes(data, byteorder='little', signed='True')
        frame.append(value / 32768.0)
    return frame

# parse arguments

argc = len(sys.argv)
if argc != 3:
    print ("Usage:", str(sys.argv[0]), "<store|query> <file>")
    exit()

mode = str(sys.argv[1])
name = str(sys.argv[2])

store = None
if mode == "store":
    store = True
elif mode == "query":
    store = False
else:
    print ("mode not supported")
    exit()

print ("loading database...")
table = table_load(table_name)  # long-term memory
song = table_get_number_of_songs(table)  # number of songs in the database
print (" (%d songs) done" % song)

hits = None

if store:
    song = song + 1
    print ("storing song #%d" % song)
else:  # query
    hits = hits_new(song)

buffer = buffer_new()  # short-term memory
current_time = 0
# statistics
peak_count = 0
pair_count = 0

with wave.open(name, "rb") as file:
    check_wav_header(file)
    # browse the whole sound file
    while True:
        # frame
        s = frame_read(file)  # no overlap (yet?)
        if s == None:  # End Of File
            break
        # spectrum
        S = abs(fourier(s)) / get_window_size()  # backward compatibility...
        # peaks
        N = get_window_size()  # no overlap (yet?)...
        Fs = get_sampling_rate()
        amax = max(S)  # idea: consider global maximum
        for m in range(2, len(S)-2):
            if (S[m] > 0.1 * amax) and (S[m-1] < S[m]) and (S[m] > S[m+1]):  # (significant) local maximum
                if S[m] > 0.001:  # -60dB above (absolute)
                    threshold = (S[m-2] / 2 + S[m-1] + S[m+1] + S[m+2] / 2) / 3;
                    if S[m] > 2 * threshold:  # 6dB above (relative)
                        # add peak to input buffer
                        peak = dict()
                        peak['t'] = current_time  # (discrete) time
                        peak['f'] = m  # (discrete) frequency
                        buffer[0].append(peak)
                        peak_count = peak_count + 1
        # pairs of peaks
        for cur in buffer[0]:
            for n in range(Moff, M):  # target zone (time)
                for prv in buffer[n]:
                    if abs(cur['f'] - prv['f']) < (350*get_window_size()/get_sampling_rate()):  # +/- 350Hz for the target zone (frequency)
                        pair_count = pair_count + 1
                        if store:
                            table_set(table, prv['t'], prv['f'], cur['t'], cur['f'], song)
                        else:  # query
                            cell = table_get(table, prv['t'], prv['f'], cur['t'], cur['f'])
                            if cell != None:
                                for c in cell:
                                    hits_accumulate(hits, prv['t'], c[1], c[0])
        # shift buffer
        buffer = buffer_shift(buffer)
        # forward...
        current_time = current_time + 1
    file.close()

print ("stats:")
print (" %d frames (%g seconds)" % (current_time, (current_time*get_window_size())/get_sampling_rate()))
print (" ", peak_count, "peaks")
print (" ", pair_count, "pairs")

if store:
    print ("saving database...")
    table_save(table, table_name)
    print (" done")
else:  # query
    song = histograms_max(hits, table['count'], pair_count)
    if song > 0:
        print ("this is song #%d" % song)
    else:
        print ("no result...")

# End Of File

