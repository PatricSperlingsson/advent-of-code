#https://adventofcode.com/2025/day/6
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
with open('../../inputs/2025/6i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

num_vert = 0
grid = []
for line in lines:
    num_vert += 1
    horizontal = line.split()
    grid.append(horizontal)

print(f"num_vert: {num_vert}")
num_hor = len(grid[0])
print(f"num_hor: {num_hor}")

grand = 0
for i in range(num_hor):
    if grid[num_vert-1][i] == '+':
        answer = 0
        for j in range(num_vert-1):
            answer += int(grid[j][i])
        grand += answer
    else: # *
        answer = 1
        for j in range(num_vert-1):
            answer *= int(grid[j][i])
        grand += answer

print(f"grand: {grand}")
# Correct answers: 4277556 and 6417439773370
