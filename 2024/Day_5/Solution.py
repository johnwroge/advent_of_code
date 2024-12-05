import os

with open(os.getcwd() + '/2024/Day_5/data.txt') as file:
    content = file.read().split('\n')
    rules = [list(map(int,row.split('|'))) for row in content if '|' in row]
    updates = [list(map(int,update.split(','))) for update in content if ',' in update]

def find_sum_of_medians(group):
    medians = []
    for update in group:
        index = len(update) // 2
        med = update[index]
        medians.append(med)
    return sum(medians)

def Part_One():
    to_include = []
    broken = []
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
    answer = find_sum_of_medians(to_include)
    return answer, broken



def Part_Two(unsorted):
    fixed = []
    for update in unsorted:
        copy = update.copy()
        changes_made = True
        while changes_made:
            changes_made = False
            for rule in rules:
                before, after = rule
                if before in copy and after in copy:
                    first_index = copy.index(before)
                    second_index = copy.index(after)
                    if first_index > second_index:
                        copy[first_index], copy[second_index] = copy[second_index], copy[first_index]
                        changes_made = True
        fixed.append(copy)
    
    answer = find_sum_of_medians(fixed)
    return answer
    
part_1, unsorted = Part_One()
print("Part 1:", part_1)
part_2 = Part_Two(unsorted)
print("Part 2:", part_2)


