with open('/Users/johnwroge/advent_of_code/2023/Day1/day1.txt', 'r') as file:
    contents = file.read().splitlines()

# Part 1

def part_1():
    total = 0
    for line in contents:
        num = ''
        for c in line:
            if c.isnumeric():
                num += c

        val = num[0] + num[len(num) - 1] 
        total += int(val)
    return total


tests_2 = [
    'two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen',
]

import re

t = 0

number = "one two three four five six seven eight nine".split()

pattern = "(?=(" + "|".join(number) + "|\\d))"

# https://www.regular-expressions.info/lookaround.html

def f(x):
    if x in number:
        return str(number.index(x) + 1)
    return x
for x in contents:
    digits = [*map(f, re.findall(pattern, x))]
    t += int(digits[0] + digits[-1])
print(t)

