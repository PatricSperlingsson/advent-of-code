#https://adventofcode.com/2024/day/19
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

# Open and read the file as a single string
with open('19i.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

# def find_pattern(design, atp_list):
#     queue = deque()
#     queue.append(0)
#     visited = set()
#     visited.add(0)

#     while queue:
#         p = queue.popleft()
        
#         if p == len(design):
#             return True

#         for atp in atp_list:
#             dp = len(atp)
#             np = p + dp
            
#             print(f"test design: {design[p:np]}")
#             if np < len(design) and design[p:np] == atp:
#                 if np not in visited:
#                     queue.append(np)
#                     visited.add(np)
#     return False            

def can_build_design(design, atp_list):

    # current_built_design = []
    # for p in range(len(design)):
    #     current_built_design.append(False)
    # print(f"current_built_design: {current_built_design}")
    
    # for atp in atp_list:
    #     for p in range(len(design)):
    #         if design[p:p+len(atp)] == atp:
    #             current_built_design[p:p+len(atp)] = True

    # print(f"current_built_design: {current_built_design}")
    # for p in range(len(design)-1):
    #     if not current_built_design[p]:
    #         return False
    # return True

    current_built_design = [False] * (len(design) + 1)  # Adding +1 to handle the last position
    current_built_design[0] = True  # Start position (empty design) is always considered built

    # current_built_design = []
    # for p in range(len(design)+1):
    #     current_built_design.append(False)
    print(f"current_built_design: {current_built_design}")

    # Iterate over each position in the design
    for p in range(len(design)):
        if current_built_design[p]:
            for atp in atp_list:
                # Check if the substring of the design matches the available towel pattern
                if design[p:p + len(atp)] == atp:
                    # If it matches, mark the new position as "built"
                    current_built_design[p + len(atp)] = True

    # Return True if the entire design can be built (i.e., the last position is marked as True)
    return current_built_design[len(design)]

atp_dict = {}
atp_list = lines[0].split(', ')
print(f"atp_list: {atp_list}")
for atp in atp_list:
    atp_dict[atp] = 10**9
print(f"atp_dict: {atp_dict}")

designs = len(lines)-2
print(f"designs: {designs}")
possible = 0
for ddi in range(2, designs + 2, 1):
    design = lines[ddi]
    print(f"design: {design}")

    found = can_build_design(design, atp_list)
    if found:
        possible += 1

print(f"Possible: {possible}")
# Correct Answer: 334