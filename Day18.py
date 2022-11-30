def ResolveParentheses(exp=""):
    # print("Resolving parentheses: ", exp)
    i = 0
    numP = 1
    while numP > 0:
        i+=1
        if exp[i] == "(":
            numP += 1
        elif exp[i] ==")":
            numP -= 1

    # print("resolved ", exp[1:i], "pos ", i)  
    return exp[1:i], i
    

def EvaluateExp(exp=""):
    # print("Evaluating expression: ", exp)
    i = 0
    if exp[0] == "(":
        p = ResolveParentheses(exp[i:])
        value = EvaluateExp(p[0])
        i = p[1] + 1
    else:
        value = int(exp[0])
        i = 1

    while i < len(exp):
        c = exp[i]
        i += 1
        if c == "+":
            c = exp[i]
            if c.isdigit():
                value += int(c)
            elif c == "(":                
                p = ResolveParentheses(exp[i:])
                value += EvaluateExp(p[0])
                i += p[1]
        elif c == "*":
            c = exp[i]
            if c.isdigit():
                value *= int(c)
            elif c == "(":        
                p = ResolveParentheses(exp[i:])
                value *= EvaluateExp(p[0])
                i += p[1]
        i += 1

    # print("return", value)
    return value

def EvaluateExp2(exp = ""):
    # print("Evaluating expression: ", exp)
    i = 0
    if exp[0] == "(":
        p = ResolveParentheses(exp[i:])
        value = EvaluateExp2(p[0])
        i = p[1] + 1
    else:
        value = int(exp[0])
        i = 1

    while i < len(exp):
        c = exp[i]
        i += 1
        if c == "+":
            c = exp[i]
            if c.isdigit():
                value += int(c)
            elif c == "(":                
                p = ResolveParentheses(exp[i:])
                value += EvaluateExp2(p[0])
                i += p[1]
        elif c == "*":
            return value * EvaluateExp2(exp[i:])
            # c = exp[i]
            # if c.isdigit():
            #     return value * EvaluateExp2(exp[c:])
            #     # value *= int(c)
            # elif c == "(":        
            #     p = ResolveParentheses(exp[i:])
            #     return value * 
            #     value *= EvaluateExp2(p[0])
            #     i += p[1]
        i += 1

    # print("return", value)
    return value

def Puzzle1(input=[]):

    sum = 0

    for line in input:
        e = line.replace(" ", "")
        sum += EvaluateExp(e)

    print("Puzzle 1:", sum)


def Puzzle2(input=[]):
    sum = 0

    for line in input:
        e = line.replace(" ", "")
        # print(EvaluateExp2(e))
        sum += EvaluateExp2(e)

    print("Puzzle 2:", sum)


f = open("PuzzleInputs\\Day18.txt", "r")
Puzzle1(f.read().splitlines())
f.close()
f = open("PuzzleInputs\\Day18.txt", "r")
Puzzle2(f.read().splitlines())
f.close