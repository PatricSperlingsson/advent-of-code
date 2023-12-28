#https://adventofcode.com/2023/day/7
import copy
# file = open('7-input-test.txt', 'r')
file = open('7-input.txt', 'r')
# Using readlines()
#Lines = file.readlines()
# Using readlines() + strip of newlines
Lines = [line.strip() for line in file]
file.close()

def find_dup():
    d = 1
    l = len(lcards)
    
    lcards_loop = copy.deepcopy(lcards)
    first = ''
    for l,c in enumerate(lcards_loop):
        if l == 0:
            first = c
            continue
        if first == c:
            d += 1
            lcards.remove(c)
    lcards.remove(first)
    return d
            
        

five = 0
four = 1
full = 2
three = 3
twop = 4
onep = 5
high = 6
types = [[] for _ in range(7)]
for hi,line in enumerate(Lines):
    cards = line.split()[0]
    bid = line.split()[1]
    print("cards: {}, bid: {}".format(cards, bid))
    # Find type

    c0, c1, c2, c3, c4 = cards
    lcards = [c0, c1, c2, c3, c4]
    print("lcards: ", lcards)
    #Possible types
    done = 0
    while len(lcards) > 1:
        d = find_dup()
        if d == 5:
            types[five].append([cards, bid])
            done = 1
            break
        elif d == 4:
            types[four].append([cards, bid])
            done = 1
            break
        elif d == 3:
            if len(lcards) <= 1:
                types[three].append([cards, bid])
                done = 1
                break
            d = find_dup()
            if d == 2:
                types[full].append([cards, bid])
                done = 1
                break
            else:
                types[three].append([cards, bid])
                done = 1
                break
        elif d == 2:
            if len(lcards) <= 1:
                types[onep].append([cards, bid])
                done = 1
                break
            d = find_dup()
            if d == 3:
                types[full].append([cards, bid])
                done = 1
                break
            elif d == 2:
                types[twop].append([cards, bid])
                done = 1
                break
            elif len(lcards) > 1:
                d = find_dup()
                if d == 2:
                    types[twop].append([cards, bid])
                    done = 1
                    break
                else:
                    types[onep].append([cards, bid])
                    done = 1
                    break
            else:
                types[onep].append([cards, bid])
                done = 1
                break
                
    if not done:
        types[high].append([cards, bid])
    print("types: ", types)

def find_highest(num_winnings):
    dup_card = ['' for _ in range(5)]
    for i in range(5):
        highest_h = -1
        highest_v = -1
        dup = 0
        for h,hand in enumerate(type_copy):
            if hand[0] == '879A6':
                print("Debug")
            stop = 0
            for ii in range(i):
                # if dup_card[ii] == '':
                #     break
                if hand[0][ii] != dup_card[ii]:
                    stop = 1
                    break
            if stop:
                continue
            card = hand[0][i]
            if card == 'A':
                if 14 > highest_v:
                    highest_h = h
                    highest_v = 14
                    dup = 0
                    dup_card[i] = ''
                elif 14 == highest_v:
                    dup += 1
                    dup_card[i] = 'A'
            elif card == 'K':
                if 13 > highest_v:
                    highest_h = h
                    highest_v = 13
                    dup = 0
                    dup_card[i] = ''
                elif 13 == highest_v:
                    dup += 1
                    dup_card[i] = 'K'
            elif card == 'Q':
                if 12 > highest_v:
                    highest_h = h
                    highest_v = 12
                    dup = 0
                    dup_card[i] = ''
                elif 12 == highest_v:
                    dup += 1
                    dup_card[i] = 'Q'
            elif card == 'J':
                if 11 > highest_v:
                    highest_h = h
                    highest_v = 11
                    dup = 0
                    dup_card[i] = ''
                elif 11 == highest_v:
                    dup += 1
                    dup_card[i] = 'J'
            elif card == 'T':
                if 10 > highest_v:
                    highest_h = h
                    highest_v = 10
                    dup = 0
                    dup_card[i] = ''
                elif 10 == highest_v:
                    dup += 1
                    dup_card[i] = 'T'
            else:
                if int(card) > highest_v:
                    highest_h = h
                    highest_v = int(card)
                    dup = 0
                    dup_card[i] = ''
                elif int(card) == highest_v:
                    dup += 1
                    dup_card[i] = card
        if dup == 0:
            return highest_h
    if i == 4:
        should_not_be_here()

num_winnings = len(Lines)
print("num_winnings: ", num_winnings)
total_winnings = 0
for type in types:
    length = len(type)
    if length == 1:
        total_winnings += int(type[0][1]) * num_winnings
        num_winnings -= 1
    elif length > 1:
        type_copy = copy.deepcopy(type)
        while len(type_copy) > 1:
            hh = find_highest(num_winnings)
            total_winnings += int(type_copy[hh][1]) * num_winnings
            num_winnings -= 1
            type_copy.pop(hh)
            
        total_winnings += int(type_copy[0][1]) * num_winnings
        num_winnings -= 1

print("total_winnings: ", total_winnings)
#253638586