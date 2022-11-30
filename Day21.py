def Puzzle1(input=[]):

    allergenes = {}
    ingredients = []
    for line in input:
        ing = line.split(" (")[0].split(" ")
        alls = line.split("contains ")[1]
        alls = alls.strip(")")
        alls = alls.split(", ")
        
        for all in alls:
            if all not in allergenes:
                allergenes[all] = []
            allergenes[all].append(set(ing))

        ingredients.append(ing)
    # print(allergenes)

    for a in allergenes:
        # print(a)
        # print(allergenes[a])
        allergenes[a] = set.intersection(*allergenes[a])

    mappedA = {}
    bFinished = False
    while not bFinished:
        bFinished = True
        # print(allergenes, mappedA)

        for a in allergenes:
            if len(allergenes[a]) == 1:
                mappedIng = allergenes[a].pop()
                # print(mappedIng)
                mappedA[a] = mappedIng
                bFinished = False

                for b in allergenes:
                    if b != a:
                        if mappedIng in allergenes[b]:
                            allergenes[b].remove(mappedIng)

    sum = 0
    for r in ingredients:
        for i in r:
            if i not in mappedA.values():
                sum += 1
    # print(ingredients)

    print("Puzzle 1:", sum)

    cdil = ""
    for k in sorted(mappedA):
        cdil += mappedA[k] + ","
    cdil = cdil.strip(",")    

    print("Puzzle 2:", cdil)

# def Puzzle2(input=[]):

#     print("Puzzle 2: ")

f = open("PuzzleInputs\\Day21.txt", "r")
Puzzle1(f.read().splitlines())
f.close()
# f = open("PuzzleInputs\\test.txt", "r")
# Puzzle2(f.read().splitlines())
# f.close