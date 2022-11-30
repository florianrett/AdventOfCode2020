from collections import Counter

def FlipTile(tiles = {}, path = ""):
    north = 0
    east = 0

    i = 0
    while i < len(path):
        dir = path[i]
        if dir == 'e':
            east += 1
        elif dir == 's':
            i += 1
            dir = path[i]
            if dir == 'e':
                north -= 1
                east += 1
            elif dir == 'w':
                north -= 1
        elif dir == 'w':
            east -= 1
        elif dir == 'n':
            i += 1
            dir = path[i]
            if dir == 'e':
                north += 1
            elif dir == 'w':
                north += 1
                east -= 1
        
        i += 1

    if (north, east) in tiles:
        tiles[(north, east)] = not tiles[(north, east)]
    else:
        tiles[(north, east)] = True

def GetNeighborTiles(n = 0, e = 0):
    return [(n, e+1), (n+1, e), (n+1, e-1), (n, e-1), (n-1, e), (n-1, e+1)]

def Puzzle1(input=[]):

    tiles  = {}
    
    for line in input:
        FlipTile(tiles, line)

    numBlack = 0
    for t in tiles:
        if tiles[t]:
            numBlack += 1

    print("Puzzle 1:", numBlack)

def Puzzle2(input=[]):
    
    tiles  = {}
    
    for line in input:
        FlipTile(tiles, line)

    for _ in range(100):
        # numNeighbours = {}
        # for t in tiles:
        #     if tiles[t] == True:
        #         if t not in numNeighbours:
        #             numNeighbours[t] = 0

        #         for n in GetNeighborTiles(t[0], t[1]):
        #             if n not in numNeighbours:
        #                 numNeighbours[n] = 1
        #             else:
        #                 numNeighbours[n] += 1

        # for x in numNeighbours:
        #     num = numNeighbours[x]
        #     if x not in tiles or not tiles[x]:
        #         if num == 2:
        #             tiles[x] = True
        #     else:
        #         if num == 0 or num > 2:
        #             tiles[x] = False


        # alternate solution from reddit, should really learn to use counters^^
        total_neighbours = Counter(n for coordinate in tiles for n in GetNeighborTiles(coordinate[0], coordinate[1]))
        tiles = {p for p, n in total_neighbours.items() if (p in tiles and n == 1) or n == 2}

        # print(tiles)
    
    # numBlack = 0
    # for t in tiles:
    #     if tiles[t]:
    #         numBlack += 1

    print("Puzzle 2:", len(tiles))

f = open("PuzzleInputs\\Day24.txt", "r")
Puzzle1(f.read().splitlines())
f.close()
f = open("PuzzleInputs\\Day24.txt", "r")
Puzzle2(f.read().splitlines())
f.close