# Using readlines()
file1 = open('2-input.txt', 'r')
Lines = file1.readlines()

forward = 0
elevation = 0
count = 0
for line in Lines:
    line = line.strip()
    command = line.split(" ")
    print("command: ", command)
    if command[0] == "forward":
        forward += int(command[1])
    elif command[0] == "up":
        elevation -= int(command[1])
    else:
        elevation += int(command[1])
        
print("forward: ", forward)
print("elevation: ", elevation)
print("Total: ", forward*elevation)
file1.close()
# Correct answer: 1962940