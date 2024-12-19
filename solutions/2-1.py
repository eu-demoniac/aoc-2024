import operator
from itertools import pairwise

def is_safe(report: list[int]) -> bool:
    distance = report[1] - report[0]
    if distance == 0:
        return False
    
    is_strictly_monotonic = operator.gt if distance > 0 else operator.lt
    
    for prev, next in pairwise(report):
        if not is_strictly_monotonic(next, prev):
            return False
        if abs(next - prev) > 3:
            return False

    return True

safe_reports_count = 0

with open('inputs/2.txt') as file:
    for line in file:
        report = [int(level) for level in line.split()]

        if is_safe(report):
            safe_reports_count += 1

print(safe_reports_count)
