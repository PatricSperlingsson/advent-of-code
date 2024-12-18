#https://adventofcode.com/2024/day/18
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
with open('18i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
for line in lines:
    coords = [tuple(map(int, line.split(","))) for line in lines]
# coords = [tuple(map(int, line.strip().split(','))) for line in file.readlines()]

print(f"coords: {coords}")
num_coords = len(coords)
print(f"num_coords: {len(coords)}")

# width = 7
# height = 7
# start = (0, 0)
# end = (6, 6)
# bytes_simulation = 12
width = 71
height = 71
start = (0, 0)
end = (70, 70)
bytes_simulation = 1024

# Directions: Down,   Right,  Up,      Left
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(grid, start, end):
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited = set()
    visited.add((start))

    while queue:
        x, y, s = queue.popleft()
        
        # We are done
        if (x, y) == end:
            return s
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= x < width and 0 <= y < height and grid[y][x] == 0:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, s + 1))
    return -1

# Add simulation
grid = [[0 for _ in range(height)] for _ in range(height)]
for i, (x, y) in enumerate(coords, start=1):
    grid[y][x] = 1

    shortest_path = bfs(grid, start, end)
    if shortest_path == -1:
        print(f"coordinate that prevents exit: {x},{y}")
        break
# Correct Answer: 20,12