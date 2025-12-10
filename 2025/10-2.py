#https://adventofcode.com/2025/day/10
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
# from math import gcd
import math
from sympy import symbols, Eq, solve
from itertools import product
from functools import cache
import re
import pulp

# Open and read the file as a single string
# Outputs a list from the delimitier '\n'
with open('../../inputs/2025/10i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

fewest_button_presses = 0
for line in lines:
    button_target_str = line.split('{')[1].split('}')[0].strip(',')
    button_target = tuple([int(button) for button in button_target_str.split(',')])
    print(f"button_target: {button_target}")

    button_wirings = []
    for b in re.findall(r'\(([\d,]+)\)', line):
        vec = [0] * len(button_target)
        for i in map(int, b.split(',')):
            vec[i] = 1
        button_wirings.append(vec)
    print(f"button_wirings: {button_wirings}")

#  Below is too slow
      # Start with an empty state
#     start_state = tuple([0] * len(button_target))
#     print(f"start_state: {start_state}")
#     queue = deque([start_state])
#     button_presses = {start_state: 0}
#     presses = None
#     while queue:
#         state = queue.popleft()
#         buttons_pressed = button_presses[state]
    
#         # Check if we reached target
#         if state == button_target:
#             presses = buttons_pressed
#             break
    
#         # Try pressing each button
#         for button_wiring in button_wirings:
#             # Build the next state without using zip
#             new_state_list = []
#             for i in range(len(state)):
#                 updated_value = state[i] + button_wiring[i]
#                 new_state_list.append(updated_value)
#             ns = tuple(new_state_list)
    
#             # Check that the new state does not exceed the target counters
#             state_is_valid = True
#             for i in range(len(button_target)):
#                 if ns[i] > button_target[i]:
#                     state_is_valid = False
#                     break
    
#             # If the state is valid and we haven't seen it before, record it
#             if state_is_valid and ns not in button_presses:
#                 button_presses[ns] = buttons_pressed + 1
#                 queue.append(ns)

#     print(f"Minimum presses for this machine: {presses}")
#     fewest_button_presses += presses
# print(f"fewest_button_presses: {fewest_button_presses}")


    # --- ILP solver ---
    n_buttons = len(button_wirings)
    x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(n_buttons)]

    prob = pulp.LpProblem("AoC2025_Day10_Part2", pulp.LpMinimize)
    prob += pulp.lpSum(x), "MinTotalPresses"

    # Constraints: each counter must equal its target
    for i in range(len(button_target)):
        prob += pulp.lpSum(button_wirings[j][i] * x[j] for j in range(n_buttons)) == button_target[i]

    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))
    if pulp.LpStatus[status] != "Optimal":
        print("No feasible solution for this machine.")
        continue

    presses = int(sum(pulp.value(xj) for xj in x))
    fewest_button_presses += presses

    # Optional: show which buttons were pressed
    plan = [(idx, int(pulp.value(xj))) for idx, xj in enumerate(x) if pulp.value(xj) > 0]
    print(f"Minimum presses for this machine: {presses}")
    print(f"Plan (button_index, count): {plan}")

print(f"fewest_button_presses: {fewest_button_presses}")
# Correct answers: 33 and 18387