import re

def BuildRegex(rules = {}, start = "0", numRec = 0):
    if start not in rules:
        print("Invalid rule ", start)
        return ""

    # if numRec > 0:
    #     print(start)
    #     if start == "8":
    #         return BuildRegex(rules, "42") +  "+"
    #     if start == "11":
    #         return "(" + BuildRegex(rules, "42") + BuildRegex(rules, "31") + ")|(" + BuildRegex(rules, "42") + BuildRegex(rules, "11", numRec-1) + BuildRegex(rules, "31") + ")"
    #         # return BuildRegex(rules, "42") + "+" + BuildRegex(rules, "31") + "+"

    exp = ""
    for option in rules[start]:
        # print(option)
        for rule in option:
            # print(rule)
            if rule.isnumeric():
                if rule == start:
                    if numRec > 0:
                        exp += BuildRegex(rules, rule, numRec-1)
                else:
                    exp += BuildRegex(rules, rule, numRec)
            else:                
                exp += rule.replace("\"", "")
        exp += "|"
    exp = exp.strip("|")
    # print(rules[start])

    if len(exp) > 1:
        exp = "(" + exp + ")"

    return exp

def Puzzle1(input=[]):
    rules = {}

    # read in rules
    for line in input:        
        if ":" in line:
            s = line.split(": ")
            rules[s[0]] = [r.split(" ") for r in s[1].split(" | ")]
    # print(rules)
    
    # generate regex
    regex = BuildRegex(rules, "0")
    # print("Regex:", regex)
    
    # print(re.fullmatch(regex, "aaaabbb") != None)    
    # check strings    
    sum = 0
    for line in input:
        if ":" not in line:
            if re.fullmatch(regex, line) != None:
                sum += 1
            # print(line, re.fullmatch(regex, line))

    print("Puzzle 1:", sum)

def Puzzle2(input=[]):
    rules = {}

    # read in rules
    for line in input:        
        if ":" in line:
            s = line.split(": ")
            rules[s[0]] = [r.split(" ") for r in s[1].split(" | ")]
    # print(rules)
    
    # generate regex
    regex = BuildRegex(rules, "0", 10)
    # print("Regex:", regex)
    
    # print(re.fullmatch(regex, "aaaabbb") != None)    
    # check strings    
    sum = 0
    for line in input:
        if ":" not in line:
            if re.fullmatch(regex, line) != None:
                sum += 1
            # print(line, re.fullmatch(regex, line))

    print("Puzzle 2:", sum)

f = open("PuzzleInputs\\Day19.txt", "r")
Puzzle1(f.read().splitlines())
f.close()
f = open("PuzzleInputs\\Day19.txt", "r")
Puzzle2(f.read().splitlines())
f.close