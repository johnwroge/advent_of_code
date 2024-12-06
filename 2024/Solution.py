import os
import numpy as np



def Read_File(filename):
    with open(os.getcwd() + f'/2024/Day_6/{filename}', 'r') as file:
        lines = file.read().split('\n')
    return lines

def Create_Grid(lines):
    return [list(line) for line in lines]

def Part_One(grid):
   to_add = set()
   dy_dx = {0: (-1, 0), 1: (0, 1), 2: (1,0), 3: (0,-1)}
   directions = ['^', '>', 'v', '<']
   current = '^'
   position = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '^']
   r, c = position[0]
   
   while True:
       index = directions.index(current)
       dy, dx = dy_dx[index]
       to_add.add((r, c))
       
       new_r, new_c = r + dy, c + dx
       if not (0 <= new_r < len(grid) and 0 <= new_c < len(grid[0])):
           break
           
       if grid[new_r][new_c] != '#':
           r, c = new_r, new_c
           continue
               
       temp = directions.index(current) + 1 
       current = directions[temp % 4]
           
   return len(to_add)
        




def main():
    grid_lines = Read_File('data.txt')
    grid = Create_Grid(grid_lines)
    solution1 = Part_One(grid)
    print(solution1)


if __name__ == '__main__':
    main()