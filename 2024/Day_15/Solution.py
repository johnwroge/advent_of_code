import os

def create_grid(string):
    return [list(row) for row in string if row]

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_15/{filename}', 'r') as file:
        lines = file.readlines()
        if '\n' in lines:
            split_index = lines.index('\n')
            grid = create_grid(''.join(lines[:split_index]).split('\n'))
            instructions = ''.join(lines[split_index+1:]).replace('\n','')
            return grid, instructions
        else:
            return create_grid(''.join(lines).split('\n'))
         

def goods_positioning_system(r, c):
    return (100 * r) + c

def calculate_sum(grid):
    return sum(goods_positioning_system(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 'O')

def find_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '@':
                return r, c

def push_boxes(grid, r, c, dr, dc): 
    indices = []
    curr_r, curr_c = r, c
    
    while grid[curr_r][curr_c] == 'O':
        indices.append((curr_r, curr_c))
        curr_r += dr
        curr_c += dc
    
    if grid[curr_r][curr_c] == '#':
        return False
    
    elif grid[curr_r][curr_c] == '.':
        for old_r, old_c in indices:
            grid[old_r][old_c] = '.'
        
        for old_r, old_c in indices:
            grid[old_r + dr][old_c + dc] = 'O'
        return True

def Part_One():
    grid, path = read_file('data.txt')
    directions = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}
    r, c = find_start(grid)
    grid[r][c] = '.'  
    
    for d in path:
        dr, dc = directions[d]
        new_r, new_c = r + dr, c + dc
        
        if grid[new_r][new_c] == '.':
            grid[r][c] = '.'      
            grid[new_r][new_c] = '@'  
            r, c = new_r, new_c
        elif grid[new_r][new_c] == '#':
            continue
        else:  
            if push_boxes(grid, new_r, new_c, dr, dc):
                grid[r][c] = '.'          
                grid[new_r][new_c] = '@'  
                r, c = new_r, new_c
    return calculate_sum(grid)


def create_new_grid(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for char in row:
            if char == '#':
                new_row.extend(['#', '#'])
            elif char == 'O':
                new_row.extend(['[', ']'])
            elif char == '.':
                new_row.extend(['.', '.'])
            elif char == '@':
                new_row.extend(['@', '.'])
        new_grid.append(new_row)
    return new_grid


def calculate_sum_2(grid):
    return sum(goods_positioning_system(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '[')
   
'''
user modified bfs, store a set and assert horizontal positions. 
'''

def Part_Two():
    old_grid, path = read_file('smaller.txt')
    new_grid = create_new_grid(old_grid)
    directions = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}
    r, c = find_start(new_grid)
    new_grid[r][c] = '.'  
    
    for d in path:
        dr, dc = directions[d]
        new_r = r + dr
        new_c = c + dc
        
    return calculate_sum_2(new_grid)


        
if __name__ == '__main__':
    print(Part_One())
    print(Part_Two())