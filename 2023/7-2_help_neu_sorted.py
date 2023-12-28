import sys
import re
from collections import defaultdict, Counter
Lines = open('7-input.txt').read().strip().split('\n')
#print("Lines: ", Lines)

def strength(hand):
  # Replace strange characters to characters that can be sorted
  hand = hand.replace('T',chr(ord('9')+1))
  hand = hand.replace('J',chr(ord('2')-1))# Joker gets lowest value of all cards
  hand = hand.replace('Q',chr(ord('9')+3))
  hand = hand.replace('K',chr(ord('9')+4))
  hand = hand.replace('A',chr(ord('9')+5))
  print("hand: ", hand)

  # Count each characters and put answer into a dictionary
  C = Counter(hand)
  print("  C: ", C)
  print("  C.keys(): ", C.keys())
  
  # target is first key in the list (random)
  target = list(C.keys())[0]
  print("  target: ", target)

  # Set target to the key (not joker) that exist most
  for key in C:
    if key != '1': # if key not a joker
      if C[key] > C[target] or target=='1':
        target = key
  #assert target != '1' or list(C.keys()) == ['1']

  # Set the joker to the key that had the moost
  if '1' in C and target != '1':
    C[target] += C['1']
    del C['1']
  #assert '1' not in C or list(C.keys()) == ['1'], f'{C} {hand}'

  print("  C.values(): ", C.values())
  print("  sorted(C.values()): ", sorted(C.values()))
  if sorted(C.values()) == [5]:#Five
    return (10, hand)
  elif sorted(C.values()) == [1,4]:#Four
    return (9, hand)
  elif sorted(C.values()) == [2,3]:#Full
    return (8, hand)
  elif sorted(C.values()) == [1,1,3]:#Three
    return (7, hand)
  elif sorted(C.values()) == [1,2,2]:#Twop
    return (6, hand)
  elif sorted(C.values()) == [1,1,1,2]:#Onep
    return (5, hand)
  elif sorted(C.values()) == [1,1,1,1,1]:#High
    return (4, hand)
  else:
    assert False, f'{C} {hand} {sorted(C.values())}'

H = []
for line in Lines:
  # Add as tuples: ordered, immutable
  hand,bid = line.split()
  H.append((hand,bid))
print("H: ", H)

# Rank all cards
H = sorted(H, key=lambda hb:strength(hb[0]))
#print("H: ", H)

# Since the cards are already sorted by rank it is an easy task to summarize everything
ans = 0
for i,(hand,bid) in enumerate(H):
  #print(i,h,b)
  ans += (i+1)*int(bid)
print(ans)
# Correct answer: 253253225