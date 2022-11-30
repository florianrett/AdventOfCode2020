f = open("PuzzleInputs\\Day3.txt", "r")
input = f.read().splitlines()
f.close()

# print(input)

def CheckSlope(Sx, Sy):
    x = 0
    y = 0
    trees = 0

    while True:
        if y >= input.__len__():
            break
        if input[y][x] == '#':
            trees += 1
        x = (x + Sx) % input[0].__len__()
        y += Sy
    return trees

t11 = CheckSlope(1, 1)
t31 = CheckSlope(3, 1)
t51 = CheckSlope(5, 1)
t71 = CheckSlope(7, 1)
t12 = CheckSlope(1, 2)

print("Number of trees: " + str(t11 * t31 * t51 * t71* t12))