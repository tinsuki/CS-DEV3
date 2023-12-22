def hits_new(songs):
    hits = list()
    for s in range(songs):
        data = list()
        hits.append(data)
    return hits

def hits_accumulate(hits, ref_time, song, time):
    data = hits[song-1]
    data.append([ref_time, time])

def hits_range(hits):
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    for s in range(len(hits)):
        data = hits[s]
        for p in data:
            xmin = min([xmin, p[0]])
            xmax = max([xmax, p[0]])
            ymin = min([ymin, p[1]])
            ymax = max([ymax, p[1]])
    return [ xmin, xmax, ymin, ymax ]

def hits_delta_range(hits):
    dmax = 0
    for s in range(len(hits)):
        data = hits[s]
        for p in data:
            dmax = max([dmax, abs(p[1]-p[0])])
    return dmax

# End Of File
 
