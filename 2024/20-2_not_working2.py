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
with open('../inputs/2024/20i.txt', 'r') as file:
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
CHEAT_LENGTH = 20
CHEAT_SAVE = 50
# Real data:
# CHEAT_LENGTH = 20
# CHEAT_SAVE = 100
def bfs_cheat(best_path, grid, start, end, goal):
    beat_fastest_time_cheating = 0
    queue = deque()
    visited = set()
    beat_fastest_time_cheating = set()
    
    queue.append((start[0], start[1], 0, None, None, None, None, CHEAT_LENGTH))
    # visited.add((start[0], start[1], None, None, None, None, CHEAT_LENGTH))

    while queue:
        r, c, t, cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c, cheat_time = queue.popleft()

        # Too slow    
        if t > goal-CHEAT_SAVE:
            continue

        # We are done
        if (r, c) == end:
            if cheat_end_r is None and cheat_end_c is None:
                cheat_end_r, cheat_end_c = (r,c)
            if t <= goal-CHEAT_SAVE and (cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c) not in beat_fastest_time_cheating:
                print(f"Cheat saved: {goal-t}, cheat start: ({cheat_start_r}, {cheat_start_c}), cheat end: ({cheat_end_r}, {cheat_end_c})")
                beat_fastest_time_cheating.add((cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c))

        # Check visited
        if (r, c, cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c, cheat_time) in visited:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                # Already visited
                # if (nr, nc, cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c) in visited:
                #     continue
                # visited.add((nr, nc, cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c, cheat_time))

                # Check cheat state
                if cheat_time == CHEAT_LENGTH:
                    if grid[nr][nc] == '#':
                        # Cheat start
                        queue.append((nr, nc, t + 1, nr, nc, cheat_end_r, cheat_end_c, cheat_time - 1))
                        visited.add((nr, nc, nr, nc, cheat_end_r, cheat_end_c, cheat_time - 1))
                    else:
                        # Continue without cheat
                        queue.append((nr, nc, t + 1, cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c, cheat_time))
                        visited.add((nr, nc, cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c, cheat_time))
                elif cheat_time < CHEAT_LENGTH and cheat_time > 0:
                    if grid[nr][nc] != '#':
                        # # if (nr, nc) in best_path and best_path[(nr, nc)] > t+1:
                        # if (nr, nc) in best_path and best_path[(nr, nc)] <= goal-CHEAT_SAVE-(t+1):
                        #     beat_fastest_time_cheating.add((cheat_start_r, cheat_start_c, nr, nc))
                        if t <= goal-CHEAT_SAVE and (cheat_start_r, cheat_start_c, nr, nc) not in beat_fastest_time_cheating:
                            print(f"Cheat saved: {goal-t}, cheat start: ({cheat_start_r}, {cheat_start_c}), cheat end: ({nr}, {nc})")
                            beat_fastest_time_cheating.add((cheat_start_r, cheat_start_c, nr, nc))
                    else:
                        queue.append((nr, nc, t + 1, cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c, cheat_time - 1))
                        visited.add((nr, nc, cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c, cheat_time - 1))
                elif cheat_time == 0 and grid[nr][nc] != '#':
                    if t <= goal-CHEAT_SAVE and (cheat_start_r, cheat_start_c, nr, nc) not in beat_fastest_time_cheating:
                        print(f"Cheat saved: {goal-t}, cheat start: ({cheat_start_r}, {cheat_start_c}), cheat end: ({nr}, {nc})")
                        beat_fastest_time_cheating.add((cheat_start_r, cheat_start_c, nr, nc))
                    # if (nr, nc) in best_path and best_path[(nr, nc)] <= goal-CHEAT_SAVE-(t+1):
                    #     beat_fastest_time_cheating.add((cheat_start_r, cheat_start_c, nr, nc))

                    # if (nr, nc) in best_path and best_path[(nr, nc)] >= t+1:
                    #     if cheat_end_r is None and cheat_end_c is None:
                    #         queue.append((nr, nc, t + 1, cheat_start_r, cheat_start_c, nr, nc, 0))
                    #     else:
                    #         queue.append((nr, nc, t + 1, cheat_start_r, cheat_start_c, cheat_end_r, cheat_end_c, 0))

    draw_grid(visited)
    return beat_fastest_time_cheating

fastest_time_no_cheat, best_path = bfs(grid, start, end)
print(f"len(best_path): {len(best_path)}")
print(f"fastest_time_no_cheat: {fastest_time_no_cheat}")
beat_fastest_time_cheating = bfs_cheat(best_path, grid, start, end, fastest_time_no_cheat)
print(f"len(beat_fastest_time_cheating): {len(beat_fastest_time_cheating)}")
# Correct Answer: 1429