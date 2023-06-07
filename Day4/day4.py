with open('/Users/johnwroge/advent_of_code/Day4/data.txt', 'r') as file:
    contents = file.read().splitlines()
    sum = 0
    # for i in range(len(contents)):
    #     info = contents[i]
    #     item = info.split(",")
    #     one, two = item
    #     first = one.split('-')
    #     second = two.split('-')
    #     range1Start = int(first[0])
    #     range1End = int(first[1])
    #     range2Start = int(second[0])
    #     range2End = int(second[1])
    #     if (range1Start >= range2Start and range1End <= range2End) or (range2Start >= range1Start and range1End >= range2End):
    #         sum +=1
    # for i in range(len(contents)):
    #     info = contents[i]
    #     item = info.split(",")
    #     one, two = item
    #     first = one.split('-')
    #     second = two.split('-')
    #     result = []
    #     for number in first:
    #         digits = [int(digit) for digit in number]
    #         result.extend(digits)
    #     print(result)


    #     result2 = []
    #     for number in second:
    #         digits2 = [int(digit) for digit in number]
    #         result2.extend(digits)
    for i in range(len(contents)):
        info = contents[i]
        item = info.split(",")
        one, two = item
        first = one.split('-')
        second = two.split('-')
        range1Start = int(first[0])
        range1End = int(first[1])
        range2Start = int(second[0])
        range2End = int(second[1])
        # (2-4,6-8 and 2-3,4-5)
        if ((range1Start <= range2Start) and (range1End >= range2Start)) or ((range2Start <= range1Start) and (range2End >= range1Start)):
            sum += 1
#correct 905       
print(sum)