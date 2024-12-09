
import os

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_9/{filename}', 'r') as file:
        contents = file.read()
    return contents



def format_string(string):
    to_update = list(string)
    j = 0
    for i in range(len(string)):
        if i % 2 == 1:
            to_update[i] = '.' * int(to_update[i])
        else:
            to_update[i] = str(j) * int(to_update[i])
            j += 1
    return list(''.join(to_update))

def update(char_list):
    i = 0
    while i < len(char_list):
        if i == len(char_list):
            break
        if char_list[i] == '.':
            while char_list and char_list[len(char_list) - 1] == '.':
                char_list.pop()
                if i == len(char_list):
                    break
            if i == len(char_list):
                break
            char_list[i] = char_list.pop()
        i += 1
    return char_list

def calculate_checksum(string):
    return sum([i * int(string[i]) for i in range(len(string)) if string[i].isdigit()])

def Part_One():
    contents = read_file('data.txt')
    # contents = read_file('test.txt')
    # contents = "252"
    formatted = format_string(contents)
    updated = update(formatted)
    answer = calculate_checksum(updated)
    print(calculate_checksum("0099811188827773336446555566"))
    return answer
"""
# id can be a multi digit number
"""
if __name__ == "__main__":
    print(Part_One())
