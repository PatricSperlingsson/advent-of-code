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
reg_a_orig = int(lines[0].split(': ')[1])
reg_b = int(lines[1].split(': ')[1])
reg_c = int(lines[2].split(': ')[1])
prog = [int(instr) for instr in lines[4].split(': ')[1].split(',')]
prog_len = len(prog)
print(f"reg_a_orig: {reg_a_orig}")
print(f"reg_b: {reg_b}")
print(f"reg_c: {reg_c}")
print(f"prog: {prog}")
print(f"prog_len: {prog_len}")

# Go though the program and the input:
# 2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0
# 2,4: 0: reg_b = reg_a % 8
# 1,1: reg_b ^= 1
# 7,5: reg_c = reg_a // (2 ** reg_b) 
# 4,6: reg_b ^= reg_c
# 0,3: reg_a //= 8
# 1,4: reg_b ^= 4
# 5,5: out reg_b % 8
# 3,0: jnz 0

wanted_output = prog
# reg_a_init = 202972175280682
reg_a_init = 0
reg_a_cnt = 0
best = 0
while True:
    reg_a_init += 1
    if reg_a_init % 10000000 == 0:
        print(reg_a_init)
    # reg_a = reg_a_init
    # First time took forever but I got len 9 of len 16:
    # 73935402 => oct(73935402) == 0o432025052
    # I can reuse octets since our program adds one octet each time:
    #    => reg_a = reg_a_init * 8**5 + 0o25052

    # Second time took much fast but got stuck eventually at len 12:
    #    => reg_a_old = 4320
    #    => reg_a = reg_a_init * 8**9 + 0o432025052
    
    # Third time I solved it, but I got 04 at the ends so I add it to speed it up:
    #    => reg_a = reg_a_init * 8**11 + 0o04432025052
    reg_a = reg_a_init * 8**11 + 0o04432025052
    reg_a_old = reg_a
    reg_a_cnt += 1
    reg_b = 0
    reg_c = 0
    wrong_output = False
    instr_ptr = 0
    output = []
    output_index = 0
    while instr_ptr < prog_len:
        opcode = prog[instr_ptr]
        operand = prog[instr_ptr + 1]
        instr_ptr += 2
        # print(f"opcode: {opcode}")
        # print(f"operand: {operand}")

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
                if wanted_output[output_index] == operand % 8 and output_index == len(output):
                    output_index += 1
                    output.append(operand % 8)
                else:
                    wrong_output = True
                    break
            elif operand == 4:
                # print(f"  wanted_output[output_index]: {wanted_output[output_index]}")
                # print(f"  output: {reg_a % 8}")
                if wanted_output[output_index] == reg_a % 8 and output_index == len(output):
                    output_index += 1
                    output.append(reg_a % 8)
                else:
                    wrong_output = True
                    break
            elif operand == 5:
                output.append(reg_b % 8)
                if output[len(output)-1] != wanted_output[len(output)-1]:
                    if len(output) > best:
                        best = len(output)
                        print(f"5:5: reg_a: {reg_a}, oct(reg_a_old): {oct(reg_a_old)}, best: {best}, len(wanted_output): {len(wanted_output)}")
                    break
            elif operand == 6:
                if wanted_output[output_index] == reg_c % 8 and output_index == len(output):
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
    if wanted_output == output:
        print(f"reg_a_old: {reg_a_old}, bin: {bin(reg_a_old)}")
        break

print(",".join(map(str, output)))
# Correct Answer: 202972175280682