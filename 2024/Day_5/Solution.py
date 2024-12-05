import os

with open(os.getcwd() + '/2024/Day_5/data.txt') as file:
    content = file.read().split('\n')
    rules = [list(map(int,row.split('|'))) for row in content if '|' in row]
    updates = [list(map(int,update.split(','))) for update in content if ',' in update]

# print(rules)
# print(updates)
broken = []

def Part_One():
    to_include = []

    for update in updates:
        count = len(rules)
        for rule in rules:
            before, after = rule
            if before in update and after in update:
                first_index, second_index = update.index(before), update.index(after)
                if first_index < second_index:
                    count -= 1
                else:
                    broken.append(update)
                    break
            else:
                count -= 1
        if count == 0:
            to_include.append(update)

    medians = []
    for update in to_include:
        index = len(update) // 2
        med = update[index]
        medians.append(med)
    
    return sum(medians)



def Part_Two():
    print(broken)


print(Part_One())
print(Part_Two())


