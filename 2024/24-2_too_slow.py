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



# Compute addition of the two binary inputs
x_bits = []
for key, value in inputs.items():
    if key.startswith('x'):
        x_bits.append((int(key[1:]), value))
x_bits = sorted(x_bits, key=lambda x: x[0])
x_binary_str = ''.join(str(value) for _, value in x_bits)[::-1]
print(f"x_binary_str: {x_binary_str}")

y_bits = []
for key, value in inputs.items():
    if key.startswith('y'):
        y_bits.append((int(key[1:]), value))
y_bits = sorted(y_bits, key=lambda x: x[0])
y_binary_str = ''.join(str(value) for _, value in y_bits)[::-1]
print(f"y_binary_str: {y_binary_str}")

# Create the wanted answer from the addition
x_int = int(x_binary_str, 2)
y_int = int(y_binary_str, 2)
sum_int = x_int + y_int
wanted_binary_str = bin(sum_int)[2:]
print(f"wanted_binary_str: {wanted_binary_str}")



# Perform 4 swaps
for i in range(len(gates) - 1):
    for j in range(i + 1, len(gates)):
        func_i, wire_one_i, wire_two_i, wire_out_i = gates[i]
        func_j, wire_one_j, wire_two_j, wire_out_j = gates[j]
        gates[i] = (func_i, wire_one_i, wire_out_i, wire_two_j)
        gates[j] = (func_j, wire_one_j, wire_out_j, wire_two_i)
        for k in range(len(gates) - 1):
            if k == i or k == j:
                continue
            for l in range(k + 1, len(gates)):
                if l == i or l == j:
                    continue
                func_k, wire_one_k, wire_two_k, wire_out_k = gates[k]
                func_l, wire_one_l, wire_two_l, wire_out_l = gates[l]
                gates[k] = (func_k, wire_one_k, wire_out_k, wire_two_l)
                gates[l] = (func_l, wire_one_l, wire_out_l, wire_two_k)
                for m in range(len(gates) - 1):
                    if m == i or m == j or m == k or m == l:
                        continue
                    for n in range(m + 1, len(gates)):
                        if n == i or n == j or n == k or n == l:
                            continue
                        func_m, wire_one_m, wire_two_m, wire_out_m = gates[m]
                        func_n, wire_one_n, wire_two_n, wire_out_n = gates[n]
                        gates[m] = (func_m, wire_one_m, wire_out_m, wire_two_n)
                        gates[n] = (func_n, wire_one_n, wire_out_n, wire_two_m)
                        for o in range(len(gates) - 1):
                            if o == i or o == j or o == k or o == l or o == m or o == n:
                                continue
                            for p in range(o + 1, len(gates)):
                                if p == i or p == j or p == k or p == l or p == m or p == n:
                                    continue
                                func_o, wire_one_o, wire_two_o, wire_out_o = gates[o]
                                func_p, wire_one_p, wire_two_p, wire_out_p = gates[p]
                                gates[o] = (func_o, wire_one_o, wire_out_o, wire_two_p)
                                gates[p] = (func_p, wire_one_p, wire_out_p, wire_two_o)




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
                                # print(f"inputs: {inputs}")
                                
                                # Get all inputs with 'z', sort them, convert to binary string and finally convert to 10 base
                                z_bits = []
                                for key, value in inputs.items():
                                    if key.startswith('z'):
                                        z_bits.append((int(key[1:]), value))
                                z_bits = sorted(z_bits, key=lambda x: x[0])
                                # print(f"z_bits: {z_bits}")
                                binary_str = ''.join(str(value) for _, value in z_bits)[::-1]
                                print(f"binary_str: {binary_str}")
                                if binary_str == wanted_binary_str:
                                    print("Found swaps: {wire_two_i} -> {wire_two_j}, {wire_two_k} -> {wire_two_l}, {wire_two_m} -> {wire_two_n}, {wire_two_o} -> {wire_two_p}")



# Correct answer: 