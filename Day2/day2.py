with open('/Users/johnwroge/advent_of_code/Day2/data.txt', 'r') as file:
    contents = file.read().splitlines()
    yourScore = 0
    theirScore = 0
    for i in range(len(contents)):
        yourPlay = contents[i][2]
        theirPlay = contents[i][0]
        # if yourPlay == "X" and theirPlay == "A":
        #     yourScore += 4
        #     theirScore += 4 
        
        # elif yourPlay == "X" and theirPlay == "B":
        #     yourScore += 1
        #     theirScore += 8
        
        # elif yourPlay == "X" and theirPlay == "C":
        #     yourScore += 7
        #     theirScore += 3

        # elif yourPlay == "Y" and theirPlay == "A":
        #     yourScore += 8
        #     theirScore += 1 

        # elif yourPlay == "Y" and theirPlay == "B":
        #     yourScore += 5
        #     theirScore += 5

        # elif yourPlay == "Y" and theirPlay == "C":
        #     yourScore += 2
        #     theirScore += 9

        # elif yourPlay == "Z" and theirPlay == "A":
        #     yourScore += 3
        #     theirScore += 7 

        # elif yourPlay == "Z" and theirPlay == "B":
        #     yourScore += 9
        #     theirScore += 2

        # elif yourPlay == "Z" and theirPlay == "C":
        #     yourScore += 6
        #     theirScore += 6
        if yourPlay == "X" and theirPlay == "A":
            yourScore += 3
            theirScore += 7
        
        elif yourPlay == "X" and theirPlay == "B":
            yourScore += 1
            theirScore += 8
        
        elif yourPlay == "X" and theirPlay == "C":
            yourScore += 2
            theirScore += 9

        elif yourPlay == "Y" and theirPlay == "A":
            yourScore += 4
            theirScore += 4

        elif yourPlay == "Y" and theirPlay == "B":
            yourScore += 5
            theirScore += 5

        elif yourPlay == "Y" and theirPlay == "C":
            yourScore += 6
            theirScore += 6

        elif yourPlay == "Z" and theirPlay == "A":
            yourScore += 8
            theirScore += 1 

        elif yourPlay == "Z" and theirPlay == "B":
            yourScore += 9
            theirScore += 2

        elif yourPlay == "Z" and theirPlay == "C":
            yourScore += 7
            theirScore += 3
print(yourScore)
