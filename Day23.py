def GetDestination(cups={}, current=0, removedCups = []):
    while True:
        # print("current", current)
        current = (current - 1) % (len(cups) + 4)
        # print(current)
        if current in cups and current not in removedCups:
            return current

def PlayRound(cups={}, current = 0):

    cup1 = cups[current]
    cup2 = cups[cup1]
    cup3 = cups[cup2]
    cups[current] = cups[cup3]

    # print("Cups removed:", cups, cup1, cup2, cup3)

    destination = GetDestination(cups, current, [cup1, cup2, cup3])
    # print("Destination:", destination)
    cups[cup3] = cups[destination]
    cups[destination] = cup1

    # print("Round finished.", cups)

    return cups[current]

def Puzzle1(input=""):
    cups = {}

    for i in range(len(input)):
        value = int(input[i])
        cups[value] = int(input[(i+1) % len(input)])

    # print(cups)
    currentCup = int(input[0])
    for i in range(100):
        currentCup = PlayRound(cups, currentCup)

    i = 1
    labels = ""
    for j in range(1, len(cups)):
        i = cups[i]
        labels += str(i)


    print("Puzzle 1:", labels)

def Puzzle2(input=""):
    cups = {}

    last = 1000000
    highest = 0
    for i in range(last):
        if i < len(input):
            value = int(input[i])
            highest = max(highest, value)
        else:
            value = i + highest - len(input) + 1

        cups[last] = value
        last = value
    # print(cups)

    print(cups[1000000])
    currentCup = int(input[0])
    for i in range(10000000):
        currentCup = PlayRound(cups, currentCup)

    label1 = cups[1]
    label2 = cups[label1]
    print(label1, label2)
    print("Puzzle 2:", label1*label2)

f = open("PuzzleInputs\\Day23.txt", "r")
Puzzle1(f.read())
f.close()
f = open("PuzzleInputs\\Day23.txt", "r")
Puzzle2(f.read())
f.close