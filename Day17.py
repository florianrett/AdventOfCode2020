def GetNeighbours(cell = ()):
    n = []

    if len(cell) == 3:

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0 , 1]:
                    if not (i == 0 and j == 0 and k == 0):
                        n.append((cell[0] + i, cell[1] + j, cell[2] + k))

    elif len(cell) == 4:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in [-1, 0 , 1]:
                    for l in [-1, 0, 1]:
                        if not (i == 0 and j == 0 and k == 0 and l == 0):
                            n.append((cell[0] + i, cell[1] + j, cell[2] + k, cell[3] + l))

    return n

def GetNewCells(oldActive = []):
    activeNeighbours = {}

    # print(oldActive)

    for c in oldActive:
        for n in GetNeighbours(c):
            if n in activeNeighbours:
                activeNeighbours[n] += 1
            else:
                activeNeighbours[n] = 1

    newCells = []
    for a in activeNeighbours:
        # print(a, a in oldActive, activeNeighbours[a])
        if a in oldActive:
            n = activeNeighbours[a]
            if n == 2 or n == 3:
                # print("add", a)
                newCells.append(a)
        else:
            if activeNeighbours[a] == 3:
                # print("add", a)
                newCells.append(a)

    return newCells

def Puzzle1(input=[]):
    activeCells = []              

    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c == "#":
                activeCells.append((j, i, 0))
            
    # print(activeCells)
    for i in range(6):
        activeCells = GetNewCells(activeCells)
        # for n in newCells:
        #     activeCells[n] = newCells[n]
    # print(len(activeCells))

    print("Puzzle 1: ", print(len(activeCells)))

def Puzzle2(input=[]):
    activeCells = []              

    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c == "#":
                activeCells.append((j, i, 0, 0))
            
    # print(activeCells)
    for i in range(6):
        activeCells = GetNewCells(activeCells)
        # for n in newCells:
        #     activeCells[n] = newCells[n]
    # print(len(activeCells))

    print("Puzzle 2: ", print(len(activeCells)))

f = open("PuzzleInputs\\Day17.txt", "r")
Puzzle1(f.read().splitlines())
f.close()
f = open("PuzzleInputs\\Day17.txt", "r")
Puzzle2(f.read().splitlines())
f.close

