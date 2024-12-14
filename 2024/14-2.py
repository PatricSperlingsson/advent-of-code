#https://adventofcode.com/2024/day/14
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
with open('14i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

robots = []
for line in lines:
    px, py = line.split(' v=')[0].split('p=')[1].split(',')
    vx, vy = line.split(' v=')[1].split(',')
    print(f"pos: {px},{py}, v: {px},{py}")
    robots.append(((int(px), int(py)), (int(vx), int(vy))))
print(f"robots: {robots}")
print(f"robots[0]: {robots[0]}")
print(f"robots[0]pos: {robots[0][0]}")
print(f"robots[0]v: {robots[0][1]}")

width = 101
height = 103
time = 0
while (True):
    time += 1
    # Print all robots
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for robot in robots:
        sx, sy = robot[0]
        vx, vy = robot[1]
        ex, ey = (sx + vx * time) % width, (sy + vy * time) % height
        grid[ey][ex] = '#'
    
    # Search for the main tree, width at least 1 and height least 10?
    for col in range(width):
        found_tree = 0
        for row in range(height):
                if grid[row][col] == '#':
                    found_tree += 1
                    if found_tree == 10:
                        break
                else:
                    found_tree = 0
        if found_tree == 10:
            break

    if found_tree == 10:
        print("\033[H\033[J", end="") 
        print(f"time: {time}")
        # Print current grid for visual confirmation:
        for row in grid:
            print(''.join(row))
        # Wait for spacebar press to continue
        input("Press Enter to advance by 1 second...") 

# Visual confirmation at time: 7037