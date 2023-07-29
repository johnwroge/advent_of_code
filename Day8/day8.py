rot90 = lambda A: [*map(list, zip(*A[::-1]))]

grid = [[*map(int, x.strip())] for x in open('/Users/johnwroge/advent_of_code/Day8/data.txt')]
part1 = [[0 for _ in x] for x in grid]
part2 = [[1 for _ in x] for x in grid]

for _ in range(4):
    for x,y in [(x,y) for x in range(99) for y in range(99)]:   
        lower = [t < grid[x][y] for t in grid[x][y+1:]]

        part1[x][y] |= all(lower)
        part2[x][y] *= len(lower) if all(lower) else lower.index(0)+1

    grid, part1, part2 = map(rot90, [grid, part1, part2])

print(sum(map(sum, part1)), max(map(max, part2)))


# with open('/Users/johnwroge/advent_of_code/Day8/data.txt', 'r') as file:
#     contents = file.read().splitlines()
#     grid = []
    
#     for i in range(len(contents)):
#         # row = list(contents[i])
#         row = [int(num) for num in contents[i]]
#         grid.append(row)
#     # calculate initial values (lenght and width * 2)
# # count = 2*(len(grid)+len(grid[0])) - 4; 

# visited = {}
   

# def traverse(grid, i, j, direction, current, count):
#     if (grid[i][j] < current or i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])):
#         return count; 

#     if (grid[i][j] > current and not visited.get(f"{i},{j}",True)
#         and i != len(grid) - 1 and j != len(grid[0]) - 1):
#         print(i, j, grid[i][j])
#         visited[f"{i},{j}"] = True
#         count += 1
#     current = max(current, grid[i][j])
    
#     if direction == 'up':
#         return traverse(grid, i - 1, j, direction, current, count)
#     if direction == 'down':
#         return traverse(grid, i + 1, j, direction, current, count)
#     if direction == 'left':
#         return traverse(grid, i, j - 1, direction, current, count)
#     if direction == 'right':
#         return traverse(grid, i, j + 1, direction, current, count)
    
    
# def calculate(grid, count):      
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             visited[f"{i},{j}"] = False; 
#             if (i == 0):
#                 count += 1
#                 count += traverse(grid, i, j, 'down', grid[i][j], 0)
#             if (j == 0):
#                 count += 1
#                 count += traverse(grid, i, j, 'right',grid[i][j], 0)
#             if (i == len(grid) - 1):
#                 count += 1
#                 count += traverse(grid, i, j, 'up', grid[i][j], 0)
#             if (j == len(grid[0]) - 1):
#                 count += 1
#                 count += traverse(grid, i, j, 'left', grid[i][j], 0)
#     return count - 4      
                
# test = [[3,0,3,7,3],[2,0,5,1,2],[6,5,3,3,2],[3,3,5,4,9],[3,5,3,9,0]]
 
# initial = 2*(len(test)+len(test[0])) - 4; 
# # print(traverse(grid, 0, 0 count))
# # print(calculate(test, initial))
# print(calculate(test, 0))
