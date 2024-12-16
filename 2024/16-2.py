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

# Find path forward from start
# queue = deque()
# Queue: score, row, col, direction_index
# queue.append((0, start, 1))
pq = [(0, start[0], start[1], 1)]
visited = set()
lowest = None
s1 = {}
print(f"r, c: {r}, {c}")
while pq:
    # s, r, c, d = queue.popleft()
    s, r, c, d = heappop(pq)

    if (r, c, d) not in s1:
        s1[(r, c, d)] = s

    # If done
    if (r, c) == end:
        if lowest is None:
            lowest = s

    # If visisted
    if (r, c, d) in visited:
        continue
    visited.add((r, c, d))

    # Move forward
    dr, dc = directions[d]
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
        heappush(pq, (s + 1, nr, nc, d))

    # Rotate cw and ccw
    heappush(pq, (s + 1000, r, c, (d + 1) % 4))
    heappush(pq, (s + 1000, r, c, (d - 1) % 4))

print(f"Lowest score: {lowest}")



# Find path backwards from end
# Queue: score, row, col, direction_index
pq = []
for d in range(4):
    heappush(pq, (0, end[0], end[1], d))
visited = set()
s2 = {}
print(f"r, c: {r}, {c}")
while pq:
    s, r, c, d = heappop(pq)

    if (r, c, d) not in s2:
        s2[(r, c, d)] = s

    # If visisted
    if (r, c, d) in visited:
        continue
    visited.add((r, c, d))

    # Move backwards
    dr, dc = directions[(d + 2) % 4]
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
        heappush(pq, (s + 1, nr, nc, d))

    # Rotate cw and ccw
    heappush(pq, (s + 1000, r, c, (d + 1) % 4))
    heappush(pq, (s + 1000, r, c, (d - 1) % 4))



best_paths = set()
for r in range(rows):
    for c in range(cols):
        for d in range(4):
            # (r,c,dir) is on an optimal path if:
                # The scores exist on both paths
                # The score from start to (r, c, d) plus the score from (r, c, d) to end equals lowest score
            if (r, c, d) in s1 and (r, c, d) in s2 and s1[(r, c, d)] + s2[(r, c, d)] == lowest:
                best_paths.add((r, c))
print(f"Number of tiles on best paths: {len(best_paths)}")
# Correct Answer: 538



# Optional: Mark the grid for visualization
# for r, c in best_path:
#     if grid[r][c] not in "SE":
#         grid[r][c] = 'O'

# print("Marked Grid:")
# for row in grid:
#     print(''.join(row))