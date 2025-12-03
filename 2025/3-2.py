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
# print(f"lines: {lines}")

total_output_jolt = 0
for line in lines:
    digits_left = len(line)-12
    stack = []
    for digit in line:
        while digits_left and stack and stack[-1] < digit:
            stack.pop()
            digits_left -= 1
        stack.append(digit)

    total_output_jolt += int(''.join(stack[:12]))

print(f"total_output_jolt: {total_output_jolt}")
# Correct answers: 3121910778619 and 171388730430281
