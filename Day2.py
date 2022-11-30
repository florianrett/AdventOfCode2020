
f = open("PuzzleInputs\\input2.txt", "r")
input = f.read().splitlines()
f.close()

# print(input)
sumvalid = 0
sumvalid2 = 0

for line in input:
    min = int(line.split('-')[0])
    max = int(line.split('-')[1].split(' ')[0])
    char = line.split(':')[0][-1]
    pw = line.split(' ')[2]

    num = pw.count(char)
    if num >= min and num <= max:
        sumvalid += 1

    if (pw[min-1] == char) ^ (pw[max-1] == char):
        sumvalid2 += 1

print("Number of valid paswords: " + str(sumvalid) + " for puzzle 1 and " + str(sumvalid2) + " for puzzle 2")

