f = open("PuzzleInputs\\Day12.txt", "r")
input = f.read().splitlines()
f.close()

facing = 90  # 0 = north, 90 = east, ...
north = 0
east = 0

for line in input:
    com = line[0]
    value = int(line[1:])

    if com == 'N':
        north += value
    elif com == 'S':
        north -= value
    elif com == 'E':
        east += value
    elif com == 'W':
        east -= value
    elif com == 'L':
        facing -= value
        facing %= 360
    elif com == 'R':
        facing += value
        facing %= 360
    elif com == 'F':
        if facing == 0:
            north += value
        elif facing == 90:
            east += value
        elif facing == 180:
            north -= value
        elif facing == 270:
            east -= value
        else:
            print("Invalid facing value: " + str(facing))
    else:
        print("Invalid command: " + com)

print("Manhatten distance: " + str(abs(north) + abs(east)))


def RotateWaypoint(deg=0, n=0, e=0):
    deg %= 360
    if deg == 0:
        return (n, e)
    elif deg == 90:
        return (-1 * e, n)
    elif deg == 180:
        return (-1 * n, -1 * e)
    elif deg == 270:
        return (e, -1 * n)
    else:
        print("Invalid waypoint turn degrees: " + str(deg))


north = 0
east = 0
wn = 1
we = 10

for line in input:
    com = line[0]
    value = int(line[1:])

    if com == 'N':
        wn += value
    elif com == 'S':
        wn -= value
    elif com == 'E':
        we += value
    elif com == 'W':
        we -= value
    elif com == 'L':
        turn = RotateWaypoint(-1 * value, wn, we)
        wn = turn[0]
        we = turn[1]
    elif com == 'R':
        turn = RotateWaypoint(value, wn, we)
        wn = turn[0]
        we = turn[1]
    elif com == 'F':
        north += value * wn
        east += value * we
    else:
        print("Invalid command: " + com)

    # print(str(north) + ", " + str(east) + ", " + str(wn) + ", " + str(we))

print("Actual Manhatten distance: " + str(abs(north) + abs(east)))
