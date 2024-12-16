#https://adventofcode.com/2024/day/16
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

# Open and read the file as a single string
with open('16i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

# Grid
robot_pos = None
grid = []
for r, row in enumerate(lines):
    nrow = []
    for c, char in enumerate(row):
        if char == '#':
            nrow.append('#')
        if char == '.':
            nrow.append('.')
        elif char == 'S':
            nrow.append('S')
            start = (r, c)
        elif char == 'E':
            nrow.append('E')
            end = (r, c)
    grid.append(''.join(nrow))
print("Grid:")
for row in grid:
    print(row)
# Convert to list so that I can update robot and box positions
grid = [list(row) for row in grid]
for row in grid:
    print(row)

rows = len(grid)
cols = len(grid[0])
print(f"rows: {rows}")
print(f"cols: {cols}")
print(f"start: {start}")
print(f"end: {end}")

#             N        E       S        W
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
print(f"directions: {directions}")

# Find path
# queue = deque()
# Queue: score, row, col, direction_index
# queue.append((0, start[0], start[1], 1))
pq = [(0, start[0], start[1], 1)]
visited = set()
print(f"r, c: {r}, {c}")
while pq:
# while queue:
    # s, r, c, d = queue.popleft()
    s, r, c, d = heappop(pq)

    # If done
    if (r, c) == end:
        print(f"Lowest score: {s}")
        break

    # If visisted
    if (r, c, d) in visited:
        continue
    visited.add((r, c, d))

    # Move forward
    dr, dc = directions[d]
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
        heappush(pq, (s + 1, nr, nc, d))
        # queue.append((s + 1, nr, nc, d))

    # Rotate cw and ccw
    heappush(pq, (s + 1000, r, c, (d + 1) % 4))
    heappush(pq, (s + 1000, r, c, (d - 1) % 4))
    # queue.append((s + 1000, r, c, (d + 1) % 4))
    # queue.append((s + 1000, r, c, (d - 1) % 4))
# Correct Answer: 7036