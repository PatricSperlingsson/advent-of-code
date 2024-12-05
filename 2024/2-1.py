#https://adventofcode.com/2024/day/2
import numpy as np
from collections import deque
from collections import Counter
import copy
import sympy

# Open and read the file as a single string
with open('2i.txt', 'r') as file:
    lines = file.readlines()

# Convert each line into a list of integers
data = [list(map(int, line.split())) for line in lines]
print("Processed data:", data)

# grid = open('25-input-test.txt').read().splitlines()
# grid = open('1-1i.txt').read().splitlines()
# grid = [list(x) for x in open('24-input-test.txt').read().strip().splitlines()]
# grid = [list(x) for x in open('22-input.txt').read().strip().splitlines()]
# grid = np.array([[c for c in line] for line in open('22-input-test.txt').readlines()])
# grid = np.array([[c for c in line] for line in open('22-input.txt').readlines()])
# print("Line: ", grid)

# Example Input
# data = [
#     [7, 6, 4, 2, 1], # Safe
#     [1, 2, 7, 8, 9], # Unsafe, diff > 2
#     [9, 7, 6, 2, 1], # Unsafe, diff > 2
#     [1, 3, 2, 4, 5], # Unsafe, direction changes
#     [8, 6, 4, 4, 1], # Unsafe, diff < 1
#     [1, 3, 6, 7, 9]  # Safe
# ]
# Above should give 2 safe

safe_count = 0

# Iterate each line
for line in data:
    is_safe = True
    direction = None

    # Compare each level with the next one
    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]

        # Check if the difference is out of the allowed range (1 to 3)
        if abs(diff) < 1 or abs(diff) > 3:
            is_safe = False
            break

        # Determine the direction for the first valid pair
        if direction is None:
            if diff > 0:
                direction = "increasing"
            elif diff < 0:
                direction = "decreasing"

        # Check if the direction is consistent
        if direction == "increasing" and diff < 0:
            is_safe = False
            break
        if direction == "decreasing" and diff > 0:
            is_safe = False
            break

    # Increment safe counter
    if is_safe:
        safe_count += 1

print(f"Safe reports: {safe_count}")
# Correct answer: 598