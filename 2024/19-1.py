#https://adventofcode.com/2024/day/19
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

# Open and read the file as a single string
with open('19i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

def can_build_design(design, atp_list):
    # Mark current built designs as True
    last_successful = [False] * (len(design))
    print(f"  last_successful: {last_successful}")

    for p in range(len(design)):
        if p == 0 or last_successful[p-1]:
            for atp in atp_list:
                # Check if the substring of the design matches the available towel pattern
                if design[p:p + len(atp)] == atp:
                    print(f"Found {atp} at pos: {p}")
                    last_successful[p + len(atp)-1] = True

    print(f"  last_successful: {last_successful}")
    return last_successful[-1]

atp_dict = {}
atp_list = lines[0].split(', ')
print(f"atp_list: {atp_list}")
for atp in atp_list:
    atp_dict[atp] = 10**9
print(f"atp_dict: {atp_dict}")

designs = len(lines)-2
print(f"designs: {designs}")
found = 0
for ddi in range(2, designs + 2, 1):
    design = lines[ddi]
    print(f"design: {design}")

    if can_build_design(design, atp_list):
        print("  Found")
        found += 1

print(f"Found: {found}")
# Correct Answer: 311