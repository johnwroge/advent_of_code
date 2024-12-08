
import os

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_8/{filename}') as file:
        content = file.read().splitlines()
    return content

def create_grid(lines):
    return [list(line) for line in lines]



def Part_One():
    content = read_file('test.txt')
    grid = create_grid(content)
    for line in grid:
        print(line, '\n')

def Part_Two(grid):
    pass

if __name__ == "__main__":
    print(Part_One())

