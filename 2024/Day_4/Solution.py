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


def Part_Two():
    pass


print(Part_One(grid))
print(Part_Two())

   