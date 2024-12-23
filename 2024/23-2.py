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

# for k, v in conns.items():
#     print(f"{k} {v}")

# Recursive search
sets = set()
def search(node, req):
    # print(f"\tsearch node: {node}\treq: {req}")
    key = tuple(sorted(req))
    # print(f"\tkey: {key}")
    if key in sets: return
    sets.add(key)
    for neighbor in conns[node]:
        if neighbor in req: continue

        # Check if neighbor is connected to every node in the current set req
        all_connected = True
        for query in req:
            if neighbor not in conns[query]:
                all_connected = False
                break
        if not all_connected:
            continue

        search(neighbor, {*req, neighbor})

# Start recursive search for each node's neighbors
for node in conns:
    print(f"node: {node}")
    search(node, {node})

# Find longest set
longest_set_len = 0
longest_set = set()
for set in sets:
    # print(f"set: {set}")
    if len(set) > longest_set_len:
        longest_set_len = len(set)
        longest_set = set
print(f"longest_set: {','.join(longest_set)}")
# Correct answer: 1170