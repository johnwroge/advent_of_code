
import os
from functools import lru_cache

def read_file(filename):
    with open(os.getcwd()+f'/2024/Day_11/{filename}', 'r') as file:
        contents = file.read().split()
        return contents
# brute force
def Part_One(blinks):
    contents = read_file('data.txt')
    while blinks > 0:
        curr = []
        for i in range(len(contents)):
            stone = contents[i]
            length = len(stone)
            if stone == '0':
                curr.append('1')
            elif length % 2 == 0:
                first = str(int(stone[:length//2],base=10))
                second = str(int(stone[length//2:],base=10))
                curr.extend([first, second])
            else: 
                num = int(stone) * 2024
                curr.append(str(num))
        contents = curr
        blinks -= 1
    return len(contents)

# Recursive and Caching
def Part_Two(blinks):
    contents = read_file('data.txt')
    total = 0
    for stone in contents:
        total += process_stone(stone, blinks)
    return total

@lru_cache(maxsize=None)
def process_stone(stone, blinks):
    if blinks == 0:
        return 1
    
    length = len(stone)

    if stone == '0':
        return process_stone('1', blinks - 1)
    elif length % 2 == 0:
        first = str(int(stone[:length//2], base=10))
        second = str(int(stone[length//2:], base=10))
        return process_stone(first, blinks - 1) + process_stone(second, blinks - 1)
    else:
        num = str(int(stone) * 2024)
        return process_stone(num, blinks - 1)
    

if __name__ == "__main__":
    print('Part 1:', Part_Two(75))
    # print('Part 1:', Part_One(25))