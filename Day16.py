class FieldRule:
    fieldname = ""
    min1 = 0
    max1 = 0
    min2 = 0
    max2 = 0
    index = -1

    def __init__(self, line=""):
        split1 = line.split(':')
        self.fieldname = split1[0]
        values1 = split1[1].split(' ')[1]
        values2 = split1[1].split(' ')[3]
        self.min1 = int(values1.split('-')[0])
        self.max1 = int(values1.split('-')[1])
        self.min2 = int(values2.split('-')[0])
        self.max2 = int(values2.split('-')[1])

    def GetName(self):
        return self.fieldname

    def IsValueValid(self, value=0):
        return (value >= self.min1
                and value <= self.max1) or (value >= self.min2
                                            and value <= self.max2)


def SplitInput(input=[]):
    rules = []

    i = 0
    while True:
        line = input[i]
        if len(line) == 0:
            i += 2
            break
        rules.append(FieldRule(line))
        i += 1

    myticket = list(map(int, input[i].split(',')))
    i += 3

    tickets = []

    while i < len(input):
        tickets.append(list(map(int, input[i].split(','))))
        i += 1

    return rules, tickets, myticket


def Puzzle1(input=[]):
    ret = SplitInput(input)
    rules = ret[0]
    tickets = ret[1]
    errorRate = 0

    for t in tickets:
        # print(t)
        for v in t:
            # print("Value ", v)
            valid = False
            for r in rules:
                if r.IsValueValid(v):
                    # print(r.fieldname)
                    valid = True
            
            # print(valid)
            if not valid:
                errorRate += v

    print("Puzzle 1 scanning error rate: ", errorRate)


def Puzzle2(input=[]):
    ret = SplitInput(input)
    rules = ret[0]
    tickets = ret[1]
    myticket = ret[2]
    invtickets = []

    for t in tickets:
        # print("Ticket ", t)
        ticketvalid = True
        for v in t:
            # print("Value ", v)
            valid = False
            for r in rules:
                if r.IsValueValid(v):
                    valid = True
            
            # print(valid)
            if not valid:
                ticketvalid = False
                break
        if not ticketvalid:
            invtickets.append(t)

    tickets = [t for t in tickets if t not in invtickets]
    # print(tickets)
                    
    validrules = []

    for i in range(len(tickets[0])):
        validrulesTemp = []
        for r in rules:
            bValid = True
            for t in tickets:
                if not r.IsValueValid(t[i]):
                    bValid = False
            if bValid:
                validrulesTemp.append(r)
        validrules.append(validrulesTemp)
     
    
    numMatched = 0
    departureIndices = []
    while numMatched < len(validrules):
        for i, v in enumerate(validrules):
            if len(v) == 1:
                matchedrule = v[0]
                print(matchedrule.fieldname, i)
                if matchedrule.fieldname.startswith("departure"):
                    departureIndices.append(i)
                numMatched += 1
                # validrules.remove(v)
                break

        for v in validrules:
            if matchedrule in v:
                v.remove(matchedrule)
    
    solution = 1
    for i in departureIndices:
        solution *= myticket[i]
    print("Puzzle 2: ", solution)


f = open("PuzzleInputs\\Day16.txt", "r")
Puzzle1(f.read().splitlines())
f.close()
f = open("PuzzleInputs\\Day16.txt", "r")
Puzzle2(f.read().splitlines())
f.close