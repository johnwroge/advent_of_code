import os

def read_file(file):
    with open(os.getcwd() + f'/2024/Day_16/{file}', 'r') as file:
        content = file.read().splitlines()
    return [list(line) for line in content]

def print_grid(grid):
    for line in grid:   
        print(''.join(line))
        
def Part_One():
    grid  = read_file('small.txt')
    
           
if __name__ == "__main__":
    print(Part_One())