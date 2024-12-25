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
# gates = []
gates = {}

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
        # gates.append((func, wire_one, wire_two, wire_out))
        gates[wire_out] = (func, wire_one, wire_two)
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
print(f"wanted_binary_str:\t {wanted_binary_str}")



# # Process gates in order, remove processed and delay those with dependencies
# while gates: # Added to support delay
#     for gate in gates:
#         func, wire_one, wire_two, wire_out = gate
#         if wire_one not in inputs or wire_two not in inputs: # Added to support delay
#             continue # Added to support delay

#         if func == 'AND':
#             inputs[wire_out] = inputs[wire_one] & inputs[wire_two]
#         elif func == 'OR':
#             inputs[wire_out] = inputs[wire_one] | inputs[wire_two]
#         elif func == 'XOR':
#             inputs[wire_out] = inputs[wire_one] ^ inputs[wire_two]

#         # Remove processed gate
#         gates.remove((func, wire_one, wire_two, wire_out)) # Added to support delay
# # print(f"inputs: {inputs}")

# # Get all inputs with 'z', sort them, convert to binary string and finally convert to 10 base
# z_bits = []
# for key, value in inputs.items():
#     if key.startswith('z'):
#         z_bits.append((int(key[1:]), value))
# z_bits = sorted(z_bits, key=lambda x: x[0])
# # print(f"z_bits: {z_bits}")
# binary_error_str = ''.join(str(value) for _, value in z_bits)[::-1]
# print(f"binary_error_str:\t {binary_error_str}")



# x:  1010110110 0100 000110 11010 101111011 11 010101111
# y:  1010000010 0011 011111 10100 111001000 10 000011111
# 
# w: 10100111000 0111 100110 01111 101000100 01 011001110
# c: 10100111000 1000 100110 10000 101000100 10 011001110
# 
# z09 should be 1 but in current:
# gates[181]: y09(0) AND x09(1) -> z09(0)
# This one must be swapped to someone that gives 1!
# So who can give 1?
# 1 AND 1
# 1 XOR 0
# 0 XOR 1
# 1 OR 1
# 1 OR 0
# 0 OR 1
# 
# Switch out in gates[181] gives below:
#  26  10100111000 1000 100110 10000 101000100 01 011001110
#  53  10100111000 1000 100110 10000 101000100 01 011001110
#  74  10100111000 1000 100110 10000 101000100 01 011001110
# 209  10100111000 1000 100110 10000 101000100 01 011001110
# print(f"gate 9: {gates[181]}")
# 
# =>
# w: 10100111000 0111 100110 01111 101000100 01 011001110
# c:  0100111000 1000 100110 10000 101000100 01 011001110



# Perform 1 swap
# indexes to swap out 181
# index_to_fix_bit_10_and_11 = []
# for i in range(len(gates)):
#     if i == 181:
#         continue
#     gates_test = copy.deepcopy(gates)
#     inputs_test = copy.deepcopy(inputs)
#     func_i, wire_one_i, wire_two_i, wire_out_i = gates_test[i]
#     func_j, wire_one_j, wire_two_j, wire_out_j = gates_test[181]
#     gates_test[i] = (func_i, wire_one_i, wire_two_i, wire_out_j)
#     gates_test[181] = (func_j, wire_one_j, wire_two_j, wire_out_i)
#     print(f"wire_out_i: {wire_out_i}")
#     print(f"wire_out_j: {wire_out_j}")

#     # Process gates_test in order, remove processed and delay those with dependencies
#     while gates_test: # Added to support delay
#         for gate in gates_test:
#             func, wire_one, wire_two, wire_out = gate
#             if wire_one not in inputs_test or wire_two not in inputs_test: # Added to support delay
#                 continue # Added to support delay
    
#             if func == 'AND':
#                 inputs_test[wire_out] = inputs_test[wire_one] & inputs_test[wire_two]
#             elif func == 'OR':
#                 inputs_test[wire_out] = inputs_test[wire_one] | inputs_test[wire_two]
#             elif func == 'XOR':
#                 inputs_test[wire_out] = inputs_test[wire_one] ^ inputs_test[wire_two]
    
#             # Remove processed gate
#             gates_test.remove((func, wire_one, wire_two, wire_out)) # Added to support delay
#     # print(f"inputs_test: {inputs_test}")
    
#     # Get all inputs_test with 'z', sort them, convert to binary string and finally convert to 10 base
#     z_bits = []
#     for key, value in inputs_test.items():
#         if key.startswith('z'):
#             z_bits.append((int(key[1:]), value))
#     z_bits = sorted(z_bits, key=lambda x: x[0])
#     # print(f"z_bits: {z_bits}")
#     binary_str = ''.join(str(value) for _, value in z_bits)[::-1]
#     print(f"binary_str: {binary_str}")
#     if binary_str[-10] == '1' and binary_str[-11] == '0':
#         index_to_fix_bit_10_and_11.append(i)
#         print(f"binary_str: {binary_str} fixed")
# index_to_fix_bit_10_and_11 = [26, 53, 74, 209]
# print(f"index_to_fix_bit_10_and_11: {index_to_fix_bit_10_and_11}")

