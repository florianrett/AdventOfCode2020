def ParseInput(input=[]):
    hands = ()
    hand1 = input[0].split('\n')
    hand2 = input[1].split('\n')
    hand1.pop(0)
    hand2.pop(0)
    hands = ([int(x) for x in hand1], [int(y) for y in hand2])
    return hands

def PlayRound(p1 = [], p2 = []):
    card1 = p1.pop(0)
    card2 = p2.pop(0)

    if card1 > card2:
        p1.append(card1)
        p1.append(card2)
    elif card2 > card1:
        p2.append(card2)
        p2.append(card1)
    else:
        print("Both drawn cards have equal values?!")

def PlayRecursiveCombat(p1 = [], p2=[]):
    knownConfigs = []

    while len(p1) > 0 and len(p2) > 0:

        # print("Playing round...", p1, p2)

        if (p1, p2) in knownConfigs:
            return True
        else:
            knownConfigs.append((list(p1), list(p2)))

        card1 = p1.pop(0)
        card2 = p2.pop(0)
        bP1Win = False

        if len(p1) >= card1 and len(p2) >= card2:
            sub1 = list(p1[:card1])
            sub2 = list(p2[:card2])
            bP1Win = PlayRecursiveCombat(sub1, sub2)
        else:
            bP1Win = card1 > card2

        if bP1Win:
            p1.append(card1)
            p1.append(card2)
        else:
            p2.append(card2)
            p2.append(card1)


    return len(p1) > 0


def Puzzle1(input=[]):

    hands = ParseInput(input)
    p1 = hands[0]
    p2 = hands[1]
    

    while(len(p1) > 0 and len(p2) > 0):
        PlayRound(p1, p2)
        # print(p1, p2)
    
    winner = p2 if len(p1) == 0 else p1

    score = 0
    for i, c in enumerate(reversed(winner), 1):
        score += i * c

    print("Puzzle 1:", score)

def Puzzle2(input=[]):
    hands = ParseInput(input)
    p1 = hands[0]
    p2 = hands[1]

    winner = p1 if PlayRecursiveCombat(p1, p2) == True else p2
    score = 0
    for i, c in enumerate(reversed(winner), 1):
        score += i * c

    print("Puzzle 2:", score)

f = open("PuzzleInputs\\Day22.txt", "r")
Puzzle1(f.read().split('\n\n'))
f.close()
f = open("PuzzleInputs\\Day22.txt", "r")
Puzzle2(f.read().split('\n\n'))
f.close