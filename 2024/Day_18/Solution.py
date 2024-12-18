import os
import heapq
from collections import deque

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_18/{filename}', 'r') as file:
        contents = file.read().split('\n')
    return [list(map(int,row.split(','))) for row in contents]

def create_grid(r, c):
    return [['.' for _ in range(c)] for _ in range(r)]

def print_grid(grid):
    for line in grid:
        print(''.join(line))
def is_valid(r, c, grid, visited):
    return (r,c) not in visited and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != '#'

def visualize(grid, path):
    for y, x in path:
        grid[y][x] = 'O'
    print_grid(grid)

def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    visited = {start}
    Q = deque([(start, 0)])
    
    while Q:
        (row, col), path = Q.popleft()
        if (row, col) == end:
            # visualize(grid, path)
            return path
        for dx, dy in directions:
            new_r, new_c = row + dx, col + dy
            if is_valid(new_r, new_c, grid, visited):
                Q.append(((new_r, new_c), path + 1))
                visited.add((new_r, new_c))
    return None

def Part_One():
    grid = create_grid(71, 71)
    bytes = read_file('data.txt')
    for i in range(1024):
        c, r = bytes[i]
        grid[r][c] = '#'
    return shortest_path(grid, (0,0),(70,70))
    
                

    

print(Part_One())