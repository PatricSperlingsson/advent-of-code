#https://adventofcode.com/2023/day/6
# file = open('6-input-test.txt', 'r')
file = open('6-input.txt', 'r')
# Using readlines()
#Lines = file.readlines()
# Using readlines() + strip of newlines
Lines = [line.strip() for line in file]
file.close()

for l,line in enumerate(Lines):
    if l == 0:
        times = list(map(int, line.split(":")[1].split()))
        print("times: ", times)
    else:
        dist = list(map(int, line.split(":")[1].split()))
        print("dist: ", dist)

t = ''
for ti in times:
    t = t + str(ti)
t = int(t)#40828492
print("t: ", t)

d = ''
for di in dist:
    d = d + str(di)
d = int(d)#233101111101487
print("d: ", d)

sum = 1
beat_record = 0
for i in range(1, t+1):
    #print("i: ", i)
    if i*(t-i) > d:
        #print("i: ", i)
        beat_record += 1
print("beat_record: ", beat_record)
sum *= beat_record

print("sum: ", sum)
# 27102791