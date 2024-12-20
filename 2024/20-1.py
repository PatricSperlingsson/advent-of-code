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

# Draw grid
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
# Directions: Down,   Right,  Up,      Left
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(grid, start, end):
    queue = deque()
    visited = set()
    best_path = {}
    
    queue.append((start[0], start[1], 0))
    visited.add((start[0], start[1]))

    while queue:
        r, c, t = queue.popleft()
        
        # We are done
        if (r, c) == end:
            print(f"We are done: ({r}, {c}), cost: {t}")
            return t, best_path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 < nr < rows-1 and 0 < nc < cols-1:
                if grid[nr][nc] != '#' and (nr, nc) not in visited:
                    queue.append((nr, nc, t + 1))
                    visited.add((nr, nc))
                    best_path[(nr, nc)] = t + 1

# Test data:
# CHEAT_LENGTH = 2
# CHEAT_SAVE = 0
# Real data:
CHEAT_LENGTH = 20
CHEAT_SAVE = 100
def bfs_cheat(best_path, grid, start, end, goal):
    beat_fastest_time_cheating = 0
    queue = deque()
    visited = set()

    queue.append((start[0], start[1], 0, None, None, None, None, CHEAT_LENGTH))
    visited.add((start[0], start[1], None, None))

    while queue:
        r, c, t, cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c, cheat_time = queue.popleft()

        # Too slow    
        if t >= goal:
            continue

        # We are done
        if (r, c) == end:
            if t <= goal-CHEAT_SAVE:
                print(f"Cheat saved: {goal-t}, cheat: ({cheat_start_r}, {cheat_start_c})")
                beat_fastest_time_cheating += 1
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 < nr < rows-1 and 0 < nc < cols-1:
                if cheat_time == CHEAT_LENGTH and (nr, nc, cheat_start_r, cheat_start_c) not in visited:
                    if grid[nr][nc] == '#':
                        queue.append((nr, nc, t + 1, nr, nc, cheat_end_r, cheat_end_c, 1))
                        visited.add((nr, nc, nr, nc))
                    else:
                        queue.append((nr, nc, t + 1, cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c, cheat_time))
                        visited.add((nr, nc, cheat_start_r, cheat_start_c))
                elif cheat_time < CHEAT_LENGTH and cheat_time > 0 and (nr, nc, cheat_start_r, cheat_start_c) not in visited:
                    if grid[nr][nc] != '#':
                        if (nr, nc) in best_path and best_path[(nr, nc)] > t+1:
                            queue.append((nr, nc, t + 1, cheat_start_r, cheat_start_c, nr, nc, 0))
                            visited.add((nr, nc, cheat_start_r, cheat_start_c))
                elif cheat_time == 0 and grid[nr][nc] != '#' and (nr, nc, cheat_start_r, cheat_start_c) not in visited:
                    if (nr, nc) in best_path and best_path[(nr, nc)] >= t+1:
                        queue.append((nr, nc, t + 1, cheat_start_r, cheat_start_c, nr, nc, 0))
                        visited.add((nr, nc, cheat_start_r, cheat_start_c))

    draw_grid(visited)
    return beat_fastest_time_cheating

fastest_time_no_cheat, best_path = bfs(grid, start, end)
print(f"len(best_path): {len(best_path)}")
print(f"fastest_time_no_cheat: {fastest_time_no_cheat}")
beat_fastest_time_cheating = bfs_cheat(best_path, grid, start, end, fastest_time_no_cheat)
print(f"beat_fastest_time_cheating: {beat_fastest_time_cheating}")
# Correct Answer: 44
# Correct Answer: 1429