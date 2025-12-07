#https://adventofcode.com/2025/day/7
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
from math import gcd
from sympy import symbols, Eq, solve
from itertools import product
from functools import cache

# Open and read the file as a single string
# Outputs a list from the delimitier '\n'
with open('../../inputs/2025/7i.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]
print(f"grid: {grid}")



height = len(grid)
width = len(grid[0])

for y in range(height):
    for x in range(width):
        if grid[y][x] == 'S':
            start = (x, y)
            print(f"{start}")

split_count = 0
queue = deque()
queue.append((start[0], start[1]+1))
visited = set()

while queue:
    x, y = queue.popleft()
    if not (0 <= x < width and 0 <= y < height):
        continue
    if (x, y) in visited:
        continue
    visited.add((x, y))

    if grid[y][x] == '^':
        split_count += 1
        if x-1 >= 0:
            queue.append((x-1, y+1))
        if x+1 <= width:
            queue.append((x+1, y+1))
    else:
        queue.append((x, y+1))

print(f"split_count: {split_count}")
# Correct answers: 21 and 1541
