f = open("PuzzleInputs\\Day11.txt", "r")
input = f.read().splitlines()
f.close()

adjs = []
for i, line in enumerate(input):
    linelist = []
    for j, c in enumerate(line):
        charlist = []
        if i > 0:
            if j > 0:
                charlist.append((i - 1, j - 1))
            charlist.append((i - 1, j))
            if j < len(line) - 1:
                charlist.append((i - 1, j + 1))
        if j > 0:
            charlist.append((i, j - 1))
        if j < len(line) - 1:
            charlist.append((i, j + 1))
        if i < len(input) - 1:
            if j > 0:
                charlist.append((i + 1, j - 1))
            charlist.append((i + 1, j))
            if j < len(line) - 1:
                charlist.append((i + 1, j + 1))
        linelist.append(list(charlist))
    adjs.append(list(linelist))

seats = list(input)
newseats = []

while True:    
    newseats = list(seats)
    for i, line in enumerate(seats):
        newline = ""
        for j, c in enumerate(line):
            if c == '.':
                newline += "."
                continue # skip floor
            numOcc = 0
            for adj in adjs[i][j]:
                value = seats[adj[0]][adj[1]]
                if value == '#':
                    numOcc += 1
            if numOcc == 0:
                newline += "#"
            elif numOcc >= 4:
                newline += "L"
            else:
                newline += c
        newseats[i] = newline

    # for l in newseats:
    #     print(l)

    if seats == newseats:
        break
    else:
        seats = list(newseats)

numOccupied = 0
for s in seats:
    numOccupied += s.count('#')

print("Puzzle1: Number of occupied seats: " + str(numOccupied))

def GetSeatValue(s = [], x =  0, y = 0):
    # print("GetSeatValue("+ str(x) + ", " + str(y) + ")")
    if y < 0 or y > len(s) - 1:
        return 'L'
    if x < 0 or x > len(s[y]) - 1:
        return 'L'
    
    return s[y][x]

def GetNumOccupiedSeats(s = [], x = 0, y = 0):
    num = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            counter = 1
            while True:
                seat = GetSeatValue(s, x + counter*i, y + counter * j)
                if seat == '#':
                    num += 1
                    break
                elif seat == 'L':
                    break
                else:
                    counter += 1
    return num


seats2 = list(input)
newseats2 = []
    
while True:    
    newseats2 = list(seats2)
    for i, line in enumerate(seats2):
        newline = ""
        for j, c in enumerate(line):
            if c == '.':
                newline += "."
                continue # skip floor
            numOcc = GetNumOccupiedSeats(seats2, j, i)
            
            if numOcc == 0:
                newline += "#"
            elif numOcc >= 5:
                newline += "L"
            else:
                newline += c
        newseats2[i] = newline

    # for l in newseats:
    #     print(l)

    if seats2 == newseats2:
        break
    else:
        seats2 = list(newseats2)

numOccupied = 0
for s in seats2:
    numOccupied += s.count('#')

print("Puzzle2: Number of occupied seats: " + str(numOccupied))