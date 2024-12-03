#https://adventofcode.com/2024/day/3
import numpy as np
from collections import deque
from collections import Counter
import copy
import re
import sympy

# Open and read the file as a single string
with open('3i.txt', 'r') as file:
    data = file.read()
# print("Processed data:", data)

# grid = open('25-input-test.txt').read().splitlines()
# grid = open('1-1i.txt').read().splitlines()
# grid = [list(x) for x in open('24-input-test.txt').read().strip().splitlines()]
# grid = [list(x) for x in open('22-input.txt').read().strip().splitlines()]
# grid = np.array([[c for c in line] for line in open('22-input-test.txt').readlines()])
# grid = np.array([[c for c in line] for line in open('22-input.txt').readlines()])
# print("Line: ", grid)

# Parse data for mul(mul1,mul2)

# Create Regex pattern
pattern = re.compile(r"(mul\((\d+),(\d+)\))|do\(\)|don't\(\)")
print(pattern)

mul_enabled = True
sum_of_products = 0
for match in pattern.finditer(data):
    # print(match)
    instruction = match.group(0)
    if instruction == "do()":
        mul_enabled = True
        print("do()")
        # print(f"  mg0: {match.group(0)}")
        # print(f"  mg1: {match.group(1)}")
        # print(f"  mg2: {match.group(2)}")
        # print(f"  mg3: {match.group(3)}")
    elif instruction == "don't()":
        mul_enabled = False
        print("don't()")
        # print(f"  mg0: {match.group(0)}")
        # print(f"  mg1: {match.group(1)}")
        # print(f"  mg2: {match.group(2)}")
        # print(f"  mg3: {match.group(3)}")
    elif "mul" in instruction and mul_enabled:
        print("mul")
        # print(f"  mg0: {match.group(0)}")
        # print(f"  mg1: {match.group(1)}")
        # print(f"  mg2: {match.group(2)}")
        # print(f"  mg3: {match.group(3)}")
        sum_of_products += int(match.group(2)) * int(match.group(3))

print(f"Sum of products: {sum_of_products}")
# Correct answer: 95846796