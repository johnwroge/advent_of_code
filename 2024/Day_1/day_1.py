

import os 
from collections import Counter

with open(os.getcwd() + '/2024/Day_1/data.txt', 'r') as file:
    lines = file.readlines()
    formatted = [line.split('\n') for line in lines]
    left_distance = []
    right_distance = []
    for line in formatted:
        first, second = line[0].split('   ')
        left_distance.append(int(first))
        right_distance.append(int(second))
    left_distance.sort()
    right_distance.sort()

def part_one():
    total = 0
    for i in range(len(left_distance)):
        total += abs(left_distance[i] - right_distance[i])
    return f"Total difference for Part 1 is {total}"


def part_two():
    similarity_score = 0
    right_count = Counter(right_distance)
    for n in left_distance:
        if n in right_count:
            similarity_score += right_count[n] * n
    return f"Similarity score for Part 2 is {similarity_score}"


print(part_one())
print(part_two())



