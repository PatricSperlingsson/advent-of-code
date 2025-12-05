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

ranges = []
for line in lines:
    # Read fresh ingredients
    if line == '':
        break
    nstart = int(line.split('-')[0])
    nend = int(line.split('-')[1])

    new_start = nstart
    new_end = nend
    new_ranges = []
    for start, end in ranges:
        if nstart <= end and nend >= start:
            # Overlaps completely or partial
            new_start = min(new_start, start)
            new_end = max(new_end, end)
        else:
            # No overlap, add it separately
            new_ranges.append((start, end))
    new_ranges.append((new_start, new_end))
    ranges = new_ranges

fresh = 0
for start, end in ranges:
    fresh += end - start + 1
print(f"fresh: {fresh}")
# Correct answers: 14 and 357674099117260
