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

# Open and read the file as a single string
# Outputs a list from the delimitier '\n'
with open('../../inputs/2025/10i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines: {lines}")

fewest_button_presses = 0
for line in lines:
    lights = []
    start_lights_state = line.split('[')[1].split(']')[0]
    print(f"start_lights_state: {start_lights_state}")

    # Create an XOR toggle e.g: 0110 ^ 0101 = 0011
    light_state = 0
    for i, light in enumerate(start_lights_state):
        if light == '#':
            light_state |= (1 << i)
    print(f"light_state: {bin(light_state)}")

    buttons = []
    for b in re.findall(r'\(([\d,]+)\)', line):
        mask = 0
        for i in map(int, b.split(',')):
            mask |= (1 << i)
        buttons.append(mask)
    print(f"buttons: {buttons}")

    # Start with an empty state
    start_state = 0
    queue = deque([start_state])
    button_presses = {start_state: 0}
    presses = None
    while queue:
        state = queue.popleft()
        button_pressed = button_presses[state]
        for mask in buttons:
            nstate = state ^ mask
            if nstate not in button_presses:
                button_presses[nstate] = button_pressed + 1
                # We are done when new state equals the light_state
                if nstate == light_state:
                    presses = button_pressed + 1
                    break
                queue.append(nstate)
    fewest_button_presses += presses

    print(f"Minimum presses for this machine: {presses}")
print(f"fewest_button_presses: {fewest_button_presses}")
# Correct answers: 7 and 532
