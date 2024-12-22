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



total_prize_per_four_changes = {}
for secret in init_secrets:
    print(f"secret: {secret}")

    # Prizes
    prizes = []
    prizes.append(secret % 10)
    for i in range (1, 2000+1, 1):
        secret ^= (secret * 64)
        secret %= 16777216
        secret ^= (secret // 32)
        secret %= 16777216
        secret ^= (secret * 2048)
        secret %= 16777216
        prizes.append(secret % 10)
        print(f"\t{i}\t{secret}")
    print(prizes)

    # Prize Changes    
    changes = []
    for p in range(len(prizes) - 1):
        changes.append(prizes[p + 1] - prizes[p])
    print(changes)

    # Get prize for each 4 changes
    prize_per_four_changes = {}
    for i in range(len(changes) - 3):
        if (changes[i], changes[i + 1], changes[i + 2], changes[i + 3]) not in prize_per_four_changes:
            prize_per_four_changes[(changes[i], changes[i + 1], changes[i + 2], changes[i + 3])] = prizes[i + 4]
    print(f"prize_per_four_changes: {prize_per_four_changes}")

    for pattern, prize in prize_per_four_changes.items():
        if pattern in total_prize_per_four_changes:
            total_prize_per_four_changes[pattern] += prize
        else:
            total_prize_per_four_changes[pattern] = prize
print(f"total_prize_per_four_changes: {total_prize_per_four_changes}")

# Which pattern gives the highest prize through all secrets?
max_prize = 0
for value in total_prize_per_four_changes.values():
    if value > max_prize:
        max_prize = value
print(f"max_prize: {max_prize}")
# Correct answer: 1501
