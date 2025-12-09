#https://adventofcode.com/2025/day/9
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
# from math import gcd
import math
from sympy import symbols, Eq, solve
from itertools import product
from functools import cache

# Open and read the file as a single string
# Outputs a list from the delimitier '\n'
with open('../../inputs/2025/9i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

coords = []
for line in lines:
    x, y = map(int, line.split(","))
    coords.append((x, y))
print(f"coords: {coords}")

largest_area = 0
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        # print(f"abs(x2 - x1): {abs(x2 - x1)}")
        # print(f"  abs(y2 - y1): {abs(y2 - y1)}")
        if area > largest_area:
            largest_area = area

print(f"largest_area: {largest_area}")
# Correct answers: 50 and 4763040296
