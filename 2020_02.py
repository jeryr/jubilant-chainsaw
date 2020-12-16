def pwd_valid_sledge(pwd_list):
    valid_pwds = 0
    for pwd in pwd_list:
        least = pwd[0]
        most = pwd[1]
        character = pwd[2]
        password = pwd[3]
        occurences = password.count(character)
        if least <= occurences <= most:
            valid_pwds += 1
    print(f"There were {valid_pwds} valid passwords")


def pwd_valid_toboggan(pwd_list):
    valid_pwds = 0
    for pwd in pwd_list:
        valid = 0
        p1 = pwd[0]-1
        p2 = pwd[1]-1
        character = pwd[2]
        password = pwd[3]
        valid += password.count(character, p1, p1+1)
        valid += password.count(character, p2, p2+1)
        if valid == 1:
            valid_pwds += 1
    print(f"There were {valid_pwds} valid passwords")


def pwd_seperator(line):
    a, b, pwd = line.split()
    low, high = a.split("-")
    character = b[0]
    return [int(low), int(high), character, pwd]


with open(".\\data\\2020_02.txt") as file:
    content = file.read().splitlines()

pwds = [pwd_seperator(line) for line in content]

pwd_valid_sledge(pwds)
pwd_valid_toboggan(pwds)
