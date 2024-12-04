import os

with open(os.getcwd() + '/2024/Day_4/data.txt') as file:
    content = file.read().split('\n')
    grid = [list(row) for row in content]

def Part_One(grid):
    rows = len(grid)
    cols = len(grid[0])
    matches = []
    target = "XMAS"

    for row in range(rows):
        for col in range(cols - 3):
            sequence = ''.join(grid[row][col + i] for i in range(4))
            if sequence == target:
                matches.append(("horizontal-right", (row, col)))

    for row in range(rows):
        for col in range(3, cols):
            sequence = ''.join(grid[row][col - i] for i in range(4))
            if sequence == target:
                matches.append(("horizontal-left", (row, col)))

    for row in range(rows - 3):
        for col in range(cols):
            sequence = ''.join(grid[row + i][col] for i in range(4))
            if sequence == target:
                matches.append(("vertical-down", (row, col)))

    for row in range(3, rows):
        for col in range(cols):
            sequence = ''.join(grid[row - i][col] for i in range(4))
            if sequence == target:
                matches.append(("vertical-up", (row, col)))

    for row in range(rows - 3):
        for col in range(cols - 3):
            sequence = ''.join(grid[row + i][col + i] for i in range(4))
            if sequence == target:
                matches.append(("down-right", (row, col)))

    for row in range(rows - 3):
        for col in range(3, cols):
            sequence = ''.join(grid[row + i][col - i] for i in range(4))
            if sequence == target:
                matches.append(("down-left", (row, col)))

    for row in range(3, rows):
        for col in range(cols - 3):
            sequence = ''.join(grid[row - i][col + i] for i in range(4))
            if sequence == target:
                matches.append(("up-right", (row, col)))

    for row in range(3, rows):
        for col in range(3, cols):
            sequence = ''.join(grid[row - i][col - i] for i in range(4))
            if sequence == target:
                matches.append(("up-left", (row, col)))

    return len(matches)


def Part_Two(grid):
    rows = len(grid)
    cols = len(grid[0])
    matches = []
    
    def check_diagonal_mas(row, col):
        found = []
        if row < rows-2 and col < cols-2:
            if (grid[row][col] == 'M' and 
                grid[row+1][col+1] == 'A' and 
                grid[row+2][col+2] == 'S'):
                found.append(('down-right', (row, col)))
        
        if row < rows-2 and col >= 2:
            if (grid[row][col] == 'M' and 
                grid[row+1][col-1] == 'A' and 
                grid[row+2][col-2] == 'S'):
                found.append(('down-left', (row, col)))
                
        if row >= 2 and col < cols-2:
            if (grid[row][col] == 'M' and 
                grid[row-1][col+1] == 'A' and 
                grid[row-2][col+2] == 'S'):
                found.append(('up-right', (row, col)))
                
        if row >= 2 and col >= 2:
            if (grid[row][col] == 'M' and 
                grid[row-1][col-1] == 'A' and 
                grid[row-2][col-2] == 'S'):
                found.append(('up-left', (row, col)))
        
        return found

    all_mas = []
    for row in range(rows):
        for col in range(cols):
            diagonals = check_diagonal_mas(row, col)
            all_mas.extend(diagonals)
    
    intersections = []
    for i, (dir1, pos1) in enumerate(all_mas):
        for dir2, pos2 in all_mas[i+1:]:
            if dir1 == 'down-right':
                a1_row, a1_col = pos1[0]+1, pos1[1]+1
            elif dir1 == 'down-left':
                a1_row, a1_col = pos1[0]+1, pos1[1]-1
            elif dir1 == 'up-right':
                a1_row, a1_col = pos1[0]-1, pos1[1]+1
            else: 
                a1_row, a1_col = pos1[0]-1, pos1[1]-1
                
            if dir2 == 'down-right':
                a2_row, a2_col = pos2[0]+1, pos2[1]+1
            elif dir2 == 'down-left':
                a2_row, a2_col = pos2[0]+1, pos2[1]-1
            elif dir2 == 'up-right':
                a2_row, a2_col = pos2[0]-1, pos2[1]+1
            else: 
                a2_row, a2_col = pos2[0]-1, pos2[1]-1
                
            if a1_row == a2_row and a1_col == a2_col:
                intersections.append((dir1, pos1, dir2, pos2))
    
    return len(intersections)


# print(Part_One(grid))
# print(Part_Two(grid))

   