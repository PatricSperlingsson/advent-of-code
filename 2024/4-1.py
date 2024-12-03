#https://adventofcode.com/2024/day/4
import numpy as np
from collections import deque
from collections import Counter
import copy
import sympy

# Open and read the file as a single string
with open('4i.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]
print(f"data: {data}")

row_l = len(data)
col_l = len(data[0])
print(f"row_l: {row_l}")
print(f"col_l: {col_l}")

directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
              (-1, 1), (1, 1), (1, -1), (-1, -1)]

def check_direction(r, c, dr, dc):
    for i in range(4):
        nr = r + i*dr
        nc = c + i*dc

        if 0 <= nr < row_l and 0 <= nc < col_l:
            if i == 0:
                if data[nr][nc] != 'X':
                    return False
            if i == 1:
                if data[nr][nc] != 'M':
                    return False
            if i == 2:
                if data[nr][nc] != 'A':
                    return False
            if i == 3:
                if data[nr][nc] != 'S':
                    return False
                return True

found_xmas = 0
for r in range(row_l):
    for c in range(col_l):
        # print(f"r: {r}")
        for dr, dc in directions:
            if check_direction(r, c, dr, dc):
                found_xmas += 1

print(f"found_xmas:: {found_xmas}")
# Correct answer 2504