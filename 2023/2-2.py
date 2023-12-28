#https://adventofcode.com/2023/day/1
#file1 = open('2-input-test.txt', 'r')
file1 = open('2-input.txt', 'r')
# Using readlines()
#Lines = file1.readlines()
# Using readlines() + strip of newlines
Lines = [line.strip() for line in file1]
file1.close()

# Strips the newline character
sum = 0
for i,game in enumerate(Lines):
    rs = game.split(':')[1]
    possible = 1
    max_r = 0
    max_g = 0
    max_b = 0
    multi = 0
    for reveals in rs.split(';'):
        print("reveals :", reveals)
        for cb in reveals.split(','):
            #print("cb: ", cb)
            num,col = cb.split()
            print("  num: {} col: {}".format(num, col))
            if col == 'red':
                if int(num) > 12:
                    possible = 0
                    #break;
                if int(num) > max_r:
                    max_r = int(num)
            elif col == 'green':
                if int(num) > 13:
                    possible = 0
                    #break;
                if int(num) > max_g:
                    max_g = int(num)
            elif col == 'blue':
                if int(num) > 14:
                    possible = 0
                    #break;
                if int(num) > max_b:
                    max_b = int(num)
        # if not possible:
        #     break;
    # if possible:
    #     print("Game: {} is possible".format(i+1))
    #     sum += i+1
    sum += max_r*max_g*max_b

print("sum: ", sum)
# Correct answer: 72422