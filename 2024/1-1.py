#https://adventofcode.com/2024/day/1
import numpy as np
from collections import deque
from collections import Counter
import copy
import sympy

# Open and read the file as a single string
with open('1i.txt', 'r') as file:
    lines = file.readlines()

# grid = open('25-input-test.txt').read().splitlines()
# grid = open('1-1i.txt').read().splitlines()
# grid = [list(x) for x in open('24-input-test.txt').read().strip().splitlines()]
# grid = [list(x) for x in open('22-input.txt').read().strip().splitlines()]
# grid = np.array([[c for c in line] for line in open('22-input-test.txt').readlines()])
# grid = np.array([[c for c in line] for line in open('22-input.txt').readlines()])
# print("Line: ", grid)

# Split string into lists
left_list = []
right_list = []
for line in lines:
    num1 = int(line.split()[0])
    num2 = int(line.split()[1])
    # To speed it up next time I can do:
    # num1, num2 = map(int, line.split())
    left_list.append(num1)
    right_list.append(num2)

# Sort lists
left_list.sort()
right_list.sort()

# Count distances
distances = []
for i, num1 in enumerate(left_list):
    num2 = right_list[i]
    distances.append(abs(num1 - num2))
# To speed it up next time I can do:
# for num1, num2 in zip(left_list, right_list):
#     distances.append(abs(num1 - num2))
# Most hardcore is this:
# distances = [abs(a - b) for a, b in zip(left_list, right_list)]

# Debug print
# for i, (num1, num2, distance) in enumerate(zip(left_list, right_list, distances), start=1):
#     print(f"The {i}-smallest number in the left list is {num1}, and in the right list is {num2}. The distance between them is {distance}.")

# Sum all distances
total_distance = sum(distances)
print(f"\nSum distances: {total_distance}")
# Correct answer: 2000468