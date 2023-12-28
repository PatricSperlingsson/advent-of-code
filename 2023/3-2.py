#https://adventofcode.com/2023/day/3
#file = open('3-input-test.txt', 'r')
file = open('3-input.txt', 'r')
# Using readlines()
#Lines = file.readlines()
# Using readlines() + strip of newlines
Lines = [line.strip() for line in file]
file.close()

sum = 0
for r,row in enumerate(Lines):
    print("r:{} row:{}".format(r, row))
    for c,char in enumerate(row):
        if char != "*":
            continue



        partNumIndexStart = set()
        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if cr < 0 or cr >= len(Lines) or cc < 0 or cc >= len(Lines[cr]) or not Lines[cr][cc].isdigit():
                    continue
                while cc > 0 and Lines[cr][cc - 1].isdigit():
                    cc -= 1
                partNumIndexStart.add((cr, cc))
                
        if len(partNumIndexStart) != 2:
            continue

        print("partNumIndexStart: ", partNumIndexStart)

        ns = []
        for cr,cc in partNumIndexStart:
            s = ''
            while cc < len(Lines[cr]) and Lines[cr][cc].isdigit():
                s += Lines[cr][cc]
                cc += 1
            ns.append(int(s))
        
        sum += ns[0] * ns[1]



print("sum: ", sum)
# 72246648