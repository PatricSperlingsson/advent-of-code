#https://adventofcode.com/2024/day/6
import numpy as np
from collections import deque
from collections import Counter
import copy
import sympy

# Open and read the file as a single string
with open('6i', 'r') as file:
    grid = [line.strip() for line in file.readlines()]
print(f"grid: {grid}")

start_pos = None
start_dir = None
walls = set()

# Parse map
height = len(grid)
width = len(grid[0])
for y in range(height):
    for x in range(width):
        if grid[y][x] == '#':
            walls.add((x, y))
        elif grid[y][x] == '^':
            start_pos = (x, y)
            start_dir = '^'

print(f"Walls: {walls}")
print(f"start_pos: {start_pos}")

# Simulate guard
queue = deque()
visited = set()

# Start
queue.append((start_pos, start_dir))
visited.add(start_pos)
#                   Up, Right, Down, Left
directions_order = ['^', '>', 'v', '<']
directions_map = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

while queue:
    (x, y), direction = queue.popleft()
    dx, dy = directions_map[direction]

    nx = x + dx
    ny = y + dy
    if not (0 <= nx < width and 0 <= ny < height):
        # Guard exits the map
        continue
    if (nx, ny) in walls:
        # Rotate clockwise
        ndir = (directions_order.index(direction) + 1) % 4
        queue.append(((x, y), directions_order[ndir]))
        continue

    # Continue forward
    queue.append(((nx, ny), direction))
    visited.add((nx, ny))

print(f"Visited: {len(visited)}")
# Correct answer: 5516