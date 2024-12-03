import os 

'''
The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
'''

with open(os.getcwd() + '/2024/Day_2/data.txt', 'r') as file:
    lines = file.readlines()
    reports = []
    for line in lines:
        numbers = [int(num) for num in line.split()]
        reports.append(numbers)

def is_valid_sequence(report, is_increasing):
    start = 0 if is_increasing else len(report) - 1
    step = 1 if is_increasing else -1
    
    for i in range(1, len(report)) if is_increasing else range(len(report)-2, -1, -1):
        prev = i - 1 if is_increasing else i + 1
        if report[i] - report[prev] > 3 or report[i] - report[prev] < 1:
            return False
    return True
        
def increasing(report):
    return sorted(report) == report

def decreasing(report):
    return sorted(report, reverse=True) == report


def Solution(part_2):
    safe_reports = 0
    for report in reports:
        if is_valid_sequence(report, increasing(report)) or is_valid_sequence(report, decreasing(report)):
            safe_reports += 1
            continue
            
        if part_2:
            for i in range(len(report)):
                test_report = report[:i] + report[i+1:]
                if (increasing(test_report) and is_valid_sequence(test_report, True)) or \
                   (decreasing(test_report) and is_valid_sequence(test_report, False)):
                    safe_reports += 1
                    break
                    
    return safe_reports
    

print(Solution(False))
print(Solution(True))