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

# Directions  Left,    Right,  Up,      Down
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Initialize visited
visited = [[False for _ in range(cols)] for _ in range(rows)]

def bfs(x, y, plant):
    start = (x, y)
    queue = deque([start])
    visited[x][y] = True
    area = 0
    perimeter = 0
    different_sides = 0
    
    while queue:
        x, y = queue.popleft()
        area += 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != plant:
                perimeter += 1
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

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
# Correct answer: 1433460