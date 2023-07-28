30373
25512
65332
33549
35390


with open('/Users/johnwroge/advent_of_code/Day8/data.txt', 'r') as file:
    contents = file.read().splitlines()
    grid = []
    total = 0
    for i in range(len(contents)):
        row = list(contents[i])
        grid.append(row)
    # calculate initial values (lenght and width * 2)
    total += 2*(len(grid)+len(grid[0]))
    
    def traverse(grid, row, col, curr):
        if (i <= 0 and j <= 0 and i >= len(grid) - 1 and j >= len(grid[0]) - 1):
            return True
        if (grid[row][col] > curr):
            return False
       
        
        
        if (traverse(grid, row + 1, col, curr) or traverse(grid, row - 1, col, curr) or
             traverse(grid, row, col + 1, curr) or traverse(grid, row, col - 1, curr)):
             return True

        return False



    # iterate over the rows and columns
    # row
    for i in range(len(grid)):
        # col
        for j in range(len(grid[0])):
            if (i != 0 and j != 0 and i != len(grid) - 1 and j != len(grid[0]) - 1):
                if (traverse(grid, i, j, grid[i][j])):
                    total += 1
   




        