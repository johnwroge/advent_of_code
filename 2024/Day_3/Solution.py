import os
import re

with open(os.getcwd() + '/2024/Day_3/data.txt') as file:
    content = file.read()
    instructions = file.readlines()
   

def Part_One(content):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.finditer(pattern, content)
    total = 0
    for match in matches:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        product = num1 * num2
        total += product
    return print(f"Total sum for part 1: {total}")
    

def Part_Two(content):
    pattern = r"(?:mul\((\d+),(\d+)\)|do\(\)|don't\(\))"
    enabled = True 
    total = 0
    for match in re.finditer(pattern, content):
        operation = match.group(0)
        if operation == "do()":
            enabled = True
        elif operation == "don't()":
            enabled = False
        elif enabled and operation.startswith("mul"):
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            product = num1 * num2
            total += product     
    return print(f"Total sum for part 2: {total}")
            
Part_One(content)
Part_Two(content)




    

