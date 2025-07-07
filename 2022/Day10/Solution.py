
# find the sum 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# 20 * current + 60 * current... + 220 * current
import os
from collections import deque

with open(os.getcwd() + '/2022/Day10/part_one.txt', 'r') as f:
    items = f.read().strip().split('\n')
    
    

def solve_cathode_ray_tube(instructions):
    x_register = 1
    cycle = 0
    signal_strengths = []
    target_cycles = {20, 60, 100, 140, 180, 220}
    
    def check_signal_strength():
        if cycle in target_cycles:
            signal_strengths.append(cycle * x_register)
    
    for instruction in instructions:
        if instruction.strip() == "noop":
            cycle += 1
            check_signal_strength()
        elif instruction.strip().startswith("addx"):
            value = int(instruction.strip().split()[1])
            cycle += 1
            check_signal_strength()
            cycle += 1
            check_signal_strength()
            x_register += value
    
    return sum(signal_strengths)

    
    
print(f"Part 1, answer: {solve_cathode_ray_tube(items)}")
