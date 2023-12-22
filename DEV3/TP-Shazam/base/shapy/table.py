# 3-level (associative-like) table

from os import path

from settings import *
from cell import *

# create new (empty) table
def table_new():
    table = dict()
    # add hit counter (its size is the number of songs stored)
    table['count'] = dict()
    return table

# key (f1, f2, t2-t1)
def make_keys(t1, f1, t2, f2):
    assert(t2 > t1)
    return [ f1, f2, t2-t1 ]

# set table value (time, song)
def table_set_k(table, idx1, idx2, idx3, qtime, song):
    # level 1
    if idx1 in table:
        l1 = table[idx1]
    else:
        l1 = dict()
        table[idx1] = l1
    # level 2
    if idx2 in l1:
        l2 = l1[idx2]
    else:
        l2 = dict()
        l1[idx2] = l2
    # level 3
    # normal mode: forget nothing... (histogram spreads symmetrically)
    if not(idx3 in l2):
        l2[idx3] = list()
    l2[idx3].append([qtime, song])
    # update hit counter (number of peak pairs per song -- for histogram normalization)
    count = table['count']
    if not(song in count):
        count[song] = 0
    count[song] = count[song] + 1

def table_set(table, t1, f1, t2, f2, song):
    [ key1, key2, key3 ] = make_keys(t1, f1, t2, f2)
    table_set_k(table, key1, key2, key3, t1, song)

# get table value (time, song)
def table_get_k(table, idx1, idx2, idx3):
    # level 1
    if idx1 in table:
        l1 = table[idx1]
    else:
        return None
    # level 2
    if idx2 in l1:
        l2 = l1[idx2]
    else:
        return None
    # level 3
    if idx3 in l2:
        return l2[idx3]
    else:
        return None

def table_get(table, t1, f1, t2, f2):
    [ key1, key2, key3 ] = make_keys(t1, f1, t2, f2)
    return table_get_k(table, key1, key2, key3)

# load table from file (by name)
def table_load(name):
    table = table_new()
    if path.exists(name):
        with open(name, "rb") as file:
            while True:
                c = cell_read(file)
                if c == None:  # End Of File
                    break
                idx1 = cell_idx1(c)
                idx2 = cell_idx2(c)
                idx3 = cell_idx3(c)
                song = cell_song(c)
                qtime = cell_time(c)
                table_set_k(table, idx1, idx2, idx3, qtime, song)
            file.close()
    return table

# save file to file (by name)
def table_save(table, name):
    with open(name, "wb") as file:
        for idx1 in table:
            if idx1 == 'count':
                # skip hit counter
                continue
            level1 = table[idx1]
            for idx2 in level1:
                level2 = level1[idx2]
                for idx3 in level2:
                    cells = level2[idx3]
                    for idx in range(len(cells)):
                        cell_write(idx1, idx2, idx3, cells[idx], file)
        file.close()

# get number of songs in table
def table_get_number_of_songs(table):
    return len(table['count'])

# End Of File
