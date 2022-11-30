f = open("PuzzleInputs\\Day10.txt", "r")
input = f.read().splitlines()
f.close()

input = list(map(int, input))
input.sort()

diff1 = 0
diff2 = 0
diff3 = 0
joltage = 0

for i in input:
    diff = i - joltage
    if diff == 1:
        diff1 += 1
    elif diff == 2:
        diff2 += 1
    elif diff == 3:
        diff3 += 1
    else:
        print("Unsupported joltage difference: " + str(diff) + " at joltage " + str(joltage))
    joltage = i

diff3 += 1 # built-in adapter

print("Puzzle1 result is " + str(diff1 * diff3))

def CountArrangements(subset = []):
    l = len(subset) - 2
    if l <= 0:
        return 1
    elif l <= 2:
        return pow(2, l)
    elif  l == 3:
        return pow(2, l) - 1
    else:
        print("Encountered a subset with more than 5 elements!")


input.insert(0, 0)    

subsets = []
currentset = []
last = 0

for e in input:
    if e - last == 3:
        subsets.append(list(currentset))
        currentset = []
    currentset.append(e)
    last = e
subsets.append(list(currentset))

print(subsets)
print(CountArrangements(subsets[0]))

print(max([len(x) for x in subsets]))

arr = 1
for s in subsets:
    arr *= CountArrangements(s)

print("Puzzle2 number of arrangements: " + str(arr))
    