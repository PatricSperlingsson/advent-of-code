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


# Initial positions
# width = 11
# height = 7
width = 101
width_half = 11 // 2
print(f"width_half: {width_half}")
height = 103
time = 100

# Move robots
robots_end = []
for robot in robots:
    sx, sy = robot[0]
    vx, vy = robot[1]
    ex, ey = (sx + vx*100) % width, (sy + vy*100) % height
    robots_end.append((ex, ey))
print(f"robots_end: {robots_end}")

# Calculate Robots in each Quadrants
q1, q2, q3, q4 = 0, 0, 0, 0
for robot_end in robots_end:
    x, y = robot_end
    if x <= width // 2 - 1 and y <= height // 2 - 1:
        q1 += 1
    elif x > width // 2 and y <= height // 2 - 1:
        q2 += 1
    elif x <= width // 2 - 1 and y > height // 2:
        q3 += 1
    elif x > width // 2 and y > height // 2:
        q4 += 1
print(f"q1: {q1}, q2: {q2}, q3: {q3}, q4: {q4}")

print(f"Safety factor: {q1*q2*q3*q4}")
# Correct Answer: 218965032