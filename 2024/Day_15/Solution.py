import os


def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_15/{filename}', 'r') as file:
        contents = file.read()
    return contents