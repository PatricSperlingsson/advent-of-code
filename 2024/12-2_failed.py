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
    start = (r, c)
    queue = deque([start])
    visited[r][c] = True
    area = 0
    fences = set()
    different_sides = 0
    
    while queue:
        r_prev, c_prev = queue.popleft()
        area += 1
        
        for dr, dc in directions:
            nr, nc = r_prev + dr, c_prev + dc
            print(f"  nr, nc: {nr}, {nc}")
            
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != plant:
                # Add new fence
                print(f"    fences: {fences}")
                fences.add((nr, nc))
                print(f"    Add new fence: {nr}, {nc}")

                # Check if there is a discount
                print(f"    Check discount")
                if (dr, dc) == (-1, 0) or (dr, dc) == (1, 0):
                    # Check if we already added a fence next to this
                    if (nr, nc-1) not in fences and (nr, nc+1) not in fences:
                        print(f"    No discount!")
                        different_sides += 1
                elif (dr, dc) == (0, -1) or (dr, dc) == (0, 1):
                    # Check if we already added a fence next to this
                    if (nr-1, nc) not in fences and (nr+1, nc) not in fences:
                        print(f"    No discount!")
                        different_sides += 1
            elif not visited[nr][nc]:
                print(f"    {grid[nr][nc]} => Added region: ({nr}, {nc})")
                visited[nr][nc] = True
                queue.append((nr, nc))
        print(f"\n")

    return area * different_sides

total_fence_cost = 0
for row in range(rows):
    for col in range(cols):
        print(f"grid[row={row}][col={col}]: {grid[row][col]}")
        if not visited[row][col]:
            plant = grid[row][col]
            fence_cost = bfs(row, col, plant)
            total_fence_cost += fence_cost
print(f"Total Fence Cost: {total_fence_cost}")
# Correct answer: 807190 too low