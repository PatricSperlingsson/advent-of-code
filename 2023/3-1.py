#https://adventofcode.com/2023/day/3
import re
#file = open('3-input-test.txt', 'r')
file = open('3-input.txt', 'r')
# Using readlines()
#Lines = file.readlines()
# Using readlines() + strip of newlines
Lines = [line.strip() for line in file]
file.close()

sum = 0
for l,line in enumerate(Lines):
    print("l:{} line:{}".format(l, line))

    foundDigit = 0
    partNum = ''
    index = -1
    for c, char in enumerate(line):
        print("  c:{} char:{}".format(c, char))
        
        if char.isdigit():
            foundDigit = 1
            partNum += char
            if index == -1:
                index = c
            #Special case if digit is at the end
            if c+1 != len(line):
                continue
        elif foundDigit:
            foundDigit = 0
        else:
            continue
        
        #Search around Digit
        print("index: {}, partNum: {}".format(index, partNum))
        length = len(partNum)
        for col in range(index-1, index+length+1):#Above
            if l-1 >= 0 and col >= 0 and col < len(line):
                print("  Above: col: {}: {}".format(col, Lines[l-1][col]))
                if Lines[l-1][col] != '.':
                    sum += int(partNum)
                    print("    ADD1: ", partNum)
                    break
        for col in range(index-1, index+length+1):#Below
            if l+1 < len(Lines) and col >= 0 and col < len(line):
                print("  Below: col: {}: {}".format(col, Lines[l+1][col]))
                if Lines[l+1][col] != '.':
                    sum += int(partNum)
                    print("    ADD2: ", partNum)
                    break
        if index-1 >= 0:#Next to-1
            print("  Next to-1: index-1: {}: {}".format(index-1, Lines[l][index-1]))
            if Lines[l][index-1] != '.':
                sum += int(partNum)
                print("    ADD3: ", partNum)
        if index+length < len(line):#Next to+1
            print("  Next to+1: index+length: {}: {}".format(index+length, Lines[l][index+length]))
            if Lines[l][index+length] != '.':
                sum += int(partNum)
                print("    ADD4: ", partNum)
        
        foundDigit = 0
        partNum = ''
        index = -1

print("sum: ", sum)
# 498559