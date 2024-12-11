#https://adventofcode.com/2024/day/11
import numpy as np
from collections import deque, defaultdict
from collections import Counter
import copy
import sympy

# Open and read the file as a single string
with open('11i.txt', 'r') as file:
    line = file.readline().strip()
    numbers = [int(num) for num in line.split()]
print("numbers:", numbers)

blinks = 75
for blink in range(1, blinks+1):
    print(f"blink: {blink}")
    next_numbers = []
    for number in numbers:
        if number == 0:
            next_numbers.append(1)
        elif len(str(number)) % 2 == 0:
            number_str = str(number)
            first_number_len = len(number_str) // 2
            left_number = int(number_str[:first_number_len])
            right_number = int(number_str[first_number_len:])
            # print(f"  left_number: {left_number}")
            # print(f"  right_number: {right_number}")
            next_numbers.append(left_number)
            next_numbers.append(right_number)
        else:
            next_numbers.append(number * 2024)
    numbers = next_numbers
    # print(f"numbers: {numbers}")
    
print(f"numbers: {numbers}")
print(f"Number of stones: {len(numbers)}")
# Correct answer: 217812