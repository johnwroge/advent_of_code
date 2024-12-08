
import os

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_8/{filename}') as file:
        content = file.read().splitlines()
    return content

def create_grid(lines):
    return [list(line) for line in lines]

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def create_antinode(x, y):
    pass

def print_grid(grid):
    for line in grid:
        print(line, '\n')

def Part_One():
    content = read_file('test.txt')
    grid = create_grid(content)
    positions = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                if grid[i][j] not in positions:
                    positions[grid[i][j]] = []
                positions[grid[i][j]].append((i, j))

    antinode_positions = []
    
    for char in positions.keys():
        possible_nodes = positions[char]
        for i in range(len(possible_nodes)):
            curr = possible_nodes[i]
            for j in range(i + 1, len(possible_nodes)):
                to_check = possible_nodes[j]
                distance = manhattan((curr[0], curr[1]),(to_check[0], to_check[1]))
                print(char, distance)

        # for x, y in to_check:
        #     pass
            
            

    # iterate over each character and determine if there should be an antinode by calculating man distance
        # if true determine posiiton of possible nodes and add to list

    


def Part_Two(grid):
    pass

if __name__ == "__main__":
    print(Part_One())

