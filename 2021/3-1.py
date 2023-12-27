# Using readlines()
file1 = open('3-input.txt', 'r')
Lines = file1.readlines()
 
c = [ [ 0 for y in range( 2 ) ] for x in range( 12 ) ]
#c = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
print("c: ", c)
 
gamma = 0
epsilon = 0
 
for line in Lines:
    line = line.strip()
    for x in range(12):
        if line[x] == "0":
            c[x][0] += 1
            #print("c[",x,"][0]: ", c[x][0])
        else:
            c[x][1] += 1
            #print("c[",x,"][1]: ", c[x][1])
print("c: ", c)
#d = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
 
# NOTE: MSB is at pos 0!!!
 
#for x in range(11,-1,-1):
#for x in range(0,12,1):
for x in range(12):
    if c[x][1] > c[x][0]:
        print("1 ({} vs {}) x={}".format(c[x][1], c[x][0], x))
        gamma += 2**(11-x)
    else:
        print("0 ({} vs {}) x={}".format(c[x][0], c[x][1], x))
        epsilon += 2**(11-x)
 
print("gamma: ", gamma)
print("epsilon: ", epsilon)
print("power: ", gamma*epsilon)
#print("horizontal: ", horizontal)
#print("depth: ", depth)
#print("Total: ", horizontal*depth)
file1.close()
 
# Correct Answer
# MSB first in list below since we read left -> right:
#0 (506 vs 494)
#0 (510 vs 490)
#1 (506 vs 494)
#1 (508 vs 492)
#0 (501 vs 499)
#0 (502 vs 498)
#0 (506 vs 494)
#1 (511 vs 489)
#0 (505 vs 495)
#0 (524 vs 476)
#0 (515 vs 485)
#0 (510 vs 490)
#
# gamma:  784
# epsilon:  3311
# power:  2595824

