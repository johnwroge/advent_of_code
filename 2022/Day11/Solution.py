from collections import deque
import os, re


def parse_monkeys(input_text):
    monkey_blocks = input_text.strip().split("\n\n")
    monkeys = []

    for block in monkey_blocks:
        lines = block.strip().splitlines()
        
        items_line = lines[1]
        items = deque(map(int, re.findall(r'\d+', items_line)))

        op_line = lines[2]
        op_match = re.search(r'new = old ([+*]) (\d+|old)', op_line)
        operator, operand = op_match.groups()
        if operand == 'old':
            op = lambda old, op=operator: old * old if op == '*' else old + old
        else:
            operand = int(operand)
            op = lambda old, op=operator, val=operand: old * val if op == '*' else old + val

        test_line = lines[3]
        test_div = int(re.search(r'\d+', test_line).group())

        true_target = int(re.search(r'\d+', lines[4]).group())
        false_target = int(re.search(r'\d+', lines[5]).group())

        monkeys.append({
            "items": items,
            "op": op,
            "test": test_div,
            "if_true": true_target,
            "if_false": false_target,
            "inspect_count": 0
        })

    return monkeys

def Solution(monkeys):
    
    for _ in range(20):
        for monkey in monkeys:
            while monkey["items"]:
                item = monkey["items"].popleft()
                monkey["inspect_count"] += 1
                item = monkey["op"](item)
                item //= 3
                if item % monkey["test"] == 0:
                    monkeys[monkey["if_true"]]["items"].append(item)
                else:
                    monkeys[monkey["if_false"]]["items"].append(item)
        
    counts = sorted([m["inspect_count"] for m in monkeys], reverse=True)
    print("Level of monkey business:", counts[0] * counts[1])
    


with open(os.getcwd() + "/2022/Day11/part_1.txt") as f:
    input_text = f.read()

monkeys = parse_monkeys(input_text)
Solution(monkeys)
