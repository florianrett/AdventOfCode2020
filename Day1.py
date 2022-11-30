
f = open("PuzzleInputs\\input1.txt", "r")
input = f.read().splitlines()
f.close()

input = list(map(int, input))
input.sort()

a = 0
z = input.__len__() - 1

while(True):
    sum = input[a] + input[z]
    if sum < 2020:
        a += 1
    elif sum > 2020:
        z -= 1
    else:
        print("" + str(input[a]) + ", " + str(input[z]) + ", " + str(input[a] * input[z]))
        break
    
for b in input:
    for c in input:
        for d in input:
            if b+c+d == 2020:
                print(str(b*c*d))
                break