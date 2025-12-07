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

# queue = deque()
# queue.append((start[0], start[1]+1))

# timelines = 0
# while queue:
#     x, y = queue.popleft()
#     if not (0 <= x < width and 0 <= y < height):
#         timelines += 1
#         continue

#     if grid[y][x] == '^':
#         if x-1 >= 0:
#             queue.append((x-1, y+1))
#         if x+1 <= width:
#             queue.append((x+1, y+1))
#     else:
#         queue.append((x, y+1))

# print(f"timelines: {timelines}")

# ABOVE TOOK TO LONG TIME!!!
# Instead, remove duplicates => Add timeline counter for each coordinate
queue = deque()
queue.append((start[0], start[1]+1, 1))

timelines = 0
while queue:
    timelines_per_coordinate = defaultdict(int)
    # Merge all timelines into one
    # If multiple timelines are on the same (x, y) they will be merged together
    while queue:
        x, y, count = queue.popleft()
        timelines_per_coordinate[(x, y)] += count

    next_positions = defaultdict(int)
    for (x, y), count in timelines_per_coordinate.items():
        if not (0 <= x < width and 0 <= y < height):
            timelines += count
            continue

        if grid[y][x] == '^':
            if x-1 >= 0:
                next_positions[(x-1, y+1)] += count
            else:
                timelines += count
            if x+1 < width:
                next_positions[(x+1, y+1)] += count
            else:
                timelines += count
        else:
            next_positions[(x, y+1)] += count

    # Push next positions back into queue
    for (x, y), count in next_positions.items():
        queue.append((x, y, count))

print(f"timelines: {timelines}")
# Correct answers: 40 and 80158285728929
