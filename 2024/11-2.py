#https://adventofcode.com/2024/day/11
import numpy as np
from collections import deque, defaultdict
from collections import Counter
import copy
import sympy
from functools import lru_cache

# Open and read the file as a single string
with open('11i.txt', 'r') as file:
    line = file.readline().strip()
    numbers = [int(num) for num in line.split()]
print("numbers:", numbers)

# Help from Internet, I should add this to a function:
# from functools import lru_cache
# # Recursive function with memorization
# @lru_cache(None)

# Recursive function with memorization
@lru_cache(None)
def count_stones(number, blinks):
    if blinks == 0:
        # We are done
        return 1

    if number == 0:
        return count_stones(1, blinks - 1)
    elif len(str(number)) % 2 == 0:
        number_str = str(number)
        first_number_len = len(number_str) // 2
        left_number = int(number_str[:first_number_len])
        right_number = int(number_str[first_number_len:])
        return count_stones(left_number, blinks - 1) + count_stones(right_number, blinks - 1)
    else:
       return count_stones(number * 2024, blinks - 1)

blinks = 75
num_stones = 0
for number in numbers:
    num_stones += count_stones(number, blinks)

print(f"num_stones: {num_stones}")
# Correct answer: 259112729857522