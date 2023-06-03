

with open('/Users/johnwroge/advent_of_code/Day1/data.txt', 'r') as file:
    contents = file.read().splitlines()
    # Process the contents of the file
    current = 0
    maximum = 0
    sums = []
    for i in range(len(contents)):
        if contents[i] == "":
            maximum = max(maximum, current)
            sums.append(current)
            current = 0
        else:
            current += int(contents[i])
    sums.sort(reverse=True)
    print(sums[0]+ sums[1] + sums[2])
      