#https://adventofcode.com/2025/day/4
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
from itertools import product
from functools import cache

# Open and read the file as a single string
# Outputs a list from the delimitier '\n'
with open('../../inputs/2025/4i.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]
print(f"grid: {grid}")



height = len(grid)
width = len(grid[0])

directions = [(-1,-1), (0,-1), (1,-1),
              (-1, 0),         (1, 0),
              (-1, 1), (0, 1), (1, 1)]

rolls_access = 0
# Parse map
for y in range(height):
    for x in range(width):
        if grid[y][x] == '@':
            
            neighbors = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    if grid[ny][nx] == '@':
                        neighbors += 1
                
            if neighbors < 4:
                rolls_access += 1
    
print(f"rolls_access: {rolls_access}")
# Correct answers: 13 and 1351
