f = open("PuzzleInputs\\Day6.txt", "r")
input = f.read()
f.close()

groups = input.split("\n\n")

sum = 0
for g in groups:
    s = set(g)
    if s.__contains__('\n'):
        s.remove('\n')
    sum += s.__len__()

print("Puzzle 1 sum is " + str(sum))
groups = [item.split("\n") for item in groups]

sum2 = 0
for g in groups:
    s = set("abcdefghijklmnopqrstuvwxyz")
    for p in g:
        s = s.intersection(p)
    sum2 += s.__len__()

print("Puzzle 2 sum is " + str(sum2))
