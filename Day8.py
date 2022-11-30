f = open("PuzzleInputs\\Day8.txt", "r")
input = f.read().splitlines()
f.close()


program = []
for line in input:
    split = line.split(' ')
    program.append((split[0], int(split[1])))

def RunProgram(prog = [], start = 0):
    current = start
    acc = 0
    visited = []
    returncode = -1

    while True:
        ins = program[current][0]
        arg = program[current][1]

        if current in visited:
            returncode = 1
            break
        
        visited.append(current)
        if ins == "nop":
            current += 1
        if ins == "acc":
            acc += arg
            current += 1
        if ins == "jmp":
            current += arg

        if current == len(program):
            returncode = 0
            break

    return returncode, acc, visited

result1 = RunProgram(program, 0)
print("Puzzle1: Accumulator before loop: " + str(result1[1]))


unknown = set(range(len(program)))
mainloop = result1[2]
terminating = []
loop = []

while len(unknown) > 0:
    result = RunProgram(program, unknown.pop())
    unknown.difference_update(set(result[2]))
    # print(len(unknown))
    if result[0] == 1:
        # loop
        loop.extend(result[2])
    if result[0] == 0:
        terminating.extend(result[2])

# print(len(terminating))
# print(terminating)
fix = -1
for i in mainloop:
    ins = program[i][0]
    arg = program[i][1]
    if ins == "nop":
        if i+arg in terminating:
            fix = i
            break
    if ins == "jmp":
        if i+1 in terminating:
            fix = i
            break

if fix == -1:
    print("No fix found!")
else:
    ins = program[fix][0]
    arg = program[fix][1]
    if ins == "nop":
        print("nop instruction at point " + str(fix) + " is faulty")
        program[fix] = ("jmp", arg)
    if ins == "jmp":
        print("jmp instruction at point " + str(fix) + " is faulty")
        program[fix] = ("nop", arg)

result2 = RunProgram(program, 0)
print("Puzzle2: Accumulator before loop: " + str(result2[1]))


# nops = []
# jmps = []
# # for i in range(program.__len__()):
# for i, line in enumerate(program):
#     ins = program[i][0]
#     arg = program[i][1]

#     if ins == "nop":
#         nops.append(i + arg)
#         # print("line " + str(i) + " nop " + str(arg) + " dest = " + str(i+arg))
#     if ins == "jmp":
#         jmps.append(i + arg)
#         # print("line " + str(i) + " jmp " + str(arg) + " dest = " + str(i+arg))



# print(run.__contains__(619))
# for n in jmps:
#     print(n)