
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

def quadrant(r, c):
    if 0 <= c < 50 and 0 <= r < 51:
        return 0
    elif 50 < c < 101  and 0 <= r < 51:
        return 1
    elif 0 <= c < 50 and 51 < r < 103:
        return 2
    elif 50 <= c < 101 and 51 < r < 103:
        return 3

def split_into_quadrants(points):
    quadrants = [[] for _ in range(4)]
    for r, c in points:
        if r != 50 and c != 51:
            index = quadrant(r, c)
            quadrants.append((r,c))
    return quadrants

def next_position(r, c, dr, dc):
    new_r, new_c = r + dr, c + dc
    if 0 <= new_r < 103 and 0 <= new_c < 101:
        return new_r, new_c
    if new_r < 0:
        new_r += 103
    if new_c < 0:
        new_c += 101
    if new_r >= 103:
        new_r -= 103
    if new_c >= 101:
        new_c += 103
    return new_r, new_c   
    
    

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
    pass
    

# print(read_file('test_1.txt'))
    