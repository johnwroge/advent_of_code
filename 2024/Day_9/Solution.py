
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
        if char_list[i] == '.':
            while char_list[len(char_list) - 1] == '.':
                char_list.pop()
            char_list[i] = char_list.pop()
        i += 1
    return char_list

def calculate_checksun(string):
    """
    To calculate the checksum, add up the result of multiplying each of these blocks' position
    with the file ID number it contains. The leftmost block is in position 0. If a block contains
    free space, skip it instead.

    Continuing the first example, the first few blocks' position multiplied by its file ID number
    are 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32, and so on. In this example, the
    checksum is the sum of these, 1928.
    
    """
    # current index times file id number, if '.' or free space skip
    pass

def Part_One():
    contents = read_file('test.txt')
    formatted = format_string(contents)
    updated = update(formatted)
    # print(''.join(updated))
    # print('0099811188827773336446555566')


    # calculate checksum and return

if __name__ == "__main__":
    print(Part_One())