#https://adventofcode.com/2025/day/1
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
with open('../../inputs/2025/1i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
# print(f"lines: {lines}")

dial = 50
count_zero = 0

for line in lines:
    # print(f"line: {line}")
    direction = line[0]
    # print(f"  direction: {direction}")
    steps = int(line[1:])
    # print(f"  steps: {steps}")
    if direction == 'R':
        for _ in range(steps):
            dial = (dial + 1) % 100
            if dial == 0:
                count_zero += 1
    else:
        for _ in range(steps):
            dial = (dial - 1) % 100
            if dial == 0:
                count_zero += 1
    print(f"{line} => {dial}")
 
print(f"count_zero: {count_zero}")
# Correct answers: 6 and 6789
