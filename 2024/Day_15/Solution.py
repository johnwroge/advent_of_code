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


def Part_One():
    grid, directions = read_file('small.txt')
    directions = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}
    # for line in grid:
    #     print(line, '\n')
        

if __name__ == '__main__':
    pass
    # print(Part_One())
    # print(Part_Two())