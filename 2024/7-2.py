#https://adventofcode.com/2024/day/7
import numpy as np
from collections import deque
from collections import Counter
import copy
import sympy

# Open and read the file as a single string
with open('7i', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

total_calibration_result = 0

def evaluate_recursively(numbers, target, current_result, index):
    # Are we done?
    if current_result > target:
        return False
    if index == len(numbers):
        return current_result == target

    next_number = numbers[index]

    # Try +
    # print(f"Test: +")
    if evaluate_recursively(numbers, target, current_result + next_number, index + 1):
        return True

    # Try *
    # print(f"Test: *")
    if evaluate_recursively(numbers, target, current_result * next_number, index + 1):
        return True

    # Try ||
    # print(f"Test: ||")

    # print(f"  numbers: {numbers}")
    # print(f"  target: {target}")
    # print(f"  current_result: {current_result}")
    # print(f"  index: {index}")

    if evaluate_recursively(numbers, target, int(str(current_result) + str(next_number)), index + 1):
        return True

    return False

for equation in lines:
    test_value = int(equation.split(': ')[0])
    print(f"test_value: {test_value}")
    numbers = equation.split(': ')[1].split(' ')
    numbers = [int(number) for number in numbers]
    # I can also do this in one line:
    # numbers = list(map(int, equation.split(': ')[1].split(' ')))
    print(f"numbers: {numbers}")

    # Create all possible equations

    # Start recursive evaluation
    if evaluate_recursively(numbers, test_value, numbers[0], 1):
        total_calibration_result += test_value

print(f"Total Calibration Result: {total_calibration_result}")
# Correct answer is: 254136560217241