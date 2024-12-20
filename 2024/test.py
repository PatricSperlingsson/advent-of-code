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

# Draw grid together with visited
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








# bfs with no cheat
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

# bfs with cheat
def bfs_cheat(best_path, grid, start, end, goal):
    ans = set()
    Q = deque([(0,None,None,None,start[0],start[1])])
    SEEN = set()
    SAVE = 50
    # SAVE = 100
    while Q:
        d,cheat_start,cheat_end,cheat_time,r,c = Q.popleft()
        assert cheat_end is None
        if d>=goal-SAVE:
            continue
        if grid[r][c] == 'E':
            if cheat_end is None:
                cheat_end = (r,c)
            if d<=goal-SAVE and (cheat_start,cheat_end) not in ans:
                #print(d,goal,r,c,cheat_start,cheat_end,cheat_time)
                ans.add((cheat_start, cheat_end))
        if (r,c,cheat_start,cheat_end,cheat_time) in SEEN:
            continue
        SEEN.add((r,c,cheat_start,cheat_end,cheat_time))
        #if len(SEEN) % 1000000 == 0:
        #    print(len(SEEN))

        if cheat_start is None: # start cheat
            assert grid[r][c] != '#'
            Q.append((d,(r,c),None,CHEAT_LENGTH,r,c))
        if cheat_time is not None and grid[r][c]!='#': # and cheat_time==0: # end cheat
            assert grid[r][c] in ['.', 'S', 'E']
            if (r, c) in best_path and best_path[(r,c)] <= goal-SAVE-d:
                ans.add((cheat_start, (r,c)))
                #if len(ans) % 1000 == 0:
                #    print(len(ans), d+DIST[(r,c)])
            #Q.append((d,cheat_start,(r,c),None,r,c))
        if cheat_time == 0:
            continue
        else:
            for dr,dc in directions:
                rr,cc = r+dr, c+dc
                if cheat_time is not None:
                    assert cheat_time > 0
                    if 0<=rr< rows and 0<=cc< cols:
                        Q.append((d+1,cheat_start,None,cheat_time-1,rr,cc))
                else:
                    if 0<=rr< rows and 0<=cc< cols and grid[rr][cc]!='#':
                        Q.append((d+1,cheat_start,cheat_end,cheat_time,rr,cc))
    #print(len(SEEN))
    return len(ans)

fastest_time_no_cheat, best_path = bfs(grid, start, end)
print(f"len(best_path): {len(best_path)}")
print(f"fastest_time_no_cheat: {fastest_time_no_cheat}")
print(f"best_path: {best_path}")
beat_fastest_time_cheating = bfs_cheat(best_path, grid, start, end, fastest_time_no_cheat)
# print(f"len(beat_fastest_time_cheating): {len(beat_fastest_time_cheating)}")
print(f"beat_fastest_time_cheating: {beat_fastest_time_cheating}")
# Correct Answer: 1429