
"""
3 tokens to push A button
1 token to push B button

minimize A pushes first 

limit should be 100 presses from either button
"""

import os
def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_13/{filename}', 'r') as file:
        contents = file.read()
    return contents

print(read_file('test_1.txt'))

