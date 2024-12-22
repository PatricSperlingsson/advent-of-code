#https://adventofcode.com/2024/day/22
import numpy as np
from collections import deque, Counter, defaultdict
# Priority Queue
from heapq import heappop, heappush
import copy
import sympy
# Recursive function with memorization
from functools import lru_cache
#@lru_cache(None)
# Creating functions
from math import gcd
from sympy import symbols, Eq, solve
from itertools import product
from functools import cache

# Open and read the file as a single string
with open('../../inputs/2024/22i.txt', 'r') as file:
    init_secrets = [int(line.strip()) for line in file.readlines()]
print(f"init_secrets: {init_secrets}")

total = 0
for secret in init_secrets:
    print(f"secret: {secret}")
    for i in range (1, 2000+1, 1):
        secret ^= (secret * 64)
        secret %= 16777216
        secret ^= (secret // 32)
        secret %= 16777216
        secret ^= (secret * 2048)
        secret %= 16777216
    print(f"\t{i}\t{secret}")
    total += secret
print(total)
# Correct answer: 13185239446