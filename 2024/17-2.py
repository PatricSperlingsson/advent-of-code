#https://adventofcode.com/2024/day/17
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
with open('17i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

# Parse input
reg_a = int(lines[0].split(': ')[1])
reg_b = int(lines[1].split(': ')[1])
reg_c = int(lines[2].split(': ')[1])
prog = [int(instr) for instr in lines[4].split(': ')[1].split(',')]
prog_len = len(prog)
print(f"reg_a: {reg_a}")
print(f"reg_b: {reg_b}")
print(f"reg_c: {reg_c}")
print(f"prog: {prog}")
print(f"prog_len: {prog_len}")

wanted_output = [0, 3, 5, 4, 3, 0]
# wanted_output = [7, 3, 0, 5, 7, 1, 4, 0, 5]
reg_a = 117440
while True:
    wrong_output = False
    instr_ptr = 0
    output = []
    output_index = 0
    while instr_ptr < prog_len:
        opcode = prog[instr_ptr]
        operand = prog[instr_ptr + 1]
        instr_ptr += 2
    
        if opcode == 0: # adv
            # print(f"adv: reg_a += reg_a // (2 ** operand)")
            if operand < 4:
                reg_a //= 2 ** operand
            elif operand == 4:
                reg_a //= 2 ** reg_a
            elif operand == 5:
                reg_a //= 2 ** reg_b
            elif operand == 6:
                reg_a //= 2 ** reg_c
        elif opcode == 1: # bxl
            # print(f"bxl: reg_b += reg_b ^ operand")
            reg_b ^= operand
        elif opcode == 2: # bst
            # print(f"bst: reg_b = operand % 8")
            if operand < 4:
                reg_b = operand % 8
            elif operand == 4:
                reg_b = reg_a % 8
            elif operand == 5:
                reg_b = reg_b % 8
            elif operand == 6:
                reg_b = reg_c % 8
        elif opcode == 3: # jnz
            # print(f"jnz: if reg_a != 0, jump to operand")
            if reg_a != 0:
                instr_ptr = operand
        elif opcode == 4: # bxc
            # print(f"bxc: reg_b = reg_b ^ reg_c")
            reg_b ^= reg_c
        elif opcode == 5: # out
            # print(f"out: output = operand % 8")
            if operand < 4:
                if wanted_output[output_index] == operand % 8:
                    output_index += 1
                    output.append(operand % 8)
                else:
                    wrong_output = True
                    break
            elif operand == 4:
                if wanted_output[output_index] == reg_a % 8:
                    output_index += 1
                    output.append(reg_a % 8)
                else:
                    wrong_output = True
                    break
            elif operand == 5:
                if wanted_output[output_index] == reg_b % 8:
                    output_index += 1
                    output.append(reg_b % 8)
                else:
                    wrong_output = True
                    break
            elif operand == 6:
                if wanted_output[output_index] == reg_c % 8:
                    output_index += 1
                    output.append(reg_c % 8)
                else:
                    wrong_output = True
                    break
        elif opcode == 6: # bdv
            # print(f"bdv: reg_b = reg_a // (2 ** operand)")
            if operand < 4:
                reg_b = reg_a // (2 ** operand)
            elif operand == 4:
                reg_b = reg_a // (2 ** reg_a)
            elif operand == 5:
                reg_b = reg_a // (2 ** reg_b)
            elif operand == 6:
                reg_b = reg_a // (2 ** reg_c)
        elif opcode == 7: # cdv
            # print(f"cdv: reg_c = reg_a // (2 ** operand)")
            if operand < 4:
                reg_c = reg_a // (2 ** operand)
            elif operand == 4:
                reg_c = reg_a // (2 ** reg_a)
            elif operand == 5:
                reg_c = reg_a // (2 ** reg_b)
            elif operand == 6:
                reg_c = reg_a // (2 ** reg_c)
    if wrong_output:
        reg_a += 1
    else:
        print(f"reg_a should be: {reg_a}")
        break

print(",".join(map(str, output)))
# Correct Answer: 7,3,0,5,7,1,4,0,5