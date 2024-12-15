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

rows = len(warehouse)
cols = len(warehouse[0])
print(f"rows: {rows}")
print(f"cols: {cols}")

# Parse start locations
robot_pos = None
box_pos = set()
for r, row in enumerate(warehouse):
    for c, char in enumerate(row):
        if char == '@':
            robot_pos = (r, c)
        elif char == 'O':
            box_pos.add((r, c))
print(f"robot_pos: {robot_pos}")
print(f"box_pos: {box_pos}")

directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

# Move robots
for move in move_sequence:
    dr, dc = directions[move]
    nrp = (robot_pos[0] + dr, robot_pos[1] + dc)
    print(f"nrp: {nrp}")

    if warehouse[nrp[0]][nrp[1]] == '#':
        continue

    if nrp not in box_pos:
        robot_pos = nrp
        continue

    # Box in front move boxes until:
        # reaching wall => no move for anyone
        # reaching empty => move everyone
    nbp = nrp
    while warehouse[nbp[0]][nbp[1]] != '#' and nbp in box_pos:
        nbp = (nbp[0] + dr, nbp[1] + dc)
    if warehouse[nbp[0]][nbp[1]] == '#':
        # No move
        continue
    box_pos.remove(nrp)
    box_pos.add(nbp)
    robot_pos = nrp

gps_coordinates = 0
for r, c in box_pos:
    gps_coordinates += r * 100 + c
print(f"gps_coordinates: {gps_coordinates}")
# Correct Answer: 1476771