# Using readlines()
# file1 = open('1-input-test.txt', 'r')
file1 = open('1-input.txt', 'r')
# Reads each line
#Lines = file1.readlines()
# Reads each line AND strips (removes) the newline character
Lines = [line.strip() for line in file1]
file1.close()
print("Lines: ", Lines)


nbrOfIncreases = 0
previous = 0
count = 0
for line in Lines:
    count += 1
    #print("Line{}: {}".format(count, line))
    if int(line) > previous and previous != 0:
        nbrOfIncreases += 1
    previous = int(line)
print("nbrOfIncreases: ", nbrOfIncreases)
# Answer: 1477