#https://adventofcode.com/2024/day/23
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
with open('../../inputs/2024/23i.txt', 'r') as file:
    conns_data = [line.strip() for line in file.readlines()]
print(f"conns_data: {conns_data}")

# Create list of nodes with their neighbors
conns = defaultdict(set)
for conn_data in conns_data:
    conn_one = conn_data.split('-')[0]
    conn_two = conn_data.split('-')[1]
    # print(f"conn_one: {conn_one}")
    conns[conn_one].add(conn_two)
    conns[conn_two].add(conn_one)

for k, v in conns.items():
    print(f"{k} {v}")

# Find all nodes with neighbor that has one of the other neighbors as neighbor in its node
sets_of_threes = set()
for node, neighbors in conns.items():
    neighbors = list(neighbors)
    for i in range(len(neighbors)):
        current_neighbor = neighbors[i]
        print(f"current_neighbor {i}: {current_neighbor}")
        # Check each of the other neighbors if they exist in current_neighbor list => At least three connected
        for j in range(i + 1, len(neighbors)):
            if neighbors[j] in conns[neighbors[i]]:
                triangle = tuple(sorted((node, neighbors[i], neighbors[j])))
                sets_of_threes.add(triangle)
print(f"sets_of_threes: {sets_of_threes}")

sets_of_threes_starts_with_t = set()
for triangle in sets_of_threes:
    print(f"triangle: {triangle}")
    for comp in triangle:
        print(f"\t{comp}")
        if comp.startswith('t'):
            sets_of_threes_starts_with_t.add(triangle)
print(f"sets_of_threes_starts_with_t: {sets_of_threes_starts_with_t}")
print(f"result: {len(sets_of_threes_starts_with_t)}")
# Correct answer: 1170