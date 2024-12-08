
import os

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_8/{filename}') as file:
        content = file.read().splitlines()
    return content

def create_grid(lines):
    return [list(line) for line in lines]

def get_distance(a, b):
    return [b[0] - a[0], b[1] - a[1]]

def print_grid(grid):
    for line in grid:
        print(' '.join(line))

def Part_One():
    content = read_file('data.txt')
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

def Part_Two():
    content = read_file('data.txt')
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
                p1 = to_check[0] + dy1
                p2 = to_check[1] + dx1
                while 0 <= p1 < len(grid) and 0 <= p2 <= len(grid[0]):
                    anti_nodes.add((p1, p2))
                    p1 += dy1
                    p2 += dx1
                p3 = curr[0] + dy2
                p4 = curr[1] + dx2
                while 0 <= p3 < len(grid) and 0 <= p4 <= len(grid[0]):
                    anti_nodes.add((p3, p4))
                    p3 += dy2
                    p4 += dx2
                
    result = 0                       
    for x, y in anti_nodes:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            grid[x][y] = "#"

    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != '.':
                result += 1
    
    return result

if __name__ == "__main__":
    print('Part 1:', Part_One())
    print('Part 2:', Part_Two())

