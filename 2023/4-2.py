#https://adventofcode.com/2023/day/4
#file = open('4-input-test.txt', 'r')
file = open('4-input.txt', 'r')
# Using readlines()
#Lines = file.readlines()
# Using readlines() + strip of newlines
Lines = [line.strip() for line in file]
file.close()

card_inst = {}
for i,card in enumerate(Lines):
    nbr_str = card.split(':')[1]
    print("nbr_str: ", nbr_str)

    if i not in card_inst:
        card_inst[i] = 1

    win_nbrs = set()
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
            points += 1

    for p in range(i+1, i+1+points):
        card_inst[p] = card_inst.get(p, 1) + card_inst[i]

print(sum(card_inst.values()))
# 6874754