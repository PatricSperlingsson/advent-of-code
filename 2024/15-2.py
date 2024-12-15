#https://adventofcode.com/2024/day/15
import numpy as np
from collections import deque, defaultdict
from collections import Counter
import copy
import sympy
# Recursive function with memorization
from functools import lru_cache
#@lru_cache(None)
# Creating functions
from math import gcd
from sympy import symbols, Eq, solve

# Open and read the file as a single string
with open('15i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

# Warehouse
warehouse = []
moves = []
part1 = True
for line in lines:
    if part1:
        if line != '':
            warehouse.append(list(line))
        else:
            part1 = False
    else:
        moves.append(line)
move_sequence = ''.join(moves)
print(f"warehouse: {warehouse}")
print(f"move_sequence: {move_sequence}")

# Double Wide Warehouse
robot_pos = None
dww = []
for row in warehouse:
    nrow = []
    for char in row:
        if char == '#':
            nrow.append('##')
        elif char == 'O':
            nrow.append('[]')
        elif char == '.':
            nrow.append('..')
        elif char == '@':
            nrow.append('@.')
    dww.append(''.join(nrow))
print("double_wide_warehouse:")
for row in dww:
    print(row)
# Convert to list so that I can update robot and box positions
dww_list = [list(row) for row in dww]
for row in dww_list:
    print(row)

rows = len(dww)
cols = len(dww[0])
print(f"rows: {rows}")
print(f"cols: {cols}")

# Parse start locations
robot_pos = None
for r in range(rows):
    for c in range(cols):
        if dww[r][c] == '@':
            robot_pos = (r, c)
print(f"robot_pos: {robot_pos}")

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

# Move robots
for move in move_sequence:
    dr, dc = directions[move]
    targets = [robot_pos]  # Start with the robot position
    go = True

    # Collect all affected positions (robot and boxes)
    for cr, cc in targets:
        nr = cr + dr
        nc = cc + dc

        print(f"targets: {targets}")

        # Prevent re-checking positions
        if (nr, nc) in targets: 
            continue

        char = dww_list[nr][nc]

        if char == "#":  # Wall
            go = False
            break
        elif char == "[":  # Left part of a box
            if dww_list[nr][nc + 1] != "]":  # Validate right side of box
                go = False
                break
            targets.append((nr, nc))      # Left
            targets.append((nr, nc + 1))  # Right
        elif char == "]":  # Right part of a box
            if dww_list[nr][nc - 1] != "[":  # Validate left side of box
                go = False
                break
            targets.append((nr, nc))      # Right
            targets.append((nr, nc - 1))  # Left

    if not go: 
        continue  # Skip this move if invalid

    print(f"Before updates, targets: {targets}")
    print(f"Num Targets: {len(targets)}")
    for row in dww_list:
        print(row)

    left = False
    right = False
    if (dr, dc) == (0, -1):# <
        dww_list[robot_pos[0]][robot_pos[1]] = "."
        robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)
        dww_list[robot_pos[0]][robot_pos[1]] = "@"
        for i in range(1, len(targets)):
            nr, nc = robot_pos[0] + dr * i, robot_pos[1] + dc * i
            if right == False:
                dww_list[nr][nc] = "]"
                right = True
            else:
                dww_list[nr][nc] = "["
                right = False
    if (dr, dc) == (0, 1):# >
        dww_list[robot_pos[0]][robot_pos[1]] = "."
        robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)
        dww_list[robot_pos[0]][robot_pos[1]] = "@"
        for i in range(1, len(targets)):
            nr, nc = robot_pos[0] + dr * i, robot_pos[1] + dc * i
            if left == False:
                dww_list[nr][nc] = "["
                left = True
            else:
                dww_list[nr][nc] = "]"
                left = False
    if (dr, dc) == (-1, 0):# ^
        # Sort based on first parameter "row"
        sorted_targets = sorted(targets, key=lambda x: x[0], reverse=False)
        print(f"Before updates, sorted_targets: {sorted_targets}")
        for i, (tr, tc) in enumerate(sorted_targets):
            if dww_list[tr][tc] == "[":
                dww_list[tr + dr][tc + dc] = "["
                dww_list[tr][tc] = "."
            elif dww_list[tr][tc] == "]":
                dww_list[tr + dr][tc + dc] = "]"
                dww_list[tr][tc] = "."
        dww_list[robot_pos[0]][robot_pos[1]] = "."
        robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)
        dww_list[robot_pos[0]][robot_pos[1]] = "@"
    if (dr, dc) == (1, 0):# v
        # Sort based on first parameter "row"
        sorted_targets = sorted(targets, key=lambda x: x[0], reverse=True)
        print(f"Before updates, sorted_targets: {sorted_targets}")
        for i, (tr, tc) in enumerate(sorted_targets):
            if dww_list[tr][tc] == "[":
                dww_list[tr + dr][tc + dc] = "["
                dww_list[tr][tc] = "."
            elif dww_list[tr][tc] == "]":
                dww_list[tr + dr][tc + dc] = "]"
                dww_list[tr][tc] = "."
        dww_list[robot_pos[0]][robot_pos[1]] = "."
        robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)
        dww_list[robot_pos[0]][robot_pos[1]] = "@"
    print("After updates:")
    for row in dww_list:
        print(row)

# Final computation
result = sum(100 * r + c for r in range(rows) for c in range(cols) if dww_list[r][c] == "[")
print("Final result:", result)
# Correct Answer: 1468005