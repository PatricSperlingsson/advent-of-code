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
def simulate_guard(walls, start_pos, start_dir):
    queue = deque()
    visited = set()
    
    # Start
    queue.append((start_pos, start_dir))
    visited.add((start_pos, start_dir))
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
            return False
        if (nx, ny) in walls:
            # Rotate clockwise
            ndir = (directions_order.index(direction) + 1) % 4
            next_state = ((x, y), directions_order[ndir])
        else:
            # Continue forward
            next_state = ((nx, ny), direction)

        # Already visited? => loop detected
        if next_state in visited:
            return True

        # Continue forward
        queue.append(next_state)
        visited.add(next_state)
    # No loop found
    return False

# Loop through all locations except walls and start_pos
possible_positions = set()
for y in range(height):
    for x in range(width):
        if grid[y][x] == '#':
            continue
        elif grid[y][x] == '^':
            continue
        else:
            possible_positions.add((x, y))

created_loop = 0
for pos in possible_positions:
    if simulate_guard(walls | {pos}, start_pos, start_dir):
        created_loop += 1
print(f"Created loops: {created_loop}")
# Correct answer: 2008
        