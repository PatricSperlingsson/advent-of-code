# from collections import deque
# from itertools import product

#https://adventofcode.com/2024/day/20
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
with open('../../inputs/2024/21i.txt', 'r') as file:
    codes = [line.strip() for line in file.readlines()]
print(f"codes: {codes}")

# Define keypads
numeric_keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]

directional_keypad = [
    [' ', '^', 'A'],
    ['<', 'v', '>']
]

# Convert direction deltas to moves
def direction_to_move(dr, dc):
    if dr == -1:
        return "^"
    if dr == 1:
        return "v"
    if dc == -1:
        return "<"
    if dc == 1:
        return ">"

# Find the position of a key in a keypad
def find_position(keypad, key):
    for r, row in enumerate(keypad):
        for c, char in enumerate(row):
            if char == key:
                return r, c

# BFS to find the shortest path between two keys
def bfs(start_key, end_key, keypad):
    start = find_position(keypad, start_key)
    print(f"  start: {start}")
    end = find_position(keypad, end_key)
    print(f"  end: {end}")

    # up, down, left, right
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    queue = deque([(start, "")])
    # Visited used so that we don't go backwards
    visited = set([start])

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            print(f"  Path from {start_key} to {end_key}: {path}")
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(keypad) and 0 <= nc < len(keypad[0]) and keypad[nr][nc] != ' ':
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + direction_to_move(dr, dc)))
# test = bfs('A', '<', directional_keypad)

# Above is wrong since, we need to store all possibilities
# The shortest sequence depends on combinations
# Below finds all shortest combinations
def compute_seqs(keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] != ' ': pos[keypad[r][c]] = (r, c)
    seqs = {}
    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            possibilities = []
            q = deque([(pos[x], "")])
            optimal = float("inf")
            while q:
                (r, c), moves = q.popleft()
                for nr, nc, nm in [(r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">")]:
                    if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]): continue
                    if keypad[nr][nc] == ' ': continue
                    if keypad[nr][nc] == y:
                        if optimal < len(moves) + 1: break
                        optimal = len(moves) + 1
                        possibilities.append(moves + nm + "A")
                    else:
                        q.append(((nr, nc), moves + nm))
                else:
                    continue
                break
            seqs[(x, y)] = possibilities
    return seqs
numeric_keypad_seqs = compute_seqs(numeric_keypad)
print(f"numeric_keypad_seqs: {numeric_keypad_seqs}")
directional_keypad_seqs = compute_seqs(directional_keypad)
print(f"directional_keypad_seqs: {directional_keypad_seqs}")

def find_all_combinations(string, seqs):
    # Initialize options with the first sequence starting at "A"
    options = []
    # Iterate over indices to construct pairs without zip
    for i in range(len(string)):
        from_key = "A" if i == 0 else string[i - 1]
        to_key = string[i]
        # Append the possible sequences for each transition
        options.append(seqs[(from_key, to_key)])
    
    # Generate the cartesian product of all options
    result = []
    for product_option in product(*options):
        result.append("".join(product_option))
    
    return result

num_seqs = compute_seqs(numeric_keypad)
dir_seqs = compute_seqs(directional_keypad)



# Part 2
dir_lengths = {key: len(value[0]) for key, value in dir_seqs.items()}

@cache
def compute_length(seq, depth=25):
    if depth == 1:
        return sum(dir_lengths[(x, y)] for x, y in zip("A" + seq, seq))
    length = 0
    for x, y in zip("A" + seq, seq):
        length += min(compute_length(subseq, depth - 1) for subseq in dir_seqs[(x, y)])
    return length

total = 0
for code in codes:
    inputs = find_all_combinations(code, num_seqs)
    length = min(map(compute_length, inputs))
    total += length * int(code[:-1])

print(total)
# total = 0
# for code in codes:
#     print(f"code: {code}")
#     robot1 = find_all_combinations(code, num_seqs)
#     next = robot1
#     for _ in range(25):
#         possible_next = []
#         for seq in next:
#             possible_next += find_all_combinations(seq, dir_seqs)
#         minlen = min(map(len, possible_next))
#         next = [seq for seq in possible_next if len(seq) == minlen]
#     total += len(next[0]) * int(code[:-1])

# print(total)
# Correct answer: 188000493837892