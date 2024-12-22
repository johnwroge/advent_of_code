
import os

def read_file(filename):
    with open(os.getcwd() + f'/2024/Day_22/{filename}', 'r') as file:
        contents = file.read().split('\n')
    return list(map(int, contents))

def prune(num):
    return num % 16777216

def mix(secret, mix):
    return secret ^ mix

def process(secret):
    answers = [secret]
    for _ in range(2000):
        secret = prune(mix(secret, secret * 64))
        secret = prune(mix(secret, secret // 32))
        secret = prune(mix(secret, secret * 2048))
        answers.append(secret)
    return answers

def changes(prices):
    return [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]

def get_scores(prices, changes):
    answer = {}
    for i in range(len(changes) - 3):
        pattern = (changes[i], changes[i + 1], changes[i + 2], changes[i + 3])
        if pattern not in answer:
            answer[pattern] = prices[i + 4]
    return answer


def Solution():
    contents = read_file('data.txt')
    total = 0
    scores = {}
    for c in contents:
        prices = process(c)
        total += prices[-1]
        prices = [x % 10 for x in prices]
        change = changes(prices)
        score = get_scores(prices, change)
        for k, v in score.items():
            if k not in scores:
                scores[k] = v
            else:
                scores[k] += v
    return total,  max(scores.values())
        
if __name__ == '__main__':
    part_1, part_2 = Solution()
    print('Part One:', part_1)
    print('Part Two:', part_2)
