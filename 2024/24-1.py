#https://adventofcode.com/2024/day/24
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
with open('../../inputs/2024/24i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
# print(f"lines: {lines}")

inputs = defaultdict()
gates = []

reading_part_one = True
for line in lines:
    # print(f"line: {line}")
    if line == '':
        reading_part_one = False
        continue
    if reading_part_one:
        wire, v = line.split(": ")
        inputs[wire] = int(v)
    else:
        func = line.split(' ')[1]
        wire_one = line.split(' ')[0]
        wire_two = line.split(' ')[2]
        wire_out = line.split(' ')[4]
        gates.append((func, wire_one, wire_two, wire_out))
print(f"inputs: {inputs}")
print(f"gates: {gates}")

# Process gates in order, remove processed and delay those with dependencies
while gates: # Added to support delay
    for gate in gates:
        func, wire_one, wire_two, wire_out = gate
        if wire_one not in inputs or wire_two not in inputs: # Added to support delay
            continue # Added to support delay

        if func == 'AND':
            inputs[wire_out] = inputs[wire_one] & inputs[wire_two]
        elif func == 'OR':
            inputs[wire_out] = inputs[wire_one] | inputs[wire_two]
        elif func == 'XOR':
            inputs[wire_out] = inputs[wire_one] ^ inputs[wire_two]

        # Remove processed gate
        gates.remove((func, wire_one, wire_two, wire_out)) # Added to support delay
print(f"inputs: {inputs}")

# Get all inputs with 'z', sort them, convert to binary string and finally convert to 10 base
z_bits = []
for key, value in inputs.items():
    if key.startswith('z'):
        z_bits.append((int(key[1:]), value))
z_bits = sorted(z_bits, key=lambda x: x[0])
print(f"z_bits: {z_bits}")
binary_str = ''.join(str(value) for _, value in z_bits)[::-1]
print(f"binary_str: {binary_str}")
decimal = int(binary_str, 2)
print(decimal)
# Correct answer: 45923082839246