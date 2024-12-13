#https://adventofcode.com/2024/day/12
import numpy as np
from collections import deque, defaultdict
from collections import Counter
import copy
import sympy
# Recursive function with memorization
from functools import lru_cache
#@lru_cache(None)

# Open and read the file as a single string
with open('12i.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]
print(f"grid: {grid}")
rows = len(grid)
cols = len(grid[0])
print(f"rows x cols: {rows} x {cols}")

# Directions  Up,      Down,   Left,    Right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Initialize visited
visited = [[False for _ in range(cols)] for _ in range(rows)]

def bfs(r, c, plant):
    # Find area
    start = (r, c)
    queue = deque([start])
    visited[r][c] = True
    area = set()
    
    while queue:
        r, c = queue.popleft()
        area.add((r, c))
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != plant:
                continue
            elif not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))
    # print(f"area: {area}")



    # Find corners
    
    # 1: Add half coordinates as fence for all coordinates in current area.
    #    Add all fence coordinates as possible corners.
    corner_candidates = set()
    for r, c in area:
        for cr, cc in [(r - 0.5, c - 0.5), (r + 0.5, c - 0.5), (r + 0.5, c + 0.5), (r - 0.5, c + 0.5)]:
            corner_candidates.add((cr, cc))
            # print(f"corner_candidates: {corner_candidates}")

    # 2: Loop through all corner candidates and see if they exist in area or not
    corners = 0
    for cr, cc in corner_candidates:
        config = [(sr, sc) in area for sr, sc in [(cr - 0.5, cc - 0.5), (cr + 0.5, cc - 0.5), (cr + 0.5, cc + 0.5), (cr - 0.5, cc + 0.5)]]
        # print(f"config: {config}")

        number = sum(config)
        # print(f"number: {number}")
        # xo
        # oo
        if number == 1:
            corners += 1
        # xo
        # ox
        # or
        # ox
        # xo
        elif number == 2:
            # [top-left, top-right, bottom-right, bottom-left]
            if config == [True, False, True, False] or config == [False, True, False, True]:
                corners += 2
        # xx
        # xo
        elif number == 3:
            corners += 1

    return len(area) * corners



total_fence_cost = 0
for row in range(rows):
    for col in range(cols):
        print(f"grid[row={row}][col={col}]: {grid[row][col]}")
        if not visited[row][col]:
            plant = grid[row][col]
            total_fence_cost += bfs(row, col, plant)
print(f"Total Fence Cost: {total_fence_cost}")
# Correct answer: 855082