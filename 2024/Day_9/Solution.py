
import os

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_9/{filename}', 'r') as file:
        contents = file.read()
    return contents

def generate_id(lines):
    # do we need id first or last, what is the lookup key later?
    pass

def format_string(string):
    # iterate over string and append digit or space ('.) alternating position
    pass

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
    print(contents)
    # create mapping of ids and blocks (id key and file type as value)

    # separate contents into sections with first(file block) and second (space)
    
        # insert periods at these block positions

    # format the files by shifting last most position to first available free space

    # calculate checksum and return

if __name__ == "__main__":
    print(Part_One())