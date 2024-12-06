import os



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

def Part_Two(grid):
   def simulate(test_grid, r, c):
       dy_dx = {0: (-1, 0), 1: (0, 1), 2: (1,0), 3: (0,-1)}
       directions = ['^', '>', 'v', '<']
       current = '^'
       visited = set()
       
       while True:
           state = (r, c, current)
           if state in visited:
               return True
           visited.add(state)
           
           index = directions.index(current)
           dy, dx = dy_dx[index]
           new_r, new_c = r + dy, c + dx
           
           if not (0 <= new_r < len(test_grid) and 0 <= new_c < len(test_grid[0])):
               return False
               
           if test_grid[new_r][new_c] != '#':
               r, c = new_r, new_c
               continue
                   
           current = directions[(directions.index(current) + 1) % 4]

   start = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '^'][0]
   cycles = 0
   
   for i in range(len(grid)):
       for j in range(len(grid[0])):
           if grid[i][j] == '.' and (i,j) != start:
               test_grid = [row[:] for row in grid]
               test_grid[i][j] = '#'
               if simulate(test_grid, start[0], start[1]):
                   cycles += 1
                   
   return cycles


def main():
    grid_lines = Read_File('data.txt')
    grid = Create_Grid(grid_lines)
    solution1 = Part_One(grid)
    print('Part 1 :', solution1)
    solution2 = Part_Two(grid)
    print('Part 2 :', solution2)


if __name__ == '__main__':
    main()

