# Lines = open('1-input-test.txt').read().splitlines()
Lines = open('1-input.txt').read().splitlines()

prevSum = 0
Sum = 0
incSum = 0

for l,line in enumerate(Lines):
    if l+2 == len(Lines):
        break
    Sum = int(Lines[l]) + int(Lines[l+1]) + int(Lines[l+2])
    print("Sum: ", Sum)
    #print("lineCount", Lines[count], Lines[count+1], Lines[count+2])
    #print("Line{}: {}".format(count, line.strip()))
    if Sum > prevSum and l > 0:
        incSum += 1
        print("Sum: {} > prevSum: {} ".format(Sum, prevSum))
    prevSum = Sum

print("incSum: ", incSum)
# Correct answer: 1523