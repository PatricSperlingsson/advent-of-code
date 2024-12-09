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
# Move only whole block from right to free space to the left
current_file_id = -1
len_current_file = 0
for i in range(len(individual_blocks) - 1, -1, -1):
    # print(f"Test: individual_blocks[{i}]: {individual_blocks[i]}")
    if individual_blocks[i] != '.':
        if current_file_id == -1:
            current_file_id = individual_blocks[i]
            len_current_file = 1
        elif individual_blocks[i] == current_file_id:
            len_current_file += 1

        # Are we done?
        # print(f"  Test Next: individual_blocks[{i-1}]: {individual_blocks[i-1]}")
        if individual_blocks[i-1] == current_file_id:
            continue

        # print(f"Done: len_current_file: {len_current_file}")

        # done with this file_id => find free space
        free_space_start = -1
        free_space_count = 0
        for j in range(i):
            if individual_blocks[j] == '.':
                if free_space_start == -1:
                    free_space_start = j
                free_space_count += 1
            else:
                if free_space_count >= len_current_file:
                    break
                free_space_start = -1
                free_space_count = 0

        # If a valid free space span is found, move the file
        if free_space_count >= len_current_file:
            # Clear the file from its original position
            for pos in range(i, i + len_current_file):
                individual_blocks[pos] = '.'
            # Place the file in the new position
            for k in range(len_current_file):
                individual_blocks[free_space_start + k] = current_file_id
        current_file_id = -1
#         print(f"    New: individual_blocks: {individual_blocks}")
#         print(f"")
# print(f"individual_blocks: {individual_blocks}")
 
# Calc filesystem checksum
filesystem_checksum = 0
for pos, block_id in enumerate(individual_blocks):
    if block_id != '.':
        filesystem_checksum += pos * block_id
print(f"filesystem_checksum: {filesystem_checksum}")
# Correct answer: 6307653242596