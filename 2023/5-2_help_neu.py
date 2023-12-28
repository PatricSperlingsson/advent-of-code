#https://adventofcode.com/2023/day/5
import re
#file = open('5-input-test.txt', 'r')
# file = open('5-input.txt', 'r')
# Lines = [line.strip() for line in file]
# file.close()

#Få hela filen
# seed_ranges_in, *blocks = open('5-input-test.txt', 'r').read().split("\n\n")
seed_ranges_in, *blocks = open('5-input.txt', 'r').read().split("\n\n")

seed_ranges_in = [int(s) for s in seed_ranges_in.split(': ')[1].split()]
print("seed_ranges_in: ", seed_ranges_in)

seed_ranges = []
for i in range(0, len(seed_ranges_in), 2):
    seed_ranges.append((seed_ranges_in[i], seed_ranges_in[i] + seed_ranges_in[i + 1]))
print("seed_ranges: ", seed_ranges)

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        range1 = [int(r) for r in line.split()]
        ranges.append(range1)

    new = []
    while len(seed_ranges) > 0:
        # Start to end: e.g. test 79-93, 55-68
        start, end = seed_ranges.pop(0)

        # soil-to-fertilizer: 50, 98, 2
        # soil-to-fertilizer: 52, 50, 48
        for dest_start, source_start, range_length in ranges:
            nstart = max(start, source_start)#98, 79
            nend = min(end, source_start + range_length)#93, 93

            # 98 < 93
            if nstart < nend:
                #             79          50            52       93         50            52
                new.append((nstart - source_start + dest_start, nend - source_start + dest_start))
                if nstart > start:
                    seed_ranges.append((start, nstart))
                if end > nend:
                    seed_ranges.append((nend, end))
                break
        else:
            new.append((start, end))
    seed_ranges = new

print(min(seed_ranges)[0])
# Correct answer: 52510809