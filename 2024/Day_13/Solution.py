
"""

Cramer's Rule for an optimized solution that doesn't require using numpy 

https://www.youtube.com/watch?v=jBsC34PxzoM

https://openstax.org/books/college-algebra-2e/pages/7-8-solving-systems-with-cramers-rule

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


def solve_cramers(button_a, button_b, prize):
    a_x, a_y = button_a
    b_x, b_y = button_b
    p_x, p_y = prize
    
    denominator = (a_x * b_y - a_y * b_x)
    if denominator == 0:
        return None
    
    A = (p_x * b_y - p_y * b_x) / denominator
    B = (a_x * p_y - a_y * p_x) / denominator
    
    return (A, B)

def Part_Two():
    coordinates = read_file('data.txt')
    i = 0
    total_tokens = 0
    
    while i < len(coordinates):
        button_a = coordinates[i]
        button_b = coordinates[i + 1]
        prize = list(coordinates[i + 2])
        
        prize[0] += 10000000000000
        prize[1] += 10000000000000
        
        solution = solve_cramers(button_a, button_b, prize)
        
        if solution:
            A, B = solution
            if (A >= 0 and B >= 0 and 
                abs(A - round(A)) < 1e-10 and 
                abs(B - round(B)) < 1e-10):
                A = int(round(A))
                B = int(round(B))
                tokens = (3 * A) + B
                total_tokens += tokens
        
        i += 3
    
    return total_tokens



if __name__ == '__main__':
    print('Part 1:', Part_One())
    print('Part 2:', Part_Two())


