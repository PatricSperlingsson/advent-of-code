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
    start = (r, c, None, None)
    queue = deque([start])
    visited[r][c] = True
    area = 0
    region = set()
    different_sides = 0
    
    while queue:
        r_prev, c_prev, dr_prev, dc_prev = queue.popleft()
        area += 1
        
        for dr, dc in directions:
            nr, nc = r_prev + dr, c_prev + dc
            print(f"  r_prev({r_prev}), dr({dr}), nr({nr})       c_prev({c_prev}), dc({dc}), nc({nc})")
            
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != plant:
                print(f"    Check discount")
                # Check if there is a discount
                if dr_prev == None or dc_prev == None:
                    different_sides += 1
                    print(f"    Added sides: ({dr_prev},{dc_prev} => {nr},{nc})")
                else:
                    # Left, Right
                    if (dr_prev, dc_prev) == (0, -1) or (dr_prev, dc_prev) == (0, 1):
                        # Up from r_prev, c_prev
                        nrUp, ncUp = r_prev - 1, c_prev + 0
                        print(f"    nrUp{nrUp}, ncUp{ncUp}")
                        if (nrUp, ncUp) not in region:
                            # Down from r_prev, c_prev
                            nrDown, ncDown = r_prev + 1, c_prev + 0
                            if (nrDown, ncDown) not in region:
                                different_sides += 1
                                print(f"    Added sides: ({dr_prev},{dc_prev} => {nr},{nc})")

                    # print(f"    nr1, nc1: {nr1}, {nc1}")
                    # if 0 <= nr1 > rows and 0 <= nc1 > cols and (nr1, nc1) not in region:
                    #     nr2, nc2 = r_prev - 2*dr, c_prev - 2*dc
                    #     if 0 <= nr2 > rows and 0 <= nc2 > cols and (nr2, nc2) not in region:
                    #         different_sides += 1
                    
            elif not visited[nr][nc]:
                print(f"    {grid[nr][nc]} => Added region: ({nr}, {nc})")
                visited[nr][nc] = True
                region.add((nr, nc))
                queue.append((nr, nc, dr, dc))
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
# Correct answer: 50308 too low