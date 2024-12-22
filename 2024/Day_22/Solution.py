
'''
Calculate the result of multiplying the secret number by 64. Then, mix this result into the
secret number. Finally, prune the secret number.

mix - calculate the bitwise XOR of the given value and the secret number.

prune - calculate the value of the secret number modulo 16777216.

Calculate the result of dividing the secret number by 32. Round the result down to the nearest
integer. Then, mix this result into the secret number. Finally, prune the secret number.

Calculate the result of multiplying the secret number by 2048. Then, mix this result into
the secret number. Finally, prune the secret number.
'''
import os

expected_output = """
1: 8685429
10: 4700978
100: 15273692
2024: 8667524
"""

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_22/{filename}', 'r') as file:
        contents = file.read().split('\n')
    return list(map(int, contents))

def prune(num):
    return num % 16777216

def mix(secret, mix):
    return secret ^ mix

def multiply(num):
    return num * 64

def process(secret):
    first = secret * 64
    secret = mix(secret, first)
    secret = prune(secret)
    second = secret // 32
    secret = mix(secret, second)
    secret = prune(secret)
    third = secret * 2048
    secret = mix(secret, third)
    secret = prune(secret)
    return secret

def test(secret):
    for i in range(10):
        test = process(secret)
        print('test', test)
        secret = test

def Part_One():
    contents = read_file('data.txt')
    total = 0
    for c in contents:
        secret = c
        for _ in range(2000):
            result = process(secret)
            secret = result
        total += secret
    return total
        

        
if __name__ == '__main__':
    print(Part_One())

  
    


