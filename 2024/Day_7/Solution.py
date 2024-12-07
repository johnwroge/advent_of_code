import os
import itertools
from functools import lru_cache


def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_7/{filename}', 'r') as file:
        content = file.read().split('\n')
        return content
def format(lines):
    test_values = []
    combine = []
    for line in lines:
        val, row = line.split(':')
        test_values.append(int(val))
        combine.append([int(n) for n in row.split()])
    return test_values, combine


@lru_cache(maxsize=None)
def generate_operators(ops, part_2):
    items = ['*','+']
    if part_2:
        items.append('||')
    combinations = list(itertools.product(items, repeat=ops))
    return combinations

def Part_One(lines):
    file = read_file(lines)
    test_vals, to_combine = format(file)
    result = []
    for i in range(len(test_vals)):
        nums, test_v = to_combine[i], test_vals[i]
        ops = generate_operators(len(to_combine[i]) - 1, False)
        for combination in ops:
            curr =  nums[0]
            i = 1           
            for o in combination:
                if o == '+':
                    curr += nums[i]
                elif o == '*':
                    curr *= nums[i]
                i += 1   
            if curr == test_v:
                result.append(test_v)
                break
    return sum(result)
    

# print(Part_One('test.txt'))
print(Part_One('data.txt'))