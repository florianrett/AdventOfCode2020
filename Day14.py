def BitMaskInt(i=0, m=""):
    mAND = int(m.replace("X", "1"), 2)
    mOR = int(m.replace("X", "0"), 2)
    # print(i)
    i &= mAND
    # print(i)
    i |= mOR
    # print(i)
    return i


def Puzzle1(input=[]):
    mask = ""
    mem = {}
    for line in input:
        line = line.replace(" ", "")
        split = line.split('=')
        if split[0] == "mask":
            mask = split[1]
        else:
            memcell = int(split[0].split('[')[1][:-1])
            mem[memcell] = BitMaskInt(int(split[1]), mask)

    sum = 0
    for m in mem:
        # print(mem[m])
        sum += mem[m]
    print("Puzzle1 sum in memory: ", sum)

def GetFloatingMasks(m = ""):
    i = m.find('X')
    if i == -1:
        return [int(m, 2)]
    else:
        return GetFloatingMasks(m[:i] + '0' + m[i+1:]) + GetFloatingMasks(m[:i] + '1' + m[i+1:])
        

    return []

def Puzzle2(input=[]):
    mask = ""
    mem = {}
    for line in input:
        line = line.replace(" ", "")
        split = line.split('=')
        if split[0] == "mask":
            mask = split[1]
        else:
            memcell = int(split[0].split('[')[1][:-1])
            value = int(split[1])
            memcell = format(memcell, '036b')
            maskedcell = ""
            for i in range(36):
                if mask[i] == '0':
                    maskedcell += memcell[i]
                elif mask[i] == '1':
                    maskedcell += '1'
                else:
                    maskedcell += 'X'
            # print(maskedcell)
            for m in GetFloatingMasks(maskedcell):
                mem[m] = value

    sum = 0
    for m in mem:
        sum += mem[m]
    print("Puzzle2 sum in memory: ", sum)


f = open("PuzzleInputs\\Day14.txt", "r")
Puzzle1(f.read().splitlines())
f.close()
f = open("PuzzleInputs\\Day14.txt", "r")
Puzzle2(f.read().splitlines())
f.close