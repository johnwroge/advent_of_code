
import os

def read_file(filename):
    with open(os.getcwd()+f'/2024/Day_11/{filename}', 'r') as file:
        contents = file.read().split()
        return contents


def Part_One():
    contents = read_file('test.txt')
    # contents = read_file('data.txt')
    print(contents)


if __name__ == "__main__":
    print(Part_One())