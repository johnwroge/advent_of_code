
import os
def read_file(file_name):
    with open(os.getcwd() + f'/2024/day_25/{file_name}', 'r') as file:
        contents = file.read().split('\n\n')
    return contents

def is_lock(grid):
    if all(r == '#' for r in grid[0]):
        return True
    return False

def locks(grid):
    R = len(grid)
    C = len(grid[0])
    line = []
    for i in range(C):
        j = 0
        while grid[j][i] == '#' :
            j += 1
        line.append(j - 1)   
    return line

def keys(grid):
    C = len(grid[0])
    R = len(grid) - 1
    result = []
    for i in range(C):
        count = 0
        for j in range(R, -1, -1):
            if grid[j][i] != '#':
                result.append(count - 1)
                break
            count += 1       
    return result

def create_grid(grid):
    lines = grid.split('\n')
    return [list(line) for line in lines if line]

def fits(lock, key):
    return all(l + k + 2 < 8 for l, k in zip(lock, key)) 

def Solution():
    grids = read_file('data.txt')
    l = []
    k = []
    for grid in grids:
        g = create_grid(grid)
        if is_lock(g):
            l.append(locks(g))
        else:
            k.append(keys(g))
    count = 0
    for lock in l:
        for key in k:
            if fits(lock, key):
                count += 1
    return count

if __name__ == '__main__':
    print(Solution())