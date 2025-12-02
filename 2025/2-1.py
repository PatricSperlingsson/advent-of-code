#https://adventofcode.com/2025/day/2
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
with open('../../inputs/2025/2i.txt', 'r', encoding='utf-8') as file:
    content = file.read()  # read the whole file as a single string
    lines = [item.strip() for item in content.split(',') if item.strip()]

print(f"lines: {lines}")

inv_ids = []
for ranges in lines:
    start = int(ranges.split('-')[0])
    end = int(ranges.split('-')[1])
    print(f"{start} - {end}")
    
    for i in range(start, end + 1):
        s = str(i)
        if len(s) % 2 != 0:
            continue
        if s[:len(s)//2] == s[len(s)//2:]:
            inv_ids.append(i)

print(f"inv_ids: {inv_ids}")
print(f"Sum inv_ids: {sum(inv_ids)}")
# Correct answers: 1227775554 and 18595663903