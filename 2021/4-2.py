# Using readlines()
file1 = open('4-input.txt', 'r')
#Lines = file1.readlines()
#print("Lines: ", Lines)
Lines = [line.strip() for line in file1]
len_Lines = len(Lines)
print("Lines: ", Lines)
print("len_Lines: ", len_Lines)

# Read the Random Bingo Numbers as a string
ran_nbr = Lines[0]
len_nbr = len(ran_nbr)
print("ran_nbr: ", ran_nbr)
print("len_nbr: ", len_nbr)

# Convert the Random Bingo Numbers into int array
ran_nbr = [int(item) for item in ran_nbr.split(',') if item.isdigit()]
len_nbr = len(ran_nbr)
print("ran_nbr: ", ran_nbr)
print("len_nbr: ", len_nbr)

# Calculate amount of Bingo sheeets
num_bingos = int((len_Lines-1)/6)
print("num_bingos: ", num_bingos)
c = [ [ 0 for y in range( 5 ) ] for x in range( num_bingos * 5 ) ]
print("c: ", c)
check = [ [ 0 for y in range( 5 ) ] for x in range( num_bingos * 5 ) ]
print("check: ", check)

# Store the Bingo sheeets as integers in the c array
for x in range(num_bingos * 5):
    line = Lines[2 + x + x//5]
    print("line{}: {}".format(x, line))
    c[x] = [int(item) for item in line.split(' ') if item.isdigit()]

for x in range(num_bingos * 5):
    for y in range(5):
        print("c[{}][{}]: {}".format(x, y, c[x][y]))

def find_ran_nbr(nbr):
    for x in range(num_bingos * 5):
        for y in range(5):
            if c[x][y] == nbr:
                check[x][y] = 1

bingo_indexes = [0] * num_bingos
def check_bingo():
    bingo_wins = 0
    last_bingo = -1
    for num_bingo in range(num_bingos):
        for y in range(5):
            colHit = 0
            for x in range(5):
                if check[num_bingo*5 + x][y] != 1:
                    break
                else:
                    colHit += 1
                if colHit == 5:
                    if bingo_indexes[num_bingo] != 1:
                        bingo_indexes[num_bingo] = 1
                        last_bingo = num_bingo
                        bingo_wins += 1
        for x in range(5):
            rowHit = 0
            for y in range(5):
                if check[num_bingo*5 + x][y] != 1:
                    break
                else:
                    rowHit += 1
                if rowHit == 5:
                    if bingo_indexes[num_bingo] != 1:
                        bingo_indexes[num_bingo] = 1
                        last_bingo = num_bingo
                        bingo_wins += 1
    return bingo_wins, bingo_indexes, last_bingo

def get_sum_unmarked_nbrs(num_bingo):
    print("num_bingo: ", num_bingo)
    print("check: ", check[num_bingo*5])
    sum = 0
    for x in range(5):
        for y in range(5):
                if check[num_bingo*5 + x][y] != 1:
                    sum += c[num_bingo*5 + x][y]
    return sum

bingo_wins = 0
index = 0
bingo = [-1, -1, -1]
while bingo_wins < num_bingos:
    find_ran_nbr(ran_nbr[index])
    #print("check #{}: {}".format(index, check))
    bingo = check_bingo()
    print("bingo: ", bingo)
    if bingo[0] > 0:
        bingo_wins += bingo[0]
        print("bingo_wins right now: {} max is {}".format(bingo_wins, num_bingos))
    index += 1

print("Last bingo to win is: ", bingo[2])
sum = get_sum_unmarked_nbrs(bingo[2])
print("Sum of last bingo is: ", sum)
last_nbr = ran_nbr[index-1]
print("Winning Number: ", last_nbr)
print("Answer: Final score is: ", sum*last_nbr)

file1.close()

#Correct Answer:
#bingo:  (0, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], -1)
#bingo:  (1, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 65)
#bingo_wins right now: 100 max is 100
#Last bingo to win is:  65
#num_bingo:  65
#check:  [1, 1, 1, 0, 1]
#Sum of last bingo is:  172
#Winning Number:  94
#Answer: Final score is:  16168