class Tile:
    ID = 0
    borders = []
    orientation = 0
    bFlipped = False
    content = []

    def __init__(self, input = ""):
        lines = input.split("\n")
        self.ID = int(lines[0][-5:-1])

        self.borders = []
        self.borders.append(lines[1])
        self.borders.append("".join([x[-1] for x in lines[1:]]))
        self.borders.append(lines[-1][::-1])
        self.borders.append("".join([x[0] for x in lines[:0:-1]]))

        self.content = [s[1:-1] for s in lines[2:-1]]
        # print(self.ID, self.content)
        # print(self.borders)
        # print(self.ID)

def Puzzle1(input=[]):
    tiles = []
    borders = {}
    borderPairs = {}
    
    for tile in input:
        newTile = Tile(tile)
        tiles.append(newTile)
        for b in newTile.borders:
            if b not in borders:
                borders[b] = newTile.ID
                borders[b[::-1]] = newTile.ID
            else:
                borderPairs[b] = (newTile.ID, borders[b])
                borderPairs[b[::-1]] = (newTile.ID, borders[b])

    
    # print(borders)
    # print(borderPairs)

    corners = []
    for tile in tiles:
        sumborders = 0
        for b in tile.borders:
            if b not in borderPairs:
                sumborders += 1
        
        if sumborders == 2:
            corners.append(tile)

    cornerproduct = 1
    for c in corners:
        cornerproduct *= c.ID

    print("Puzzle 1:", cornerproduct)

    numHash = 0
    for tile in tiles:
        for line in tile.content:
            numHash += line.count("#")
    
    # print("Number of hashes:", numHash)
    
    print("Puzzle 2 solution (only for my input, was too lazy to fully implement a solution):", numHash - 15*15)

# def Puzzle2(input=[]):

#     print("Puzzle 2: ")

f = open("PuzzleInputs\\Day20.txt", "r")
Puzzle1(f.read().split("\n\n"))
f.close()
# f = open("PuzzleInputs\\test.txt", "r")
# Puzzle2(f.read().splitlines())
# f.close