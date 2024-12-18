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

def Part_Two():
    grid = create_grid(71, 71)
    bytes = read_file('data.txt')
    for i in range(len(bytes)):
        c, r = bytes[i]
        grid[r][c] = '#'
        if not shortest_path(grid, (0,0),(70, 70)):
            return r, c 

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def is_valid_a_star(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != '#'

def a_star(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    open_set = [(manhattan_distance(start, end), 0, start)]
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        _, current_g, current = heapq.heappop(open_set)
        
        if current == end:
            return current_g  
            
        for dx, dy in directions:
            new_r, new_c = current[0] + dx, current[1] + dy
            neighbor = (new_r, new_c)
            
            if not is_valid_a_star(new_r, new_c, grid):
                continue
                
            tentative_g = current_g + 1
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbor, end)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))
    
    return None  

                
if __name__ == '__main__':
    print(Part_One())    
    print(Part_Two())
