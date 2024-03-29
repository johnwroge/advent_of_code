'''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). 
The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green
 cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag 
contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been
loaded with that configuration. However, game 3 would have been impossible because
at one point the Elf showed you 20 red cubes at once; similarly, game 4 would 
also have been impossible because the Elf showed you 15 blue cubes at once. 
If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with 
only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the 
IDs of those games?

'''


with open('/Users/johnwroge/advent_of_code/2023/Day2/day2.txt', 'r') as file:
    contents = file.read().splitlines()

days = { n: [] for n in range(1, 101)}

new_list = []
for i in range(0, 100):
    days[i + 1].append(contents[i].split(':')[1])
   
for key in days:
    value = days[key][0]
    games = value.split(';')

    for game in games:
        color_count_pairs = game.strip().split(',')
        # print(color_count_pairs)
        for pair in color_count_pairs:
  
            count, color = pair.strip().split()
           
            count_number = int(count)
            if color == 'red' and int(count) > 12:
                days[key] = False
                break
            elif color == 'green' and int(count) > 13:
                days[key] = False
                break
            elif color == 'blue' and int(count) > 14:
                days[key] = False
                break
        if not days[key]:
            break 
total = 0
right_total = 0
for i in range(len(days)):
    if not days[i + 1]:
        total += i + 1
    else:
        right_total += i + 1

# part 2

import numpy as np

days2 = { n: [] for n in range(1, 101)}
for i in range(0, 100):
    days2[i + 1].append(contents[i].split(':')[1])
result = []
for key in days2:
    value = days2[key][0]
    games = value.split(';')
    blue, green, red = 0,0,0

    for i, game in enumerate(games):
        color_count_pairs = game.strip().split(',')
        for j, pair in enumerate(color_count_pairs):
            
            count, color = pair.strip().split()
            
            count_number = int(count)
            if color == 'red':
                red = max(red, count_number)  
            elif color == 'green':
                green = max(green, count_number)   
            elif color == 'blue':
                blue = max(blue, count_number)

    result.append([blue, green, red])

# print(result)
final = [np.prod(arr) for arr in result]
final_result = sum(final)
print(final_result)





    
    



    
    

