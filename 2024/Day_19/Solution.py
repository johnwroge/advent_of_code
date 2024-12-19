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

if __name__ == '__main__':
     print(Part_One())