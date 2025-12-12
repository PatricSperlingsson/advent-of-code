# https://adventofcode.com/2025/day/9
import numpy as np
from collections import deque, Counter, defaultdict
# Priority Queue
from heapq import heappop, heappush
import copy
import sympy
# Recursive function with memorization
from functools import lru_cache
# @lru_cache(None)
# Creating functions
# from math import gcd
import math
from sympy import symbols, Eq, solve
from itertools import product
from functools import cache

# --- Read input file ---
# Open and read the file as a single string
# Outputs a list split by the delimiter '\n'
with open('../../inputs/2025/9i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

# Convert each line "x,y" into integer coordinates
coords = []
for line in lines:
    x, y = map(int, line.split(","))
    coords.append((x, y))
print(f"len: {len(coords)}")


# --- Scanline fill ---
def scanline_fill(polygon):
    """
    Perform scanline polygon fill.
    For each horizontal line (y), compute intersections with polygon edges.
    Pair intersections into intervals (a,b) representing filled spans.
    Return:
      - y_list: all y rows
      - intervals_per_row: list of intervals for each row
    """
    xs, ys = zip(*polygon)
    ymin, ymax = min(ys), max(ys)

    intervals_per_row = []  # list of lists of (a,b) intervals
    y_list = list(range(ymin, ymax+1))

    for y in y_list:
        intersections = []
        j = len(polygon) - 1
        # Loop over polygon edges
        for i in range(len(polygon)):
            xi, yi = polygon[i]
            xj, yj = polygon[j]
            # Skip horizontal edges
            if yi == yj:
                j = i
                continue
            # Check if edge crosses this scanline
            if (yi <= y < yj) or (yj <= y < yi):
                # Compute intersection x coordinate
                x_int = (xj - xi) * (y - yi) / (yj - yi) + xi
                intersections.append(x_int)
            j = i
        intersections.sort()

        # Pair intersections into intervals
        intervals = []
        for k in range(0, len(intersections)-1, 2):
            # ceil returns the smallest integer that is >= the left intersection
            a = math.ceil(intersections[k])
            # floor returns the largest integer that is <= the right intersection
            b = math.floor(intersections[k+1])
            if a <= b:
                intervals.append((a, b))
        intervals_per_row.append(intervals)

    # Collect all x boundaries for compression
    x_marks = set()
    for ints in intervals_per_row:
        for a, b in ints:
            x_marks.add(a)
            x_marks.add(b+1)

    return y_list, intervals_per_row



# --- Anchor-based rectangle search with interval validation ---
def anchored_rectangle_search(coords, intervals_per_row, ymin, anchor):
    """
    Find the largest rectangle inside the polygon anchored at a given point.
    Anchor is the bottom-right corner (x2,y2).
    For each candidate top-left corner (x1,y1):
      - Validate that all rows between y2..y1 cover [x1..x2].
      - If valid, compute area and update best result.
    """
    x2, y2 = anchor
    largest_area = 0
    best_pair = None

    for (x1, y1) in coords:
        # Candidate must be above and to the left of anchor
        if x1 <= x2 and y1 >= y2:
            valid = True
            # Check row coverage
            for y in range(y2, y1 + 1):
                intervals = intervals_per_row[y - ymin]
                covered = any(a <= x1 and b >= x2 for a, b in intervals)
                if not covered:
                    valid = False
                    break
            if valid:
                area = (x2 - x1 + 1) * (y1 - y2 + 1)
                if area > largest_area:
                    largest_area = area
                    best_pair = ((x1, y1), (x2, y2))
    return largest_area, best_pair


# --- Main ---
y_list, intervals_per_row = scanline_fill(coords)

# Looking at the input file the coordinate (x2, y2) = (94969, 50092)
# This is the anchor point (the "mouth of the pacman")
# From the input I could also see that x1 < x2 and y1 > y2 .
anchor = (94969, 50092)

largest_area, best_pair = anchored_rectangle_search(coords, intervals_per_row, min(y_list), anchor)

print(f"largest_area: {largest_area}, best_pair: {best_pair}")
# largest_area: 1396494456, best_pair: ((4658, 65554), (94969, 50092))
# Correct answers: 24 and 1396494456