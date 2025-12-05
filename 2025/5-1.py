#https://adventofcode.com/2025/day/5
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
with open('../../inputs/2025/5i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

fresh = 0
read_ranges = True
# fresh_ingredients = set() too slow
ranges = []
for line in lines:
    # Read fresh ingredients first
    if read_ranges:
        if line == '':
            read_ranges = False
            continue
        start = int(line.split('-')[0])
        end = int(line.split('-')[1])
        ranges.append((start, end))
        # for i in range(start, end + 1):
        #     fresh_ingredients.add(i)
        # fresh_ingredients.update(range(start, end + 1))
        continue

    # Read available ingredients
    ingredient = int(line)
    for start, end in ranges:
        if start <= ingredient <= end:
            fresh += 1
            break

print(f"fresh: {fresh}")
# Correct answers: 13 and 770
