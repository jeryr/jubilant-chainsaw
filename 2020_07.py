def load_input():    
    with open(".\\data\\2020_07.txt") as file:
        content = file.read().splitlines()
        bags = {}
        for line in content:
            line = line[:-1]
            outer_bag, contains = line.split(" contain ")
            containing = {}
            contains = contains.split(", ")
            for inner_bag in contains:
                value, key = inner_bag.split(" ", 1)
                if value == "1":
                    containing[key+ "s"] = int(value)
                elif value == "no":
                    containing[key] = 0
                else:
                    containing[key] = int(value)
            bags[outer_bag] = containing
    return bags

# Now we got a dictionary! 

# recursive lookup
def bag_search(bag, my_bag, bags):
    if bag not in bags.keys():
        return False
    if my_bag in bags[bag].keys(): 
        return True
    for inner_bag in bags[bag]:
        if bag_search(inner_bag, my_bag, bags):
            return True
    return False

def bag_contains(bag, bags):
    if bag not in bags.keys():
        return 0
    contains = 0
    for inner_bag in bags[bag]:
        containing = bags[bag][inner_bag]
        contains += containing + containing*bag_contains(inner_bag, bags)
    return contains






bags = load_input()

solution_1 = [bag_search(bag, "shiny gold bags", bags) for bag in bags]

print(sum(solution_1))


print(bag_contains("shiny gold bags", bags))

