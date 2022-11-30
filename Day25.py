def TransformNumber(subject = 0, loopSize = 0):
    value = 1
    for i in range(loopSize):
        value *= subject
        value %= 20201227

    return value

def FindLoopSize(publicKey = 0, secretNumber = 0):
    value = 1
    loopSize = 0
    while value != publicKey:
        loopSize += 1
        value *= secretNumber
        value %= 20201227

    return loopSize

def Puzzle1(input=[]):

    cardPublic = int(input[0])
    doorPublic = int(input[1])

    cardLoopSize = FindLoopSize(cardPublic, 7)
    doorLoopSize = FindLoopSize(doorPublic, 7)
    # print("Card loopsize:", FindLoopSize(cardPublic, 7))
    
    # key = TransformNumber(cardPublic, doorLoopSize)
    # print(key)
    # key = TransformNumber(doorPublic, cardLoopSize)
    # print(key)

    print("Puzzle 1:", TransformNumber(cardPublic, doorLoopSize))

def Puzzle2(input=[]):

    print("Puzzle 2: ")

f = open("PuzzleInputs\\Day25.txt", "r")
Puzzle1(f.read().splitlines())
f.close()
f = open("PuzzleInputs\\test.txt", "r")
Puzzle2(f.read().splitlines())
f.close