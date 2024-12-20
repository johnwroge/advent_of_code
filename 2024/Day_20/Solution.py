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

def bfs(grid, start, end):


def Part_One():
    grid = read_file('small.txt')
    start, end = get_start_and_end(grid)
    print(start, end)
    

if __name__ == '__main__':
    print(Part_One())
