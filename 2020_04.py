
def papers_complete(passport, sufficient, complete):
    fields = set(passport.keys())
    if fields == sufficient or fields == complete:
        return True
    else:
        return False

def papers_validate(passport, conditions):
    for validation in conditions:
        if not validation(passport):
            break
    else: 
        return True

def byr(passport):
    byr = int(passport["byr"])
    if 1920 <= byr <= 2002:
        return True
    else:
        return False

def iyr(passport):
    iyr = int(passport["iyr"])
    if 2010 <= iyr <= 2020:
        return True
    else:
        return False

def eyr(passport):
    if 2020 <= int(passport["eyr"]) <= 2030:
        return True
    else:
        return False

def hgt(passport):
    unit = passport["hgt"][-2:]
    value = int(passport["hgt"][:-2])
    if unit == "cm":
        if 150 <= value <=193:
            return True 
        else:
            return False
    elif unit == "in":
        if 59 <= value <= 76:
            return True
        else:
            return False

def hcl(passport):
    if len(passport["hcl"]) == 7:
        return True
    else:
        return False

def ecl(passport, acceptable = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
    if passport["ecl"] in acceptable:
        return True
    else:
        return False

def pid(passport):
    if len(passport["pid"]) == 9:
        return True
    else:
        return False


def papers_please(passports, sufficient, complete, validate):
    valid_papers = 0
    for passport in passports:
        if papers_complete(passport, sufficient, complete):
            if papers_validate(passport, validate):
                valid_papers += 1
    return valid_papers


with open(".\\data\\2020_04.txt") as file:
    content = file.read().splitlines()
    passports = []
    current_passport = {}
    print(content[-4])
    for line in content:
        line = line.split()
        if line == []:
            passports.append(current_passport)
            current_passport = {}
        for pair in line:
            key, value = pair.split(":")
            current_passport[key] = value
    if content[-1] != "":
        passports.append(current_passport)



sufficient = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
validate = [byr, iyr, eyr, hgt, hcl, ecl, pid]
complete = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])

print(papers_please(passports, sufficient, complete, validate))

    
