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


In this schematic, two numbers are not part numbers because they are not adjacent to a 
symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol
and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part 
numbers in the engine schematic?


'''


with open('/Users/johnwroge/advent_of_code/2023/Day3/day3_test.txt', 'r') as file:
    contents = file.read().splitlines()

symbols = set()
symbols.add('+')
symbols.add('/')
symbols.add('=')
symbols.add('*')


symbols.add('$')
symbols.add('#')
symbols.add('%')
symbols.add('@')
symbols.add('&')
symbols.add('%')


grid = []
for line in contents:
    row = []
    for char in line:
        row.append(char)
    grid.append(row)
print(grid)





 
