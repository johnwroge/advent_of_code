
import os

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_8/{filename}') as file:
        content = file.read().splitlines()
    return content

def create_grid(lines):
    return [list(line) for line in lines]

def get_distance(a, b):
    return [b[0] - a[0], b[1] - a[1]]
    
def create_antinodes(position, dist):
    pass

def print_grid(grid):
    for line in grid:
        print(line, '\n')

def Part_One():
    content = read_file('test.txt')
    test = read_file('to_check.txt')
    grid = create_grid(content)
    positions = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                if grid[i][j] not in positions:
                    positions[grid[i][j]] = []
                positions[grid[i][j]].append((i, j))

    anti_nodes = set()
    
    for char in positions.keys():
        possible_nodes = positions[char]
        for i in range(len(possible_nodes)):
            curr = possible_nodes[i]
            for j in range(i + 1, len(possible_nodes)):
                to_check = possible_nodes[j]
                dy1, dx1 = get_distance(curr, to_check)
                dy2, dx2 = get_distance(to_check, curr)
                anti_nodes.add((to_check[0] + dy1, to_check[1] + dx1))
                anti_nodes.add((curr[0] + dy2, curr[1] + dx2))
    result = 0                       
    for x, y in anti_nodes:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            result += 1
    return result
            

    


def Part_Two(grid):
    pass

if __name__ == "__main__":
    print(Part_One())

