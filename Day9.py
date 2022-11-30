f = open("PuzzleInputs\\Day9.txt", "r")
input = f.read().splitlines()
f.close()

def HasPair(num = 0, pre = []):
    for e in pre:
        other = list(pre)
        other.remove(e)
        if num-e in other:
            return True
    return False

input = list(map(int, input))

prelength = 25

lastnumbers = []
for i in range(prelength):
    lastnumbers.append(input[i])

faulty = 0
for i in range(prelength, len(input)):
    current = input[i]
    if not HasPair(current, lastnumbers):
        print("Faulty number: " + str(current))
        faulty = current

    lastnumbers.pop(0)
    lastnumbers.append(current)

for i, e in enumerate(input):
    sum = e
    numbers = set()
    numbers.add(e)
    while sum < faulty:
        i += 1
        sum += input[i]
        numbers.add(input[i])
    if sum == faulty:
        print(numbers)
        print("Encryption weakness is " + str(min(numbers) + max(numbers)))
        break