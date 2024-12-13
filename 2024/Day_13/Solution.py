
"""
3 tokens to push A button
1 token to push B button

minimize A pushes first 

limit should be 100 presses from either button
"""


import os,re
import numpy as np

def read_file(filename):
    coordinates = []
    with open(os.getcwd() + f'/2024/Day_13/{filename}', 'r') as file:
        for line in file:
            if not line.strip():
                continue
            parts = line.split(':')[1].strip() 
            x_part = parts.split(',')[0].strip()  
            y_part = parts.split(',')[1].strip() if ',' in parts else parts 
            x = int(''.join(c for c in x_part if c.isdigit()))
            y = int(''.join(c for c in y_part if c.isdigit()))
            coordinates.append((x, y))
        
    return coordinates
             
def parse_coordinates_regex(filename):
    coordinates = []
    pattern = r'[XY][+=](\d+)'
    with open(os.getcwd() + f'/2024/Day_13/{filename}', 'r') as file:
        for line in file:
            if not line.strip():
                continue
            numbers = re.findall(pattern, line)
            if len(numbers) == 2:
                coordinates.append((int(numbers[0]), int(numbers[1])))
    return coordinates

def solve(arr1, arr2, arr3):
    try:
        A = np.array([arr1, arr2])
        b = np.array(arr3)
        x = np.linalg.solve(A.T, b)
        return x
    except np.linalg.LinAlgError:
        return None 

def Part_One():
    coordinates = read_file('data.txt')
    i = 0
    total_tokens = 0
    while i < len(coordinates):
        rows = coordinates[i:i + 3]
        solution = solve(rows[0], rows[1], rows[2])
        if solution is not None:
            a, b = solution
            if (0 <= a <= 100 and 0 <= b <= 100 and 
                abs(a - round(a)) < 1e-10 and 
                abs(b - round(b)) < 1e-10):
                a = int(round(a))
                b = int(round(b))
                total_tokens += (3 * a) + b
        i += 3
    return total_tokens

def Part_Two():
    coordinates = read_file('data.txt')
    i = 0
    total_tokens = 0
    while i < len(coordinates):
        rows = coordinates[i:i + 3]
        rows[2] = (rows[2][0] + 10000000000000, rows[2][1] + 10000000000000)
        solution = solve(rows[0], rows[1], rows[2])
        if solution is not None:
            a, b = solution
            if (abs(a - round(a)) < 1e-10 and abs(b - round(b)) < 1e-10):
                a = int(round(a))
                b = int(round(b))
                total_tokens += (3 * a) + b
        i += 3
    return total_tokens




if __name__ == '__main__':
    print('Part 1:', Part_One())
    print('Part 2:', Part_Two())


