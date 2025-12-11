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
# PLEASE NOTE THAT 11-1 and 11-2 HAVE DIFFERENT TEST INPUTS!!!
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

# Debug: List all
for i, j in devices.items():
    print(f"{i} -> {j}")

#  Count outs
def count_outs(start, devices, current_path):
    if current_path == None:
        current_path = []
    # Create a new list everytime
    current_path = current_path + [start]

    if start == 'out':
        print(f"current_path: {current_path}")
        return 1

    total_outs = 0
    for output in devices[start]:
       total_outs += count_outs(output, devices, current_path)

    return total_outs

leads_to_out = count_outs("you", devices, None)
print(f"leads_to_out: {leads_to_out}")
# Correct answers: 5 and 603
