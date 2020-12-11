from lbrinks_helpers import load_to_list

adapters = load_to_list(".\\data\\2020_10.txt", int)

adapters.sort()

jumps = [1, 1]

for i in range(len(adapters)-1):
    if adapters[i+1] - adapters[i] == 1:
        jumps[0] += 1
    else:
        jumps[1] += 1

print(len(adapters))
print(jumps)
print(jumps[0]*jumps[1])