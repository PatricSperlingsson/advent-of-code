#https://adventofcode.com/2024/day/5
import numpy as np
from collections import deque
from collections import Counter
import copy
import sympy
from collections import defaultdict, deque

# Open and read the file as a single string
with open('5it.txt', 'r') as file:
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
incorrect_updates = []
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
    else:
        incorrect_updates.append(update)
print(f"correct_updates: {correct_updates}")
print(f"incorrect_updates: {incorrect_updates}")



# Kahn's algorithm using topological sort
# "in_degree" represents the number of dependencies a node has. 
# If in_degree == 0 for a node, it means it can be processed (has no dependencies left).
reordered_updates = []
for update in incorrect_updates:
    # Build graph from rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Include only rules relevant to the update
    for rule1, rule2 in rules:
        if rule1 in update and rule2 in update:
            graph[rule1].append(rule2)
            in_degree[rule2] += 1
            if rule1 not in in_degree:
                in_degree[rule1] = 0
    print(f"graph: {graph}")
    print(f"in_degree: {in_degree}")
    
    # Topological sort using Kahn's algorithm
    # Start with nodes that have an in_degree of 0 (no dependencies).
    # As each node is processed, reduce the in-degree of its neighbors.
    # If a neighbor's in-degree becomes 0, it can also be processed.
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    print(f"queue: {queue}")
    
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            # Since dependency is resolved, we can decrease the in_degree for its neighbors
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    reordered_updates.append(sorted_update)



sum_middle_page_numbers = 0
for reordered_update in reordered_updates:
    sum_middle_page_numbers += reordered_update[len(reordered_update) // 2]

print(f"sum_middle_page_numbers: {sum_middle_page_numbers}")
# Correct answer: 4598