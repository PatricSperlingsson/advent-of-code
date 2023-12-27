# Using readlines()
file1 = open('3-input.txt', 'r')
#Lines = file1.readlines()
#print("Lines: ", Lines)
Lines = [line.strip() for line in file1]
print("Lines: ", Lines)

# colRange depends on input test or not
colRange = 12#5 for test

c = [ [ 0 for y in range( 2 ) ] for x in range( colRange ) ]
#c = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
print("c: ", c)

# empty list
#my_list = []
# list with mixed data types
#my_list = [1, "Hello", 3.4]# nested list
#my_list = ["mouse", [8, 4, 6], ['a']]
# change 2nd to 4th items
#odd[1:4] = [3, 5, 7]
# Appending and Extending lists at the end in Python
#odd.append(7)
#odd.extend([9, 11, 13])

#Remove all numbers that are different than oxygen_gen_num until one remains
oxygen_gen_rate = ""
oxygen_gen_nums = []
# copying a list
LinesDel = Lines.copy()
for k in range(colRange):
    index = 0
    Lines2 = LinesDel.copy()
    print("len(Lines2): ", len(Lines2))

    c = [ [ 0 for y in range( 2 ) ] for x in range( colRange ) ]
    for line in Lines2:
        line = line.strip()
        for x in range(colRange):
            if line[x] == "0":
                c[x][0] += 1
                #print("c[",x,"][0]: ", c[x][0])
            else:
                c[x][1] += 1
                #print("c[",x,"][1]: ", c[x][1])
    
    if c[k][1] >= c[k][0]:
        print("1 ({} vs {}) k={}".format(c[k][1], c[k][0], k))
        oxygen_gen_nums.append(1)
        print("oxygen_gen_nums[{}] keep: {}".format(k, oxygen_gen_nums[k]))
    else:
        print("0 ({} vs {}) k={}".format(c[k][0], c[k][1], k))
        oxygen_gen_nums.append(0)
        print("oxygen_gen_nums[{}] keep: {}".format(k, oxygen_gen_nums[k]))

    for line in Lines2:
        line = line.strip()
        if int(line[k]) != oxygen_gen_nums[k]:
            LinesDel.pop(index)
            index -= 1
        index += 1

    if (len(LinesDel) == 1):
        oxygen_gen_rate = LinesDel[index-1]
        break;
print("oxygen_gen_rate: ", oxygen_gen_rate)

#Remove all numbers that are different than co2_scrubber_num until one remains
co2_scrubber_rate = ""
co2_scrubber_nums = []
# copying a list
LinesDel = Lines.copy()
for k in range(colRange):
    index = 0
    Lines2 = LinesDel.copy()
    print("len(Lines2): ", len(Lines2))

    c = [ [ 0 for y in range( 2 ) ] for x in range( colRange ) ]
    for line in Lines2:
        line = line.strip()
        for x in range(colRange):
            if line[x] == "0":
                c[x][0] += 1
                #print("c[",x,"][0]: ", c[x][0])
            else:
                c[x][1] += 1
                #print("c[",x,"][1]: ", c[x][1])
    
    if c[k][1] >= c[k][0]:
        print("1 ({} vs {}) k={}".format(c[k][1], c[k][0], k))
        co2_scrubber_nums.append(0)
        print("co2_scrubber_nums[{}] keep: {}".format(k, co2_scrubber_nums[k]))
    else:
        print("0 ({} vs {}) k={}".format(c[k][0], c[k][1], k))
        co2_scrubber_nums.append(1)
        print("co2_scrubber_nums[{}] keep: {}".format(k, co2_scrubber_nums[k]))

    for line in Lines2:
        line = line.strip()
        if int(line[k]) != co2_scrubber_nums[k]:
            LinesDel.pop(index)
            index -= 1
        index += 1

    if (len(LinesDel) == 1):
        co2_scrubber_rate = LinesDel[index-1]
        break;
print("co2_scrubber_rate: ", co2_scrubber_rate)

# Convert from Binary to Decimal
# NOTE: MSB is at pos 0!!!

#oxygen_gen_rate_dec = 0
#for x in range(11,-1,-1):
#for x in range(0,12,1):
#for x in range(colRange):
#    if int(oxygen_gen_rate[x]) == 1:
#        oxygen_gen_rate_dec += 2**(colRange-1-x)
#print("Converted: {} to {}".format(oxygen_gen_rate, oxygen_gen_rate_dec))

#co2_scrubber_rate_dec = 0
#for x in range(11,-1,-1):
#for x in range(0,12,1):
#for x in range(colRange):
#    if int(co2_scrubber_rate[x]) == 1:
#        co2_scrubber_rate_dec += 2**(colRange-1-x)
#print("Converted: {} to {}".format(co2_scrubber_rate, co2_scrubber_rate_dec))

print("Converted: {} to {}".format(oxygen_gen_rate, int(oxygen_gen_rate, 2)))
print("Converted: {} to {}".format(co2_scrubber_rate, int(co2_scrubber_rate, 2)))
print("life support rating: ", int(oxygen_gen_rate, 2)*int(co2_scrubber_rate, 2))

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
# Correct answer:
# gamma:  784
# epsilon:  3311
# power:  2595824

# Correct answer:
#Converted: 001100001101
# to 781
#Converted: 101010101110
# to 2734
#life support rating:  2135254