#https://adventofcode.com/2023/day/4
#file = open('4-input-test.txt', 'r')
file = open('4-input.txt', 'r')
# Using readlines()
#Lines = file.readlines()
# Using readlines() + strip of newlines
Lines = [line.strip() for line in file]
file.close()

sum = 0
for i,card in enumerate(Lines):
    nbr_str = card.split(':')[1]
    print("nbr_str: ", nbr_str)

    win_nbrs = set()#Unordered list with no duplicates

    win_str = nbr_str.split('|')[0].strip()
    for win_nbr in win_str.split():
        print("win_nbr: ", win_nbr)
        win_nbrs.add(win_nbr)

    points = 0
    your_str = nbr_str.split('|')[1].strip()
    for your_nbr in your_str.split():
        print("your_nbr: ", your_nbr)
        #your_nbrs.add(your_nbr)
        if your_nbr in win_nbrs:
            if points == 0:
                points = 1
            else:
                points *= 2
    sum += points


 

print("sum: ", sum)
# 21088