#https://adventofcode.com/2025/day/3
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
with open('../../inputs/2025/3i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

total_output_jolt = 0
for line in lines:
    largest_jolt = 0
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            # print(f"{i}{j}")
            current_joltage = int(line[i] + line[j])
            print(current_joltage)
            if current_joltage > largest_jolt:
                largest_jolt = current_joltage
    total_output_jolt += largest_jolt
print(f"total_output_jolt: {total_output_jolt}")
# Correct answers: 357 and 17281
