
import os, re
from collections import deque

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
    elif 50 < c < 101 and 51 < r < 103:
        return 3

def split_into_quadrants(points):
    quadrants = [[] for _ in range(4)]
    for r, c in points:
        if r != 51 and c != 50:
            index = quadrant(r, c)
            quadrants[index].append((r,c))
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
        new_c -= 101
    return new_r, new_c   
    
def calculate_safety_factor(q1, q2, q3, q4):
    return len(q1) * len(q2) * len(q3) * len(q4)

def Part_One():
    p_v = read_file('data.txt')
    Q = deque(p_v[0])
    t = 100 
    while t > 0:
        length = len(Q)
        for _ in range(length):
            c, r, dc, dr = Q.popleft()
            new_r, new_c = next_position(r, c, dr, dc)
            Q.append((new_c, new_r, dc, dr))
        t -= 1
    points = [(r, c) for c, r,_ ,_ in Q]
    quadrants = split_into_quadrants(points)
    safety_factor = calculate_safety_factor(quadrants[0], quadrants[1], quadrants[2], quadrants[3])
    
    return safety_factor
    
    

if __name__ == '__main__':
    print(Part_One())
    