#https://adventofcode.com/2025/day/8
import numpy as np
from collections import deque, Counter, defaultdict
# Priority Queue
from heapq import heappop, heappush
import copy
import sympy
# Recursive function with memorization
from functools import lru_cache
#@lru_cache(None)
# Creating functions
# from math import gcd
import math
from sympy import symbols, Eq, solve
from itertools import product
from functools import cache

# Open and read the file as a single string
# Outputs a list from the delimitier '\n'
with open('../../inputs/2025/8i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

coords = []
for line in lines:
    x, y, z = map(int, line.split(","))
    coords.append((x, y, z))
print(f"coords: {coords}")

num_junction_boxes = len(coords)



# Calculate distances between all junction boxes
pairs = []
for i in range(num_junction_boxes):
    for j in range(i+1, num_junction_boxes):
        x1, y1, z1 = coords[i]
        x2, y2, z2 = coords[j]
        dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
        pairs.append((dist, i, j))
print(f"pairs: {pairs}")

# Sort
pairs.sort(key=lambda x: x[0])
print(f"pairs: {pairs}")



# Union-Find (Disjoint Set Union)

def get_last_connection(c, last_connection):
    if c == last_connection[c]:
        return c
    return get_last_connection(last_connection[c], last_connection)



# Everyone starts connected to itself
last_connection = {i: i for i in range(num_junction_boxes)}

for c in range(1000): # 10 for test
    dist, i, j = pairs[c]
    ci, cj = get_last_connection(i, last_connection), get_last_connection(j, last_connection)
    if ci != cj:
        last_connection[cj] = ci


# Count all last_connections
all_last_connections = defaultdict(int)
for i in range(num_junction_boxes):
    lc = get_last_connection(i, last_connection)
    all_last_connections[lc] += 1

sizes = sorted(all_last_connections.values(), reverse=True)
result = sizes[0] * sizes[1] * sizes[2]

print(f"result: {result}")
# Correct answers: 40 and 96672
