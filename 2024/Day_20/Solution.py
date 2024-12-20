import os
from collections import deque
import heapq

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
        visited.add((r, c))
        if (r, c) == end:
            return cost
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if (new_r, new_c) in visited:
                continue
            if is_valid(grid, new_r, new_c):
                Q.append((new_r, new_c, cost + 1))
                
    return float('inf')

import os
from collections import deque
import heapq  # Add this import

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    
    pq = [(0, start[0], start[1])]
    visited = set()
    
    while pq:
        dist, r, c = heapq.heappop(pq)
        
        if (r, c) == end:
            return dist
            
        if (r, c) in visited:
            continue
            
        visited.add((r, c))
        
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            new_r, new_c = r + dr, c + dc
            
            if is_valid(grid, new_r, new_c):
                new_dist = dist + 1  
                
                if new_dist < distances[new_r][new_c]:
                    distances[new_r][new_c] = new_dist
                    heapq.heappush(pq, (new_dist, new_r, new_c))
    
    return float('inf')

def find_path_and_cheats(grid, start, end):
    path = []
    current = start
    path.append(current)
    
    while current != end:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        next_moves = set()
        for dr, dc in directions:
            nr, nc = current[0] + dr, current[1] + dc
            if is_valid(grid, nr, nc):
                next_moves.add((nr, nc))
        
        if len(path) >= 2:
            next_moves -= set(path[-2:])
            
        current = next_moves.pop()
        path.append(current)
    
    total = 0
    for i, pos1 in enumerate(path):
        for j, pos2 in enumerate(path[i+102:], i+102):
            manhattan_dist = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
            if manhattan_dist == 2: 
                total += 1
                
    return total

def Part_One():
    grid = read_file('data.txt')
    start, end = get_start_and_end(grid)
    return find_path_and_cheats(grid, start, end)

def Part_Two():
    grid = read_file('data.txt')
    i_n, j_n = len(grid), len(grid[0])
    
    h = []  
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                h = [(i,j)]
            elif cell == 'E':
                end = (i,j)
    
    while h[-1] != end:
        current = h[-1]
        next_moves = {(i,j) for i, j in [
            (current[0], current[1]-1), 
            (current[0], current[1]+1),
            (current[0]-1, current[1]),
            (current[0]+1, current[1])
        ] if i_n>i>=0<=j<j_n and grid[i][j] != '#'}
        h.append((next_moves - set(h[-2:])).pop())
    
    return sum(
        abs(i1-i0)+abs(j1-j0) <= min(20, m+2)  
        for n, (i0, j0) in enumerate(h) 
        for m, (i1, j1) in enumerate(h[n+102:])  
    )

if __name__ == '__main__':
    print(Part_One())
    print(Part_Two())
