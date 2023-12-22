# external representation of a cell (i.e. indices + internal cell)

#def cell_new(idx1, idx2, idx3, time, song):
#    return [ idx1, idx2, idx3, time, song ]

# 3 indices (3-level table)

def cell_idx1(cell):
    return cell[0]

def cell_idx2(cell):
    return cell[1]

def cell_idx3(cell):
    return cell[2]

# 2 internal cell data

# anchor
def cell_time(cell):
    return cell[3]

# index
def cell_song(cell):
    return cell[4]

# import / export

def cell_read(file):
    cell = []
    # read indices + cell itself
    for i in range(3+2):
        data = file.read(2)
        if data == b'':  # End Of File
            return None
        value = int.from_bytes(data, byteorder='little', signed='False')
        cell.append(value)
    return cell

def cell_write(idx1, idx2, idx3, cell, file):
    for value in [ idx1, idx2, idx3, cell[0], cell[1] ]:
        data = value.to_bytes(2, byteorder='little', signed='False')
        file.write(data)
    
# End Of File
