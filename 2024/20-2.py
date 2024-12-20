#https://adventofcode.com/2024/day/20
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
with open('../../inputs/2024/20i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")
rows = len(lines)
cols = len(lines[0])
print(f"rows: {rows}")
print(f"cols: {cols}")

# Print grid in two ways
start = None
end = None
grid = []
for r, row in enumerate(lines):
    nrow = []
    for c, char in enumerate(row):
        if char == '#':
            nrow.append('#')
        elif char == 'S':
            start = (r, c)
            nrow.append('S')
        elif char == 'E':
            end = (r, c)
            nrow.append('E')
        elif char == '.':
            nrow.append('.')
    grid.append(''.join(nrow))
print("grid:")
for row in grid:
    print(row)
# Convert to list so that I can update robot and box positions
grid_list = [list(row) for row in grid]
for row in grid_list:
    print(row)

# Draw grid together with visited and parse start and end
# Visited not updated for part 2!
def draw_grid(visited):
    # Draw grid
    start = None
    end = None
    grid = []
    for r, row in enumerate(lines):
        nrow = []
        for c, char in enumerate(row):
            if (r, c, 0) in visited or (r, c, 1) in visited or (r, c, 2) in visited:
                nrow.append('0')
            elif char == '#':
                nrow.append('#')
            elif char == 'S':
                start = (r, c)
                nrow.append('S')
            elif char == 'E':
                end = (r, c)
                nrow.append('E')
            elif char == '.':
                nrow.append('.')
        grid.append(''.join(nrow))
    print("grid:")
    for row in grid:
        print(row)
    # Convert to list so that I can update robot and box positions
    grid_list = [list(row) for row in grid]
    for row in grid_list:
        print(row)

print(f"start: {start}")
print(f"end: {end}")
# Directions: Right,  Down,   Left,    Up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Print grid with all distances per track
def bfs(grid, start, end):
    dists = [[-1] * cols for _ in range(rows)]
    dists[start[0]][start[1]] = 0

    queue = deque([(start[0], start[1])])
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
            if grid[nr][nc] == "#": continue
            if dists[nr][nc] != -1: continue
            dists[nr][nc] = dists[r][c] + 1
            queue.append((nr, nc))

    for row in dists:
        print(*row, sep="\t")
    return dists
dists = bfs(grid, start, end)

# Print grid with all distances per track
def while_instead_of_bfs(grid, start, end):
    dists = [[-1] * cols for _ in range(rows)]
    dists[start[0]][start[1]] = 0

    r, c = start[0], start[1]
    while grid[r][c] != "E":
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
            if grid[nr][nc] == "#": continue
            if dists[nr][nc] != -1: continue
            dists[nr][nc] = dists[r][c] + 1
            r = nr
            c = nc

    for row in dists:
        print(*row, sep="\t")
    return dists
dists = while_instead_of_bfs(grid, start, end)



# Part 1, cheat size 2
# Directions: DD,     DR,     RR,     UR,      UU,      UL,       LL,      DL
directions = [(2, 0), (1, 1), (0, 2), (-1, 1), (-2, 0), (-1, -1), (0, -2), (1, -1)]
count = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "#": continue
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
            if grid[nr][nc] == "#": continue
            if dists[r][c] - dists[nr][nc] >= 102: count += 1
print(f"Part 1, saving at least 100ps: {count}")
# Correct Answer: 1429



# Part 2, cheat size 20
count = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "#": continue
        for radius in range(2, 21):
            for dr in range(radius + 1):
                dc = radius - dr
                for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                    if grid[nr][nc] == "#": continue
                    if dists[r][c] - dists[nr][nc] >= 100 + radius: count += 1
print(f"Part 2, saving at least 100ps: {count}")
# Correct Answer: 988931