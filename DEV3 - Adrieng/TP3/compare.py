import random
import string

ln = list()
lm = list()

d = dict()

def search_list(name):
    return lm[ln.index(name)]

def search_dict(name):
    return d[name]

def insert_both(name,mark):
    ln.append(name)
    lm.append(mark)
    d[name] = mark

def get_random_name(lenth):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(lenth))

def get_random_mark():
    return random.randint(0,20)

def insert_both_random_elements(n):
    for _ in range(n):
        name = get_random_name(8)
        mark = get_random_mark()
        insert_both(name,mark)

import time_profiler

from memory_profiler import profile

#@profile
def search_both_all_names():
    for name in ln:
        note1 = search_list(name)
        note2 = search_dict(name)
        assert(note1 == note2)

for _ in range(2):
    insert_both_random_elements(10000)
    time_profiler.start()
    search_both_all_names()
    time_profiler.stop()



