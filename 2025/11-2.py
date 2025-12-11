#https://adventofcode.com/2025/day/11
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
import re

# Open and read the file as a single string
# Outputs a list from the delimitier '\n'
with open('../../inputs/2025/11i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

devices = {}
for line in lines:
    device = line.split(':')[0]
    print(f"device: {device}")
    outputs = line.split(':')[1].strip().split(' ')
    print(f"outputs: {outputs}")
    devices[device] = outputs


# BELOW IS CORRECT I THINK BUT TOO SLOW!!!
#  Count outs
# def count_outs(start, devices, current_path):
#     if current_path == None:
#         current_path = []

#     # Protection against loops
#     if start in current_path:
#         return 0

#     # Create a new list everytime
#     path = current_path + [start]

#     if start == 'out':
#         if 'dac' in path and 'fft' in path:
#             print(f"path: {path}")
#             return 1
#         return 0

#     # Protection against none existing devices
#     if start not in devices:
#         return 0

#     total_outs = 0
#     for output in devices[start]:
#        total_outs += count_outs(output, devices, path)

#     return total_outs

# leads_to_out = count_outs("svr", devices, None)
# print(f"leads_to_out: {leads_to_out}")



#  Count outs
def count_outs_dag(start, devices):
    @lru_cache(maxsize=None)
    def dfs(node, saw_dac, saw_fft):
        saw_dac = saw_dac or (node == "dac")
        saw_fft = saw_fft or (node == "fft")

        if node == "out":
            return 1 if (saw_dac and saw_fft) else 0

        if node not in devices:
            return 0

        total = 0
        for nxt in devices[node]:
            total += dfs(nxt, saw_dac, saw_fft)
        return total

    return dfs(start, False, False)

leads_to_out = count_outs_dag("svr", devices)
print(f"leads_to_out: {leads_to_out}")
# Correct answers: 2 and 380961604031372
