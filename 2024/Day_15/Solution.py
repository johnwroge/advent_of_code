import os


def create_grid(string):
    return [list(row) for row in string if row]

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_15/{filename}', 'r') as file:
        lines = file.readlines()
        if '\n' in lines:
            split_index = lines.index('\n')
            grid = create_grid(''.join(lines[:split_index]).split('\n'))
            instructions = ''.join(lines[split_index+1:])
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

def push_boxes(grid, r, c):
    # How many O's are consecutive after your position
    # Is there a dot at the end of the O sequence
    # Is there a wall blocking the move  
    # 
     
    # Can I make this move? (check the conditions)
    # How many O's am I pushing?
    # Where does everything end up? 
    pass


def Part_One():
    grid, path = read_file('small.txt')
    directions = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}
    r, c = find_start(grid)
    
    for c in path:
        dr, dc = directions[path]
        new_r, new_c = r + dr, c + dc
        if grid[new_r][new_c] == '.':
            r, c = new_r, new_c
        elif grid[new_r][new_c] == '#':
            continue
        else:
            pass

        
       
        

if __name__ == '__main__':
    print(Part_One())
    # print(Part_Two())