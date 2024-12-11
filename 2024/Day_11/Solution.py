
import os

def read_file(filename):
    with open(os.getcwd()+f'/2024/Day_11/{filename}', 'r') as file:
        contents = file.read().split()
        return contents


def Part_One():
    contents = read_file('data.txt')
    blinks = 25
    while blinks > 0:
        curr = []
        for i in range(len(contents)):
            stone = contents[i]
            length = len(stone)
            if stone == '0':
                curr.append('1')
            elif length % 2 == 0:
                first = str(int(stone[:length//2],base=10))
                second = str(int(stone[length//2:],base=10))
                # if any(str(i) in  second for i in range(1, 10)):
                #     second.lstrip('0')
                # elif all(c == '0' for c in second):
                #     second = '0'
                curr.extend([first, second])
            else: 
                num = int(stone) * 2024
                curr.append(str(num))
        # print(curr)
        contents = curr
        
        blinks -= 1
    # print('2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2')
    return len(contents)


if __name__ == "__main__":
    print(Part_One())