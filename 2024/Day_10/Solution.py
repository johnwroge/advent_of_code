import os
from collections import deque

def read_file(file):
    with open(os.getcwd() + f'/2024/Day_10/{file}', 'r') as file:
        content = file.read().split('\n')
    grid = [list(row) for row in content]
    return grid
    
def print_grid(grid):
    for line in grid:
        print(line, '\n')
def is_valid(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])



def Part_One():
    grid = read_file('test2.txt')
    Q = deque()
    score = {}
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '0':
                Q.append((i, j, 0, i, j))
    
    dr_dc = [(0,1),(0,-1),(1,0),(-1,0)]

    while Q:
        i, j, curr, r, c = Q.popleft()
        visited.add((r,c))
        if curr == 9:
            if (i,j) not in score:
                score[(i, j)] = 0
            score[(i, j)] += 1
            continue
        for dr, dc in dr_dc:
            new_r, new_c = r + dr, c + dc
            if (new_r, new_c) not in visited and is_valid(grid, new_r, new_c) and grid[new_r][new_c] != '.' and int(grid[new_r][new_c]) == curr + 1:
                Q.append((i, j, curr + 1, new_r, new_c))
    print(visited)
    return sum(score.values())
    
    



def Part_Two():
    pass




if __name__ == "__main__":
    print(Part_One())
    # print(Part_Two())
