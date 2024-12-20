import os
def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_19/{filename}', 'r') as file:
        towels, combinations = file.read().split('\n\n')
    towels = towels.split(', ')
    combinations = combinations.split('\n')
    return towels, combinations

def wordBreak(s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)] 
                    if dp[i]:
                        break
        return dp[0]


def Part_One():
    towels, combos = read_file('data.txt')
    counter = 0
    for c in combos:
        if wordBreak(c, towels):
             counter += 1
    return counter

def count_arrangements(design, valid_pieces):
    memo = {}
    def solve(pos):
        if pos == len(design):
            return 1
        if pos in memo:
            return memo[pos]
        count = 0
        for piece in valid_pieces:
            if pos + len(piece) <= len(design) and \
               all(c1 == c2 for c1, c2 in zip(design[pos:pos+len(piece)], piece)):
                count += solve(pos + len(piece))
        memo[pos] = count
        return count
        
    return solve(0)

def Part_Two():
    towels, combos = read_file('data.txt')
    counter = 0
    for c in combos:
        counter += count_arrangements(c, towels)
    return counter 
    
if __name__ == '__main__':
     print(Part_One())
     print(Part_Two())
