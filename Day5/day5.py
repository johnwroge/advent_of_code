# Open the file
with open('/Users/johnwroge/advent_of_code/Day5/data.txt', 'r') as file:
    # Read the lines and reverse the order
    stack_strings, instructions = (i.splitlines() for i in file.read().strip("\n").split("\n\n"))
        
    stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ", "")}
    
    indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]
def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks: 
        print(stack, stacks[stack])
    print("\n")


def loadStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1   
loadStacks()  

# def iterate(length, src, dest):
#     for i in range(length):
#         val = stacks[src].pop()
#         stacks[dest].append(val)
def iterate(length, src, dest):
    list = []
    for i in range(length):
        val = stacks[src].pop()
        list.append(val)
    list.reverse()
    stacks[dest] += list

for line in instructions:
    instruct = line.split(" ")
    length = int(instruct[1])
    src = int(instruct[3])
    dest = int(instruct[5]) 
    iterate(length, src, dest)
displayStacks()


