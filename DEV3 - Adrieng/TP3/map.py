import compare 
from memory_profiler import profile
 
m = list()

def map_new():
    for _ in  range(2**16):
        m.append(dict())

map_new()

def map_hash(name):
    h = hash(name) # hachage de name qui retourne un entier sur 64 bit
    if(h < 0): # si cet entier est négatif on le passe en positif
        h = 2**64 + h
    return h & 0xffff # l'entier en passant tout les bit entre le 17ieme et le 64ieme à 0

def map_insert(map,name,mark):
    h = map_hash(name)
    map[h][name] = mark

d = dict()

def insert_both(name, mark):
    d[name] = mark
    map_insert(m,name,mark)

@profile
def insert_both_random_elements(n):
    for _ in range(n):
        name = compare.get_random_name(8)
        mark = compare.get_random_mark()
        insert_both(name,mark)



def search_dict(name):
    return d[name]

def search_map(name):
    h = map_hash(name)
    d = m[h]
    return d[name]

@profile
def search_both_all_names():
    for name in d.keys():
        note1 = search_dict(name)
        note2 = search_map(name)
        assert(note1 == note2)

import time_profiler

for _ in range(2):
    insert_both_random_elements(20000)
    time_profiler.start()
    search_both_all_names()
    time_profiler.stop()


print("map = "+str(len(m)), "dict = "+str(len(d)), sep='\n')
