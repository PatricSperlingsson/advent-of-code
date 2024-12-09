#https://adventofcode.com/2024/day/9
import numpy as np
from collections import deque
from collections import Counter
import copy
import sympy

# Open and read the file as a single string
with open('9i.txt', 'r') as file:
    disk_map_dense = file.read()
print(f"disk_map_dense: {disk_map_dense}")

id = 0
individual_blocks = []
for i, char in enumerate(disk_map_dense, start=1):
    length = int(char)
    # print(f"length: {length}")
    
    # file vs free space
    file = i % 2
    # print(f"file: {file}")
    if file:
        file_list = [id] * length
        individual_blocks.extend(file_list)
        id += 1
    else:
        file_list = ['.'] * length
        individual_blocks.extend(file_list)
print(f"individual_blocks: {individual_blocks}")

# Start fragmenting
# Move each block from right to free space to the left
for i in range(len(individual_blocks) - 1, -1, -1):
    if individual_blocks[i] != '.':
        for j in range(i):
            if individual_blocks[j] == '.':
                individual_blocks[j] = individual_blocks[i]
                individual_blocks[i] = '.'
                break
print(f"individual_blocks: {individual_blocks}")

# Calc filesystem checksum
filesystem_checksum = 0
for pos, block_id in enumerate(individual_blocks):
    if block_id != '.':
        filesystem_checksum += pos * block_id
print(f"filesystem_checksum: {filesystem_checksum}")
# Correct answer: 6283170117911