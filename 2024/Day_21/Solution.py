from collections import deque
from functools import cache
from itertools import pairwise
import os

N_PAD = {
    "0": [("2", "^"), ("A", ">")],
    "1": [("2", ">"), ("4", "^")],
    "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
    "3": [("2", "<"), ("6", "^"), ("A", "v")],
    "4": [("1", "v"), ("5", ">"), ("7", "^")],
    "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
    "6": [("3", "v"), ("5", "<"), ("9", "^")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("5", "v"), ("7", "<"), ("9", ">")],
    "9": [("6", "v"), ("8", "<")],
    "A": [("0", "<"), ("3", "^")]
}

D_PAD = {
    "^": [("A", ">"), ("v", "v")],
    "<": [("v", ">")],
    "v": [("<", "<"), ("^", "^"), (">", ">")],
    ">": [("v", "<"), ("A", "^")],
    "A": [("^", "<"), (">", "v")]
}

PADS = [N_PAD, D_PAD]

def bfs(u, v, g):
    """Find all shortest paths between two positions"""
    q = deque([(u, [])])
    seen = {u}
    shortest = None
    res = []
    
    while q:
        cur, path = q.popleft()
        if cur == v:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                res.append("".join(path + ["A"]))
            continue
        if shortest and len(path) >= shortest:
            continue
            
        for nei, d in g[cur]:
            seen.add(nei)
            q.append((nei, path + [d]))
    return res

@cache
def dfs(seq, level, i=0):
    """Find shortest sequence at given level"""
    g = PADS[i]
    res = 0
    seq = "A" + seq
    
    for u, v in pairwise(seq):
        paths = bfs(u, v, g)
        if level == 0:
            res += min(map(len, paths))
        else:
            res += min(dfs(path, level - 1, 1) for path in paths)
    return res

def read_input(filename):
    with open(os.getcwd() + f'/2024/Day_21/{filename}', 'r') as file:
        return [line.strip() for line in file.readlines()]


def solve(codes, levels=25):  
    total = 0
    for code in codes:
        sequence_length = dfs(code, levels)
        numeric_part = int(''.join(c for c in code if c.isdigit()))
        complexity = sequence_length * numeric_part
        print(f"Code: {code}, Length: {sequence_length}, Numeric: {numeric_part}, Complexity: {complexity}")
        total += complexity
    return total

def main():
    codes = read_input('data.txt')
    print("Processing codes:", codes)
    print("\nPart 1 (2 robots):")
    result1 = solve(codes, 2)
    print(f"Total complexity: {result1}")
    
    print("\nPart 2 (25 robots):")
    result2 = solve(codes, 25)
    print(f"Total complexity: {result2}")

if __name__ == "__main__":
    main()