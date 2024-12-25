#https://adventofcode.com/2024/day/25
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
with open('../../inputs/2024/25i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

locks = []
keys = []

# Parse input
is_lock = None
n_list = [0] * 5
print(f"n_list: {n_list}")
rows_read = 0
for line in lines:
    if line == '':
        is_lock = None
        n_list = [0] * 5
        rows_read = 0
        continue

    if is_lock is None:
        if line == '#####':
            is_lock = True
            print(f"lock")
            continue
        elif line == '.....':
            is_lock = False
            print(f"key")
            continue
        else:
            print(f"error")
            qwerty()

    if is_lock:
        if rows_read == 5:
            locks.append(n_list)
            continue
        for col, char in enumerate(line):
            if char == '#':
                n_list[col] = n_list[col] + 1
    else:
        if rows_read == 5:
            keys.append(n_list)
            continue
        for col, char in enumerate(line):
            if char == '#':
                n_list[col] = n_list[col] + 1
    rows_read += 1
print(f"locks: {locks}")
print(f"keys: {keys}")

fit = 0
for lock in locks:
    for key in keys:
        for i in range(5): # i = 0..4
            if lock[i] + key[i] > 5:
                break
            if i == 4:
                fit += 1
                break
print(f"fit: {fit}")
# Correct answer: 3057