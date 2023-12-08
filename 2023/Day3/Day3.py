'''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

1,1 

if i > 0 and grid[i - 1] 
if i < len(grid) - 1 and grid[i + 1] 

if i < len(grid) - 1 and j < len(grid[0] - 1) and  


In this schematic, two numbers are not part numbers because they are not adjacent to a 
symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol
and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part 
numbers in the engine schematic?
'''

            

import math as m, re

board = list(open('/Users/johnwroge/advent_of_code/2023/Day3/day3.txt'))

chars = {(r, c): [] for r in range(140) for c in range(140) if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1) for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(sum(sum(p)    for p in chars.values()), sum(m.prod(p) for p in chars.values() if len(p)==2))