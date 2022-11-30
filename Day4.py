f = open("PuzzleInputs\\Day4.txt", "r")
input = f.read().splitlines()
f.close()

def CheckColor(color):
    if color[0] != '#':
        return False
    if color.__len__() != 7:
        return False
    for c in color[1:]:
        if (c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9' or c == 'a' or c == 'b' or c == 'c' or c == 'd' or c == 'e' or c == 'f') == False:
            return False
    return True

passports = []
pp = {}
for line in input:
    
    if line.__len__() > 0:
        for field in line.split(' '):
            pp[field.split(':')[0]] = field.split(':')[1]
    else:
        passports.append(pp)
        pp = {}    
passports.append(pp)

valid = 0
for p in passports:
    if p.get("byr") != None and p.get("iyr") != None and p.get("eyr") != None and p.get("hgt") != None and p.get("hcl") != None and p.get("ecl") != None and p.get("pid") != None:
        byr = int(p.get("byr"))
        if(byr < 1920 or byr > 2002):
            print("invalid byr")
            continue

        iyr = int(p.get("iyr"))
        if(iyr < 2010 or iyr > 2020):
            print("invalid iyr")
            continue

        eyr = int(p.get("eyr"))
        if(eyr < 2020 or eyr > 2030):
            print("invalid eyr")
            continue

        hgt = p.get("hgt")
        if hgt[-2:] == "cm":
            if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
                print("invalid hgt cm")
                continue
        elif hgt[-2:] == "in":
            if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
                print("invalid hgt in")
                continue
        else:
            print("invalid hgt")
            continue

        hcl = p.get("hcl")
        if CheckColor(hcl) == False:
            print("invalid hcl")
            continue

        ecl = p.get("ecl")
        if (ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth") == False:
            print("invalid ecl")
            continue
                
        pid = p.get("pid")
        if pid.__len__() != 9:
            print("invalid pid length")
            continue
        try:
            int(pid)
        except ValueError:
            print("invalid pid value")
            continue

        valid += 1

print("Valid passports: " + str(valid))
        