
import os, re

def read_file(file):
    coordinates = []
    pattern = r'p=(\d+),(\d+)\s+v=(-?\d+),(-?\d+)'
    maximum = 0
    with open(os.getcwd() + f'/2024/Day_14/{file}', 'r') as file:
        for line in file:
            group = []
            matches = re.search(pattern, line)
            if matches:
                p1, p2 = matches.group(1), matches.group(2)
                v1, v2 = matches.group(3), matches.group(4)
                coordinates.append((int(p1), int(p2), int(v1), int(v2)))
            maximum = max(int(p2), maximum)
    return list(coordinates), maximum

def create_grid(maxi):
    return []

# print(read_file('test_1.txt'))
    