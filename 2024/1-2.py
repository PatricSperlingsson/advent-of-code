#https://adventofcode.com/2024/day/1
import numpy as np
from collections import deque
from collections import Counter
import copy
import sympy

# Open and read the file as a single string
with open('1-1i.txt', 'r') as file:
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



# Count occurances
right_counter = Counter(right_list)

similarity_score = 0
for num in left_list:
# for i in range(len(left_list)):
    # num = left_list[i]
    similarity_score += num * right_counter[num]

# Summera alla avstånd
print(f"\nsimilarity_score: {similarity_score}")
# Correct answer: 18567089