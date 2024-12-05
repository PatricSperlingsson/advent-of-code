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

# Get the matches in a list
# matches = re.findall(r"mul\(\d+,\d+\)", data)
# Get the matches as tuples
mul_matches = re.findall(r"mul\((\d+),(\d+)\)", data)
print(mul_matches)

sum_of_products = 0
for mul1, mul2 in mul_matches:
    sum_of_products += int(mul1) * int(mul2)
# To speed up I can do this next time:
# sum_of_products = sum(int(mul1) * int(mul2) for mul1, mul2 in mul_matches)

print(f"Sum of products: {sum_of_products}")
# Correct answer: 167650499