# index_to_fix_bit_21_to_25 = []
# for i in index_to_fix_bit_10_and_11:
#     for k in range(len(gates) - 1):
#         if k == 181 or k == i:
#             continue
#         for l in range(len(gates)):
#             if l == k or l == 181 or l == i:
#                 continue
#             gates_test = copy.deepcopy(gates)
#             inputs_test = copy.deepcopy(inputs)
#             func_i, wire_one_i, wire_two_i, wire_out_i = gates_test[i]
#             func_j, wire_one_j, wire_two_j, wire_out_j = gates_test[181]
#             gates_test[i] = (func_i, wire_one_i, wire_two_i, wire_out_j)
#             gates_test[181] = (func_j, wire_one_j, wire_two_j, wire_out_i)
#             func_k, wire_one_k, wire_two_k, wire_out_k = gates_test[k]
#             func_l, wire_one_l, wire_two_l, wire_out_l = gates_test[l]
#             gates_test[k] = (func_k, wire_one_k, wire_two_k, wire_out_l)
#             gates_test[l] = (func_l, wire_one_l, wire_two_l, wire_out_k)

#             # Process gates_test in order, remove processed and delay those with dependencies
#             while gates_test: # Added to support delay
#                 for gate in gates_test:
#                     func, wire_one, wire_two, wire_out = gate
#                     if wire_one not in inputs_test or wire_two not in inputs_test: # Added to support delay
#                         continue # Added to support delay
            
#                     if func == 'AND':
#                         inputs_test[wire_out] = inputs_test[wire_one] & inputs_test[wire_two]
#                     elif func == 'OR':
#                         inputs_test[wire_out] = inputs_test[wire_one] | inputs_test[wire_two]
#                     elif func == 'XOR':
#                         inputs_test[wire_out] = inputs_test[wire_one] ^ inputs_test[wire_two]
            
#                     # Remove processed gate
#                     gates_test.remove((func, wire_one, wire_two, wire_out)) # Added to support delay
#             # print(f"inputs_test: {inputs_test}")
            
#             # Get all inputs_test with 'z', sort them, convert to binary string and finally convert to 10 base
#             z_bits = []
#             for key, value in inputs_test.items():
#                 if key.startswith('z'):
#                     z_bits.append((int(key[1:]), value))
#             z_bits = sorted(z_bits, key=lambda x: x[0])
#             # print(f"z_bits: {z_bits}")
#             binary_str = ''.join(str(value) for _, value in z_bits)[::-1]
#             print(f"binary_str: {binary_str}")
#             if binary_str[-21] == '1' and binary_str[-22] == '1' and binary_str[-23] == '1' and binary_str[-24] == '1' and binary_str[-25] == '0':
#                 index_to_fix_bit_21_to_25.append(i)
#                 print(f"binary_str: {binary_str} fixed")
# print(f"index_to_fix_bit_21_to_25: {index_to_fix_bit_21_to_25}")

def two_digits_padding(char, num):
    return char + str(num).rjust(2, "0")

def check_recarry(wire, num):
    # print(f"check_recarry: {}, {}", wire, num)
    if wire not in gates: return False
    op, x, y = gates[wire]
    if op != "AND": return False
    return check_intermediate_xor(x, num) and check_carry_bit(y, num) or check_intermediate_xor(y, num) and check_carry_bit(x, num)

def check_direct_carry(wire, num):
    # print(f"check_direct_carry: {}, {}", wire, num)
    if wire not in gates: return False
    op, x, y = gates[wire]
    if op != "AND": return False
    return sorted([x, y]) == [two_digits_padding("x", num), two_digits_padding("y", num)]

def check_carry_bit(wire, num):
    # print(f"check_carry_bit: {}, {}", wire, num)
    if wire not in gates: return False
    op, x, y = gates[wire]
    if num == 1:
        if op != "AND": return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR": return False
    return check_direct_carry(x, num - 1) and check_recarry(y, num - 1) or check_direct_carry(y, num - 1) and check_recarry(x, num - 1)

def check_intermediate_xor(wire, num):
    # print(f"check_intermediate_xor: {}, {}", wire, num)
    if wire not in gates: return False
    op, x, y = gates[wire]
    if op != "XOR": return False
    return sorted([x, y]) == [two_digits_padding("x", num), two_digits_padding("y", num)]

def check_z_out(wire, num):
    # print(f"check_z_out: {}, {}", wire, num)
    if wire not in gates: return False
    op, x, y = gates[wire]
    if op != "XOR": return False
    if num == 0: return sorted([x, y]) == ["x00", "y00"]
    return check_intermediate_xor(x, num) and check_carry_bit(y, num) or check_intermediate_xor(y, num) and check_carry_bit(x, num)

def progress_z_out():
    z_out_id = 0
    while True:
        if z_out_id < 10:
            if not check_z_out('z0' + str(z_out_id), z_out_id):
                break
        else:
            if not check_z_out('z' + str(z_out_id), z_out_id):
                break
        z_out_id += 1
    return z_out_id

swaps = []
for swap_id in range(4):
    current = progress_z_out()
    for out_x in gates:
        if swap_id == 0:
            out_x = 'z09'
        for out_y in gates:
            if out_x == out_y: continue
            # Try switch
            gates[out_x], gates[out_y] = gates[out_y], gates[out_x]
            if progress_z_out() > current:
                # Switch is better, keep it
                break
            # Switch back
            gates[out_x], gates[out_y] = gates[out_y], gates[out_x]
        else:
            continue
        break
    print(f"switched {out_x} with {out_y}")
    swaps += [out_x, out_y]

print(",".join(sorted(swaps)))
# Correct answer: jgb,rkf,rrs,rvc,vcg,z09,z20,z24