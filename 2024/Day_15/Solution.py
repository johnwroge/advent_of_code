import os


def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_15/{filename}', 'r') as file:
        text = file.read()
    lines = text.splitlines()
    first_part = '\n'.join(lines[:len(lines)//2]).split('\n')
    grid = [list(row) for row in first_part]
    second_part = '\n'.join(lines[len(lines)//2:]).replace('\n','') 
    return grid, second_part


def Part_One():
    grid, directions = read_file('test.txt')
    for line in grid:
        print(line, '\n')
        

if __name__ == '__main__':
    print(Part_One())
    # print(Part_Two())