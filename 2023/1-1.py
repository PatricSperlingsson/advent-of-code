#https://adventofcode.com/2023/day/1
#file1 = open('1-input-test.txt', 'r')
file1 = open('1-input.txt', 'r')
# Using readlines()
#Lines = file1.readlines()
# Using readlines() + strip of newlines
Lines = [line.strip() for line in file1]
file1.close()

# Strips the newline character
sum = 0
for line in Lines:
    print("Line: ", line)
    first = ''
    last = ''
    for x in range(len(line)):
        if line[x].isdigit():
            if first == '':
                first = int(line[x])
            else:
                last =  int(line[x])
    if last == '':
        last = first
    print("first: ", first)
    print("last: ", last)
    sum += int(str(first) + str(last))
    print("sum: ", sum)

# # Correct answer from test: 142
# # Correct answer: 55834