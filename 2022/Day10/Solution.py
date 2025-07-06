
# find the sum 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# 20 * current + 60 * current... + 220 * current
import os
from collections import deque

with open(os.getcwd() + '/2022/Day10/part_one.txt', 'r') as f:
    items = f.read().strip().split('\n')
    input = [item.split(' ') for item in items]
    
print(f"Part 1, answer: {input}")