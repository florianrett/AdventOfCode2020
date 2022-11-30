f = open("PuzzleInputs\\Day5.txt", "r")
input = f.read().splitlines()
f.close()

def GetRow(r = "B"):
    r = r.replace('F', '0')
    r = r.replace('B', '1')
    return int(r, base=2)

def GetSeat(s = "R"):
    s = s.replace('L', '0')
    s = s.replace('R', '1')
    return int(s, base=2)

highest = 0
IDs = []
for line in input:
    row = GetRow(line[:7])
    seat = GetSeat(line[7:])
    ID = row*8 + seat
    highest = max(highest, ID)
    IDs.append(ID)

IDs.sort()
print("Highest ID: " + str(highest))

for i in range(1, IDs.__len__()-1):
    if IDs[i] != IDs[i-1] + 1:
        print("Missing ID: " + str(IDs[i] - 1))
    