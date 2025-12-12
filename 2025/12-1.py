#https://adventofcode.com/2025/day/12
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
# from math import gcd
import math
from sympy import symbols, Eq, solve
from itertools import product
from functools import cache
import re

# Open and read the file as a single string
# Outputs a list from the delimitier '\n'
# THE TEST TAKES LIKE 5 MIN TO COMPLETE!!!!!!
# THE FULL TAKES LIKE 10 MIN TO COMPLETE!!!!!!
with open('../../inputs/2025/12it.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

# Read shapes
shapes = []
shape = set()
shape_ongoing = 0
num_shapes_parsed = 0

# Regions
regions = []
# Quantities
quantities = []
region_index = 0
for line in lines:
    if line == '':
        shape_ongoing = 0
        if num_shapes_parsed < 6:
            shapes.append(frozenset(shape))
            num_shapes_parsed += 1
        continue

    # Parse Shapes
    if line.endswith(':') and num_shapes_parsed < 6:
        y = 0
        shape = set()
        shape_ongoing = 1
        # print(f"new_shape")
        continue
    elif shape_ongoing and num_shapes_parsed < 6:
        # Shapes
        for x, char in enumerate(line):
            if char == '#':
                shape.add((x, y))
        y += 1
        continue

    # After 6 shapes have been parsed: Parse Regions and Quantity
    width = int(line.split('x')[0])
    height = int(line.split('x')[1].split(':')[0])
    regions.append((width, height))

    quantity = [int(x) for x in line.split('x')[1].split(': ')[1].split(' ')]
    quantities.append(quantity)

print(f"shapes: {shapes}")
print(f"regions: {regions}")
print(f"quantities: {quantities}")

# Debug
print('shapes:')
for shape in shapes:
    xs = [x for x,y in shape]; ys = [y for x,y in shape]
    for y in range(min(ys), max(ys)+1):
        print(''.join('#' if (x,y) in shape else '.' for x in range(min(xs), max(xs)+1)))
    print('\n')


# Upgraded set below to frozenset so that I could deduplicate the lists

def move_into_my_coord_system(rotated_shape):
    minx = min(x for x,y in rotated_shape)
    miny = min(y for x,y in rotated_shape)
    return frozenset(((x - minx, y - miny) for x, y in rotated_shape))

def rotate_90_cw(shape):
    rotated_shape = frozenset((-y, x) for x, y in shape)
    return move_into_my_coord_system(rotated_shape)

def rotate_180_cw(shape):
    rotated_shape = frozenset((-x, -y) for x, y in shape)
    return move_into_my_coord_system(rotated_shape)

def rotate_270_cw(shape):
    rotated_shape = frozenset((y, -x) for x, y in shape)
    return move_into_my_coord_system(rotated_shape)

def flip_along_y_axis(shape):
    flipped = frozenset((-x, y) for x, y in shape)
    return move_into_my_coord_system(flipped)

# Store all rotations of the shapes
unique_rotated_shapes = []
for shape in shapes:
    all_rotations_for_one_shape = []
    all_rotations_for_one_shape.append(shape)

    # Rotate 90 CW from my origo (0, 0) with y increasing downwards =>
    # (x,y) => (-y,x), then move shape into my positive coordinate system
    r90 = rotate_90_cw(shape)
    all_rotations_for_one_shape.append(r90)
    
    r180 = rotate_180_cw(shape)
    all_rotations_for_one_shape.append(r180)
    
    r270 = rotate_270_cw(shape)
    all_rotations_for_one_shape.append(r270)
    
    flip = flip_along_y_axis(shape)
    all_rotations_for_one_shape.append(flip)
    
    flip90 = rotate_90_cw(flip)
    all_rotations_for_one_shape.append(flip90)
    
    flip180 = rotate_180_cw(flip)
    all_rotations_for_one_shape.append(flip180)
    
    flip270 = rotate_270_cw(flip)
    all_rotations_for_one_shape.append(flip270)
    
    # Remove duplications
    unique = list({r for r in all_rotations_for_one_shape})
    unique_rotated_shapes.append(unique)


# Debug
print('rotated_shapes:')
for idx, shapes in enumerate(unique_rotated_shapes):
    print(f"Shape {idx} has {len(shapes)} orientations")
    for shape in shapes:
        xs = [x for x,y in shape]; ys = [y for x,y in shape]
        for yy in range(min(ys), max(ys)+1):
            print(''.join('#' if (x,yy) in shape else '.' for x in range(min(xs), max(xs)+1)))
        print()

def placements_for_orientation(orient, W, H):
    xs = [x for x,y in orient]; ys = [y for x,y in orient]
    w = max(xs)+1; h = max(ys)+1
    placements = []
    for dy in range(H-h+1):
        for dx in range(W-w+1):
            placement = {(x+dx, y+dy) for x,y in orient}
            placements.append(placement)
    return placements

def placements_for_shape(shape_index, W, H):
    all_orients = unique_rotated_shapes[shape_index]
    all_places = []
    for orient in all_orients:
        all_places.extend(placements_for_orientation(orient, W, H))
    return all_places

def find_solution(width, height, quantity):
    # quick check: if total cells required > board area, impossible
    total_cells = sum(len(shape) * q for shape, q in zip(shapes, quantity))
    if total_cells > width * height:
        # impossible: too many cells required
        return None

    placements_by_type = [
        placements_for_shape(i, width, height)
        for i in range(len(unique_rotated_shapes))
    ]
    solution = []
    seen = set()  # memoization of visited states

    def dfs(filled, counts_left):
        state = (frozenset(filled), tuple(counts_left))
        if state in seen:
            return False
        seen.add(state)

        # success when all presents have been placed
        if all(c == 0 for c in counts_left):
            return True

        # try placing each present type that still has copies left
        for t_idx, count in enumerate(counts_left):
            if count == 0:
                continue
            for place in placements_by_type[t_idx]:
                if place.isdisjoint(filled):
                    counts_left[t_idx] -= 1
                    solution.append((t_idx, place))
                    if dfs(filled | place, counts_left):
                        return True
                    solution.pop()
                    counts_left[t_idx] += 1
        return False

    if dfs(set(), quantity[:]):
        return solution
    return None

def render_solution(W, H, sol):
    grid = [['.' for _ in range(W)] for _ in range(H)]
    for t_idx, place in sol:
        ch = str(t_idx)
        for (x, y) in place:
            grid[y][x] = ch
    for row in grid:
        print(''.join(row))

regions_possible = 0
for (width, height), quantity in zip(regions, quantities):
    print(f"({width}, {height}), {quantity}")
    sol = find_solution(width, height, quantity)
    if sol is not None:
        regions_possible += 1
        print("Solution found!")
        render_solution(width, height, sol)  # <-- show the tiling
    else:
        print("No solution.")
    print()

print(f"regions_possible: {regions_possible}")
# Correct answers: 2 and 541
