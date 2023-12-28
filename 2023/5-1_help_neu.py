#https://adventofcode.com/2023/day/5
import re
#file = open('5-input-test.txt', 'r')
# file = open('5-input.txt', 'r')
# Lines = [line.strip() for line in file]
# file.close()

#Få hela filen
# seeds, *blocks = open('5-input-test.txt', 'r').read().split("\n\n")
seeds, *blocks = open('5-input.txt', 'r').read().split("\n\n")
print("seeds: ", seeds)

seeds = [int(s) for s in seeds.split(': ')[1].split()]
print("seeds: ", seeds)

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        range1 = [int(r) for r in line.split()]
        ranges.append(range1)

    new = []
    for seed in seeds:
        # print("seed: ", seed)
        for dest_start, source_start, range_length in ranges:
            if source_start <= seed < source_start + range_length:
                new.append(seed - source_start + dest_start)
                break
        else:
            new.append(seed)
    seeds = new

print(min(seeds))
# Correct answer: 662197086