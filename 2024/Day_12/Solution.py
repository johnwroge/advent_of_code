import os

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_12/{filename}', 'r') as file:
        contents = file.read().split('\n')
    return contents

def Part_One():
    pass

def Part_Two():
    pass

if __name__ == '__main__':
    print(Part_One())
    print(Part_Two())