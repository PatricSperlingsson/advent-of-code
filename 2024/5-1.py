#https://adventofcode.com/2024/day/5
import numpy as np
from collections import deque
from collections import Counter
import copy
import sympy

# Open and read the file as a single string
with open('5i.txt', 'r') as file:
    data = file.read().strip()
    sections = data.split('\n\n')
print(f"data: {data}")
print(f"sections: {sections}")

rules = []
for line in sections[0].split("\n"):
    line = line.strip()
    p1 = line.split("|")[0]
    p2 = line.split("|")[1]
    rules.append((int(p1),int(p2)))
print(f"rules: {rules}")

updates = []
for line in sections[1].split("\n"):
    line = line.strip()
    update = [int(li) for li in line.split(",")]
    updates.append(update)
print(f"updates: {updates}")

correct_updates = []
for update in updates:
    rule_broken = False
    for rule1, rule2 in rules:
        # Check if the rules exist
        if rule1 in update and rule2 in update:
            if update.index(rule1) < update.index(rule2):
                continue
            rule_broken = True
    if not rule_broken:
        correct_updates.append(update)
print(f"correct_updates: {correct_updates}")

sum_middle_page_numbers = 0
for correct_update in correct_updates:
    sum_middle_page_numbers += correct_update[len(correct_update) // 2]

print(f"sum_middle_page_numbers: {sum_middle_page_numbers}")
# Correct answer: 5452