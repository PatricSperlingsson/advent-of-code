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
    # lines = [line.strip() for line in file.readlines()]
    # Keep spaces:
    grid = [line.strip('\n') for line in file]
print(f"grid: {grid}")

num_vert = len(grid)
print(f"num_vert: {num_vert}")
num_hor = len(grid[0])
print(f"num_hor: {num_hor}")


answer = 0
grand = 0
start_add = 0
start_mul = 0
for i in range(num_hor):
    op = grid[num_vert-1][i]
    if op == '+':
        grand += answer
        answer = 0
        start_add = 1
        start_mul = 0
    elif op == '*':
        grand += answer
        answer = 1
        start_mul = 1
        start_add = 0

    if start_add:
        add = ''
        for j in range(num_vert-1):
            if grid[j][i] != ' ':
                add += grid[j][i]
        if add != '':
            answer += int(add)
    elif start_mul:
        mul = ''
        for j in range(num_vert-1):
            if grid[j][i] != ' ':
                mul += grid[j][i]
        if mul != '':
            answer *= int(mul)

grand += answer
print(f"grand: {grand}")
# Correct answers: 3263827 and 11044319475191
