# 1625, 2250
with open('/Users/johnwroge/advent_of_code/Day6/data.txt', 'r') as file:
    contents = file.read()
    def isDistinct(arr):
        dict = {}
        for i in range(len(arr)):
            if arr[i] in dict:
                dict[arr[i]] += 1
            else: 
                dict[arr[i]] = 1  
        for val in dict.values():
            if val > 1:
                return False
        return True  

    window = []
    for i in range(14):
        window.append(contents[i])
    
    for i in range(14,len(contents)):
        if isDistinct(window):
            print(i)
            break
        else:
            window.append(contents[i])
            window.pop(0)


