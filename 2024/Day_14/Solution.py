
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

def quadrant(r, c):
    # first
    # second
    # third
    # fourth
    pass

def split_into_quadrants():
    # first, second, third, fourth
    # iterate over points, determine which quadrant and append
    # filter first
    # filter second
    # filter third
    # filter fourth
    # return all quadrants
    pass

def next_position(r, c):
    # return new_r, new_c
    pass

def validate_position()

def Part_One():
    # get initial points and velocities
    # append to a deque
    # perform bfs while time (100) > 0
        # iterate over the entire queue length
            # get position and velocity and determine next position
            # append to the queue
    
    # get qudrants (split into quadrants)
    # iterate over qudrants and calculate the safety factor
    # return safety factor
    
    



# print(read_file('test_1.txt'))
    