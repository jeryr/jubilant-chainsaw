from lbrinks_helpers import load_to_list
from functools import lru_cache


def count_jumps(adapters):
    adapters.sort()
    # the last adapter isn't evaluated, this prevents an out of index error
    jumps = [0, 1]
    for i in range(len(adapters)-1):
        if adapters[i+1] - adapters[i] == 1:
            jumps[0] += 1
        # there don't seem to be any adapters 2 apart.
        else:
            jumps[1] += 1
    return jumps

# keeps already evaluated function calls in memory, memoized.


@lru_cache(None)
def count_ways(index):
    # if it's on the last adapter, there is only one way to go.
    if index == len(adapters) - 1:
        return 1
    total = 0
    nextIndex = index + 1
    # the first condition prevents an out of index error, the second condition evaluates all possible next adapters, i.e. all three joltages away.
    while nextIndex < len(adapters) and adapters[nextIndex] - adapters[index] <= 3:
        # the recursion part
        total += count_ways(nextIndex)
        nextIndex += 1
    return total


# the zero here is needed for the second part, the possible combinations.
adapters = [0] + load_to_list(".\\data\\2020_10.txt", int)
adapters.sort()

jumps = count_jumps(adapters)

solution = count_ways(0)


print(jumps)
print(jumps[0]*jumps[1])
print(solution)
