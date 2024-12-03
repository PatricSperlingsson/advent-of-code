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

found_xmas = 0
for r in range(1, row_l-1):
    for c in range(1, col_l-1):
        # print(f"r: {r}")
        if data[r][c] != 'A':
            continue
        
        # Search for 'MAS' or 'SAM' from 'A'
        if data[r-1][c-1] + data[r+1][c+1] != "MS" and data[r-1][c-1] + data[r+1][c+1] != "SM":
            continue

        if data[r+1][c-1] + data[r-1][c+1] != "MS" and data[r+1][c-1] + data[r-1][c+1] != "SM":
            continue
        
        found_xmas += 1


print(f"found_xmas:: {found_xmas}")
# Correct answer 2504