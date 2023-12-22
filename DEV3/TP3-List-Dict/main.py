import matplotlib.pyplot as plt
import time_profiler as tp
from time import sleep, time
from random import randint, choice
from string import ascii_lowercase


global names, ln, lm, d
names = {}
def getRandomName():
    return ''.join(choice(ascii_lowercase) for i in range(randint(5, 10)))

def getRandomMark():
    return randint(0, 20)

def searchList(name):
    return lm[ln.index(name)]

def searchDict(name):
    global d
    return d[name]

def insertBoth(name, mark):
    ln.append(name)
    lm.append(mark)
    d[name] = mark

def insertList(name, mark):
    ln.append(name)
    lm.append(mark)

def insertDict(name, mark):
    d[name] = mark

def updateList(name, mark):
    lm[ln.index(name)] = mark

def fillList(n):
    for i in range(n):
        name = getRandomName()
        mark = getRandomMark()
        try:
            names[name] += 1
            updateList(name, mark)
        except KeyError:
            names[name] = 1
            insertList(name, mark)
        insertDict(name, mark)

ln = []
lm = []
d = {}

fillList(10000)

print("_"*50)
print("Partie 1: comparaison de la recherche dans une liste et dans un dictionnaire")
print("_"*50)
print("Temps cumulé pour 10000 recherches dans une liste et dans un dictionnaire")

part1_list = []
part1_dict = []
start = 0

tp.start()
for name in ln:
    start = time()
    out1 = searchList(name)
    part1_list.append(time() - start)
    start = time()
    out2 = searchDict(name)
    part1_dict.append(time() - start)
    assert out1 == out2, "Error"
tp.stop()
print("_"*50)

print("Temps cumulé pour 10000 recherches dans une liste")
tp.start()
for name in ln:
    out1 = searchList(name)
tp.stop()
print("_"*50)

print("Temps cumulé pour 10000 recherches dans un dictionnaire")
tp.start()
for name in ln:
    out2 = searchDict(name)
tp.stop()
print("_"*50)

plt.plot(part1_list, label="List")
plt.plot(part1_dict, label="Dict")
plt.legend()
plt.show()

def map_new():
    return [{} for _ in range(2**16)]

def map_insert(m, name, mark):
    m[map_hash(name)][name] = mark

def insert_both(m, name, mark):
    map_insert(m, name, mark)
    d[name] = mark


def map_hash(name):
    h = hash(name)
    if h < 0:
        h = 2**64 + h
    return h & 0xffff

def fillMap(n, m):
    for i in range(n):
        name = getRandomName()
        mark = getRandomMark()
        insert_both(m, name, mark)

def searchMap(m, name):
    return m[map_hash(name)][name]

sleep(2)
print("_"*50)
print("Partie 2 : comparaison de dictionnaire et de tableau associatif")
print("_"*50)

m = map_new()
d = {}
names = {}

fillMap(20000, m)

print("Taille de la map: ", len(m))
print("Taille du dictionnaire: ", len(d))

part2_map = []
part2_dict = []

print("Temps cumulé pour 20000 recherches dans une map")
tp.start()
for name in d.keys():
    start = time()
    out = searchMap(m, name)
    part2_map.append(time() - start)
tp.stop()
print("_"*50)

print("Temps cumulé pour 20000 recherches dans un dictionnaire")
tp.start()
for name in d.keys():
    start = time()
    out = d[name]
    part2_dict.append(time() - start)
tp.stop()
print("_"*50)

plt.plot(part2_map, label="Map")
plt.plot(part2_dict, label="Dict")
plt.legend()
plt.show()



