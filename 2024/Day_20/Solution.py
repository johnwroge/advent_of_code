import os
from collections import deque

def read_file(file_name):
    with open(os.getcwd() + f'/2024/Day_20/{file_name}', 'r') as file:
        lines = file.read().split('\n')
    return [list(line) for line in lines]

def print_grid(grid):
    for line in grid:
        print(''.join(line))

def get_start_and_end(grid):
    start = None
    end = None
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if start and end:
                break
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)
    return start, end

def is_valid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != '#'

def bfs(grid, start, end):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    Q = deque([(start[0], start[1], 0)])
    visited = set()
    while Q:
        r, c, cost = Q.popleft()
        if (r, c) == end:
            return cost
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if (new_r, new_c) in visited:
                continue
            if is_valid(grid, new_r, new_c):
                Q.append((new_r, new_c, cost + 1))
                visited.add((new_r, new_c))
        print(Q)
    return float('inf')



def Part_One():
    grid = read_file('small.txt')
    start, end = get_start_and_end(grid)
    time_to_beat = bfs(grid, start, end)
    

if __name__ == '__main__':
    print(Part_One())
