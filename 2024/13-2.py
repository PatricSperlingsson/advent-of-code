#https://adventofcode.com/2024/day/13
import numpy as np
from collections import deque, defaultdict
from collections import Counter
import copy
import sympy
# Recursive function with memorization
from functools import lru_cache
#@lru_cache(None)
from math import gcd
from sympy import symbols, Eq, solve

# Open and read the file as a single string
with open('13i.txt', 'r') as file:
    lines = file.readlines()
print(f"lines: {lines}")



def find_min_tokens(a_x, a_y, b_x, b_y, p_x, p_y):
    # Step 1: Check if the prize is reachable
    # The prize is reachable if px is divisible by gcd(bAx, bBx) and
    # py is divisible by gcd(bAy, bBy).
    gcd_x = gcd(bAx, bBx)
    gcd_y = gcd(bAy, bBy)

    if px % gcd_x != 0 or py % gcd_y != 0:
        # Prize unreachable
        return None

    # Step 2: Set up equations to solve for button presses
    # Let `nA` = number of Button A presses, `nB` = number of Button B presses
    # The equations are:
    #   bAx * nA + bBx * nB = px
    #   bAy * nA + bBy * nB = py
    nA, nB = symbols('nA nB', integer=True, nonnegative=True)

    # Define the equations for X and Y
    eq_x = Eq(bAx * nA + bBx * nB, px)
    eq_y = Eq(bAy * nA + bBy * nB, py)

    # Step 3: Solve the equations for non-negative integer solutions
    solutions = solve((eq_x, eq_y), (nA, nB), dict=True)

    # Step 4: Find the solution with the minimum token cost
    # Cost formula: 3 tokens per Button A press + 1 token per Button B press
    # Start with a very high cost (inf)
    min_cost = float('inf')

    for sol in solutions:
        # Extract the values for nA and nB
        nA_val = sol[nA]
        nB_val = sol[nB]

        # Ensure the solution uses only non-negative integers
        if nA_val >= 0 and nB_val >= 0:
            # Calculate the total cost for this solution
            cost = 3 * nA_val + 1 * nB_val
            # Update the minimum cost if this solution is cheaper
            min_cost = min(min_cost, cost)

    # Step 5: Return the minimum cost, or None if no valid solution exists
    return min_cost if min_cost != float('inf') else None



total_tokens = 0
prizes = 0

for i,line in enumerate(lines, start=1):
    # Read input
    if i % 4 == 1:
        bAx = int(line.split(', ')[0].split('X+')[1])
        bAy = int(line.split(', ')[1].split('Y+')[1])
        print(f"bA: X+{bAx}, Y+{bAy}")
        continue
    elif i % 4 == 2:
        bBx = int(line.split(', ')[0].split('X+')[1])
        bBy = int(line.split(', ')[1].split('Y+')[1])
        print(f"bB: X+{bBx}, Y+{bBy}")
        continue
    elif i % 4 == 3:
        px = int(line.split(', ')[0].split('X=')[1])
        py = int(line.split(', ')[1].split('Y=')[1])
        px += 10000000000000
        py += 10000000000000
        print(f"px: X={px}, Y={py}")

    if line == '\n':
        # Empty line
        continue

    # Process input
    cost = find_min_tokens(bAx, bAy, bBx, bBy, px, py)
    if cost is not None:
        total_tokens += cost
        prizes += 1

print(f"Total Prizes Won: {prizes}")
print(f"Total Tokens Spent: {total_tokens}")
# Correct Answer: 101726882250942