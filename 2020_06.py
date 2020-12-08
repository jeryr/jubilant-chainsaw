with open(".\\data\\2020_06.txt") as file:
    content = file.read().splitlines()
    customs = []
    custom = []
    for line in content:
        if line == "":
            customs.append(custom)
            custom = []
        else:
            custom.append(set(line))
    if custom != []:
            customs.append(custom)

yes = 0 

for form in customs:
    declared = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    for item in form:
        declared = declared.intersection(item)
    yes += len(declared)

print(yes)



