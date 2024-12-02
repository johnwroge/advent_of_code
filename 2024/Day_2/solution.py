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

def is_valid(increasing, decreasing, report, flag = False):
        if not increasing and not decreasing and not flag:
            return False
        bad_reports = 0
        length = len(report)
        if increasing:
            start = 0
            for i in range(1, length):
                if  i < 0 or i >= len(report):
                    return False

                if report[i] - report[start] > 3 or report[i] - report[start] < 1:
                    if not flag:
                        return False
                    else:
                        bad_reports += 1
                        report.pop(start)
                        length -= 1
                start += 1
            return True if bad_reports <= 2 else False

        elif decreasing:
            start = length - 1
            for i in range(start - 1, -1, -1):
                if i < 0 or i >= len(report):
                    return False
                if report[i] - report[start] > 3 or report[i] - report[start] < 1:
                    if not flag:
                        return False
                    else:
                        bad_reports += 1
                        report.pop(start)
                        length -= 1
                start -= 1
            return True if bad_reports <= 2 else False
        
def increasing(report):
    return sorted(report) == report

def decreasing(report):
    return sorted(report, reverse=True) == report


# returns number of safe reports
def Solution(part_2):
    safe_reports = 0
    for report in reports:
        up = increasing(report)
        down = decreasing(report)
        if is_valid(up, down, report, part_2):
            safe_reports += 1
    return safe_reports

    


# print(Solution(False))
print(Solution(True))