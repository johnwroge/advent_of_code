
# find the sum 20th, 60th, 100th, 140th, 180th, and 220th cycles.
# 20 * current + 60 * current... + 220 * current
import os
from collections import deque

with open(os.getcwd() + '/2022/Day10/part_one.txt', 'r') as f:
    items = f.read().strip().split('\n')
    
with open(os.getcwd() + '/2022/Day10/part_two.txt', 'r') as f:
    items_2 = f.read().strip().split('\n')

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


def solve_crt_display(instructions):
    x_register = 1
    cycle = 0
    crt_display = []
    
    def draw_pixel():
        nonlocal cycle
        cycle += 1
        
        pixel_position = (cycle - 1) % 40

        if abs(pixel_position - x_register) <= 1:
            crt_display.append('#')
        else:
            crt_display.append('.')
    
    for instruction in instructions:
        instruction = instruction.strip()
        
        if instruction == "noop":
            draw_pixel()
        elif instruction.startswith("addx"):
            value = int(instruction.split()[1])
            draw_pixel() 
            draw_pixel()  
            x_register += value  
    
    display_lines = []
    for row in range(6):
        start_idx = row * 40
        end_idx = start_idx + 40
        display_lines.append(''.join(crt_display[start_idx:end_idx]))
    for line in display_lines:
        print(line)
    
    return 


    
print(f"Part 1: {solve_cathode_ray_tube(items)}")
print(f"Part 2: {solve_crt_display(items_2)}")
