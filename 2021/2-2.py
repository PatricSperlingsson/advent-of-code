# Using readlines()
file1 = open('2-input.txt', 'r')
Lines = file1.readlines()

horizontal = 0
depth = 0
aim = 0
for line in Lines:
    line = line.strip()
    command = line.split(" ")
    print("command: ", command)
    if command[0] == "forward":
        horizontal += int(command[1])
        depth += aim*int(command[1])
    elif command[0] == "up":
        aim -= int(command[1])
    else:
        aim += int(command[1])
        
print("horizontal: ", horizontal)
print("depth: ", depth)
print("Total: ", horizontal*depth)
file1.close()
# Correct answer: 1813664422