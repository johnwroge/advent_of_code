def calculate(char):
    val = ord(char)
    if val >= 97:
        prior = val - 96
        return prior

    else:
        prior = val - 38 
        return prior


# part 1
with open('/Users/johnwroge/advent_of_code/Day3/data.txt', 'r') as file:
    contents = file.read().splitlines()
    sum = 0
    for i in range(len(contents)):
        word = contents[i]
        length = int(len(word)/2) 
        first = word[0:length]
        second = word[length:]
        for char in first:
            if char in second:
                sol = calculate(char)
                sum += sol
                break
# part 2
# with open('/Users/johnwroge/advent_of_code/Day3/data.txt', 'r') as file:
#     contents = file.read().splitlines()
#     sum = 0
#     innerI = 0
#     innerJ = 0
#     results = []
#     while (innerI < len(contents)):
#         list = []
#         while (innerJ < 3):
#             list.append(contents[innerI + innerJ])
#             innerJ += 1
#         innerI += 3
#         innerJ = 0
#         results.append(list)
#     i = 0       
#     while(i < len(results)):
#         first, second, third = results[i]
#         for char in first:
#             if char in second:
#                if char in third:
#                     val = calculate(char)
#                     sum += val 
#                     break
        
#         i += 1 

            


   
    

