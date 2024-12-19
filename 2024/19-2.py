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

visited = {}
def count_build_design(design, patterns):
    if design in visited:
        return visited[design]

    if not design:
        return 1

    ans = 0
    for pattern in patterns:
        if design.startswith(pattern):
            # If the design starts with the pattern, recurse with the remaining part of the design
            ans += count_build_design(design[len(pattern):], patterns)

    visited[design] = ans

    return ans

    # Solution with strange loop:
    # n = len(design)
    # dp = [0] * (n + 1)  # dp[i] = number of ways to form design[:i]
    # dp[0] = 1  # Base case: 1 way to form an empty design

    # for i in range(1, n + 1):
    #     for pattern in patterns:
    #         # If pattern fits at the end
    #         if design[:i].endswith(pattern):
    #             print(f"found pattern: {pattern} \tin design: {design[:i]}, \tdp[{i}]:{dp[i]} += dp[{i} - {len(pattern)}]: {dp[i - len(pattern)]}")
    #             dp[i] += dp[i - len(pattern)]
    # print(f"dp: {dp}")
    # return dp[n]

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

    found += count_build_design(str(design), atp_list)

print(f"found: {found}")
# Correct Answer: 616234236468263