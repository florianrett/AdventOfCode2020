def Puzzle1(input=[]):

    spokenNumbers = []
    lastTurns = {}

    for i in map(int, input):
        spokenNumbers.append(i)
        lastTurns[i] = len(spokenNumbers) - 1
    lastTurns.pop(int(input[-1])) # pop last item as it still has to be considered

    for i in range(len(input), 2020):
        lastNumber = spokenNumbers[i-1]
        nextNumber = 0
        # print("Turn: ", i)
        # print("LastNumber: ", lastNumber)
        if lastNumber in lastTurns:
            nextNumber = i - 1 - lastTurns[lastNumber]

        # print("Next number: ", nextNumber)
        spokenNumbers.append(nextNumber)
        lastTurns[lastNumber] = i - 1

    # print(spokenNumbers)
    print("Puzzle 1: 2020th spoken number is ", spokenNumbers[-1])
    return 0


def Puzzle2(input=[]):
    spokenNumbers = []
    lastTurns = {}

    for i in map(int, input):
        spokenNumbers.append(i)
        lastTurns[i] = len(spokenNumbers) - 1
    lastTurns.pop(int(input[-1])) # pop last item as it still has to be considered

    for i in range(len(input), 30000000):
        lastNumber = spokenNumbers[i-1]
        nextNumber = 0
        if lastNumber in lastTurns:
            nextNumber = i - 1 - lastTurns[lastNumber]

        spokenNumbers.append(nextNumber)
        lastTurns[lastNumber] = i - 1

    print("Puzzle 2: 30000000th spoken number is ", spokenNumbers[-1])
    return 0


f = open("PuzzleInputs\\Day15.txt", "r")
Puzzle1(f.read().split(','))
f.close()
f = open("PuzzleInputs\\Day15.txt", "r")
Puzzle2(f.read().split(','))
f.close