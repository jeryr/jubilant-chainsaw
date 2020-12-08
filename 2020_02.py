import advent_of_code_data as data

pwds = data.d2_input
test = data.d2_test
print(test)

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
           

pwd_valid_sledge(test)
pwd_valid_sledge(pwds)

pwd_valid_toboggan(test)
pwd_valid_toboggan(pwds)
