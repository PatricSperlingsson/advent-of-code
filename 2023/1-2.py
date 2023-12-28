#https://adventofcode.com/2023/day/1
import math

#file1 = open('1-input-test.txt', 'r')
file1 = open('1-input.txt', 'r')
# Using readlines()
#Lines = file1.readlines()
# Using readlines() + strip of newlines
Lines = [line.strip() for line in file1]
file1.close()

# def setIndex(sindex):
#     if 
    
# Strips the newline character
sum = 0
for line in Lines:
    print("Line: ", line)
    first = ''
    firstIndex = -1
    last = ''
    lastIndex = math.inf

    for i,c in enumerate(line):
        if c.isdigit():
            if first == '':
                first = int(c)
                firstIndex = i
            else:
                last = int(c)
                lastIndex = i

    index = line.find('one')
    lindex = line.rfind('one')
    if index != -1:
        if first == '':
            first = 1
            firstIndex = index
        if last == '':
            last = 1
            lastIndex = index
        if index < firstIndex:
            first = 1
            firstIndex = index
        elif index > lastIndex:
            last = 1
            lastIndex = index
        if lindex > lastIndex:
            last = 1
            lastIndex = lindex
    index = line.find('two')
    lindex = line.rfind('two')
    if index != -1:
        if first == '':
            first = 2
            firstIndex = index
        if last == '':
            last = 2
            lastIndex = index
        if index < firstIndex:
            first = 2
            firstIndex = index
        elif index > lastIndex:
            last = 2
            lastIndex = index
        if lindex > lastIndex:
            last = 2
            lastIndex = lindex
    index = line.find('three')
    lindex = line.rfind('three')
    if index != -1:
        if first == '':
            first = 3
            firstIndex = index
        if last == '':
            last = 3
            lastIndex = index
        if index < firstIndex:
            first = 3
            firstIndex = index
        elif index > lastIndex:
            last = 3
            lastIndex = index
        if lindex > lastIndex:
            last = 3
            lastIndex = lindex
    index = line.find('four')
    lindex = line.rfind('four')
    if index != -1:
        if first == '':
            first = 4
            firstIndex = index
        if last == '':
            last = 4
            lastIndex = index
        if index < firstIndex:
            first = 4
            firstIndex = index
        elif index > lastIndex:
            last = 4
            lastIndex = index
        if lindex > lastIndex:
            last = 4
            lastIndex = lindex
    index = line.find('five')
    lindex = line.rfind('five')
    if index != -1:
        if first == '':
            first = 5
            firstIndex = index
        if last == '':
            last = 5
            lastIndex = index
        if index < firstIndex:
            first = 5
            firstIndex = index
        elif index > lastIndex:
            last = 5
            lastIndex = index
        if lindex > lastIndex:
            last = 5
            lastIndex = lindex
    index = line.find('six')
    lindex = line.rfind('six')
    if index != -1:
        if first == '':
            first = 6
            firstIndex = index
        if last == '':
            last = 6
            lastIndex = index
        if index < firstIndex:
            first = 6
            firstIndex = index
        elif index > lastIndex:
            last = 6
            lastIndex = index
        if lindex > lastIndex:
            last = 6
            lastIndex = lindex
    index = line.find('seven')
    lindex = line.rfind('seven')
    if index != -1:
        if first == '':
            first = 7
            firstIndex = index
        if last == '':
            last = 7
            lastIndex = index
        if index < firstIndex:
            first = 7
            firstIndex = index
        elif index > lastIndex:
            last = 7
            lastIndex = index
        if lindex > lastIndex:
            last = 7
            lastIndex = lindex
    index = line.find('eight')
    lindex = line.rfind('eight')
    if index != -1:
        if first == '':
            first = 8
            firstIndex = index
        if last == '':
            last = 8
            lastIndex = index
        if index < firstIndex:
            first = 8
            firstIndex = index
        elif index > lastIndex:
            last = 8
            lastIndex = index
        if lindex > lastIndex:
            last = 8
            lastIndex = lindex
    index = line.find('nine')
    lindex = line.rfind('nine')
    if index != -1:
        if first == '':
            first = 9
            firstIndex = index
        if last == '':
            last = 9
            lastIndex = index
        if index < firstIndex:
            first = 9
            firstIndex = index
        elif index > lastIndex:
            last = 9
            lastIndex = index
        if lindex > lastIndex:
            last = 9
            lastIndex = lindex
    for c in range(1,10):
        index = line.find(str(c))
        if index != -1:
            if first == '':
                first = c
                firstIndex = index
            if last == '':
                last = c
                lastIndex = index
            elif index < firstIndex:
                first = c
                firstIndex = index
            elif index > lastIndex:
                last = c
                lastIndex = index

    print("first: ", first)
    #print("firstIndex: ", firstIndex)
    print("last: ", last)
    #print("lastIndex: ", lastIndex)
    sum += int(str(first) + str(last))
    print("sum: ", sum)

# # Correct answer from test: 281
# # Correct answer: 53221