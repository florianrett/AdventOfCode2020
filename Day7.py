f = open("PuzzleInputs\\Day7.txt", "r")
input = f.read().splitlines()
f.close()

rules = {}

for line in input:
    line = line.replace(' ', '')
    line = line.replace('.', '')
    line = line.replace("bags", '')
    line = line.replace("bag", '')
    outer = line.split("contain", 1)
    content = outer[1].split(',')
    
    rule = {}
    for c in content:
        if c == "noother":
            continue

        num = int(c[0])
        rule[c[1:]] = num

    rules[outer[0]] = rule

parents = {}
for rule in rules:
    for child in rules[rule]:
        if parents.__contains__(child) == False:
            parents[child] = []
        parents[child].append(rule)
        
    #print(rules[rule].__contains__("shinygoldbags"))

if parents.__contains__("shinygold"):
    colors = []
    candidates = []
    candidates.extend(parents["shinygold"])
    while candidates.__len__() > 0:
        colors.append(candidates[0])
        # print("Candidates: " + str(candidates))
        if parents.__contains__(candidates[0]):
            candidates.extend(parents[candidates[0]])
        del candidates[0]

    print("Number of bags that could contain a shiny gold bag: " + str(set(colors).__len__()))

def GetNumBags(bag = ""):
    num = 0
    for child in rules[bag]:
        # print("Child " + child + " of bag " + bag)
        num += rules[bag][child] * (1 + GetNumBags(child))

    return num
# print(rules)
# print(GetNumBags("shinygold"))
print("Nubmer of bags within a shiny gold bag: " + str(GetNumBags("shinygold")))