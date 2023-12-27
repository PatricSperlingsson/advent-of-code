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

def check_bingo():
    for num_bingo in range(num_bingos):
        for y in range(5):
            colHit = 0
            for x in range(5):
                if check[num_bingo*5 + x][y] != 1:
                    break
                else:
                    colHit += 1
                if colHit == 5:
                    return 'c', num_bingo, y
        for x in range(5):
            rowHit = 0
            for y in range(5):
                if check[num_bingo*5 + x][y] != 1:
                    break
                else:
                    rowHit += 1
                if rowHit == 5:
                    return 'r', num_bingo, x
    return 'n', -1, -1

def get_sum_unmarked_nbrs(num_bingo):
    print("num_bingo: ", num_bingo)
    print("check: ", check[num_bingo*5])
    sum = 0
    for x in range(5):
        for y in range(5):
                if check[num_bingo*5 + x][y] != 1:
                    sum += c[num_bingo*5 + x][y]
    return sum

index = 0
bingo = ['n', -1, -1]
while bingo[0] == 'n':
    find_ran_nbr(ran_nbr[index])
    print("check #{}: {}".format(index, check))
    bingo = check_bingo()
    print("bingo: ", bingo)
    if bingo[0] != 'n':
        sum = get_sum_unmarked_nbrs(bingo[1])
        print("Sum of all unmarked numbers: ", sum)
        print("Winning Number: ", ran_nbr[index])
        print("Answer: ", ran_nbr[index] * sum)
    else:
        index += 1

file1.close()

#Correct Answer:
#bingo:  ('r', 60, 4)
#Sum of all unmarked numbers:  810
#Winning Number:  28
#Answer:  22680