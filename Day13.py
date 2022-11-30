import math

f = open("PuzzleInputs\\Day13.txt", "r")
input = f.read().splitlines()
f.close()

buslines = []
for bus in input[1].split(','):
    if bus != 'x':
        buslines.append(int(bus))


def Puzzle1(ids=[], earliestDeparture=0):
    dep = earliestDeparture
    while True:
        for id in buslines:
            if dep % id == 0:
                print("Earliest bus ID " + str(id) + ". Solution is " +
                      str(id * (dep - earliestDeparture)))
                return
        dep += 1


Puzzle1(buslines, int(input[0]))


def GetLCM(a=0, b=0):
    return int(a * b / math.gcd(a, b))


def Puzzle2Fast(idlist=[]):
    timestamp = 0
    stepsize = 1

    for i, x in enumerate(idlist):
        if x != 'x':
            id = int(x)
            # print(i, id)

            while True:
                if (timestamp + i) % id == 0:
                    stepsize = GetLCM(stepsize, id)
                    break
                timestamp += stepsize

    return timestamp

solution2 = Puzzle2Fast(input[1].split(','))
print("Earliest matching timestamp is: " + str(solution2))
