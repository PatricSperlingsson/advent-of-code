#https://adventofcode.com/2024/day/8
import numpy as np
from collections import deque
from collections import Counter
import copy
import sympy

# Open and read the file as a single string
with open('8i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

rows = len(lines)
cols = len(lines[0])
print(f"rows: {rows}")
print(f"cols: {cols}")

# Store antenna frequencies with their position
# Dictionary with Key: Frequency, Value: list of coordinates (x, y)
antenna_freq = {}
for row in range(rows):
    for col in range(cols):
        if lines[col][row] != '.':
            if lines[col][row] not in antenna_freq:
                antenna_freq[lines[col][row]] = []
            antenna_freq[lines[col][row]].append((row, col))
print(f"antenna_freq: {antenna_freq}")

antinode_pos = set()
for freq, positions in antenna_freq.items():
    num_antennas_this_freq = len(positions)

    # Minimum antennas are 2 to create antinodes
    if (num_antennas_this_freq < 2):
        continue

    print(f"freq: {freq}")

    for a1 in range(num_antennas_this_freq - 1):
        for a2 in range(a1 + 1, num_antennas_this_freq):
            x1, y1 = positions[a1]
            x2, y2 = positions[a2]
            print(f"  x1, y1: {x1, y1}")
            print(f"  x2, y2: {x2, y2}")
            
            # Antinode locations
            dx, dy = x1 - x2, y1 - y2
            print(f"    dx, dy: {dx, dy}")
            
            ax1, ay1 = x1 + dx, y1 + dy
            ax2, ay2 = x2 - dx, y2 - dy
            print(f"    ax1, ay1: {ax1, ay1}")
            print(f"    ax2, ay2: {ax2, ay2}")
            
            if 0 <= ax1 < cols and 0 <= ay1 < rows:
                antinode_pos.add((ax1, ay1))
            if 0 <= ax2 < cols and 0 <= ay2 < rows:
                antinode_pos.add((ax2, ay2))

print(f"Total unique antinode locations: {len(antinode_pos)}")
# Correct answer: 392