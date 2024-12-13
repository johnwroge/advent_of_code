
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

def is_whole_number(num):
    return np.isclose(num % 1, 0)

def Part_One():
    coordinates = read_file('test1.txt')
    i = 0
    tokens = 0
    while i < len(coordinates):
        rows = coordinates[i:i + 3] 
        solution = solve(rows[0], rows[1], rows[2])
        if any(round(x, 10) != round(int(x), 10) for x in solution):
            i += 3
            continue
        solution = solution.astype(int)
        print(solution)
        tokens += (3 * int(solution[0])) + int(solution[1])
        i += 3
    return tokens
    


if __name__ == '__main__':
    print(Part_One())

