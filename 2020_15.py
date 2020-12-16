import numpy as np
from collections import defaultdict


def memory_game(starting_in, n):
    spoken = defaultdict(lambda: -1)
    # otherwise you can't run this function twice, since it modifies global values
    starting = starting_in.copy()
    last = starting.pop(-1)
    for i in range(len(starting)):
        spoken[starting[i]] = i
    for i in range(len(starting), n-1):
        # -1 signifies never used
        if spoken[last] == -1:
            # store the first time it was spoken
            spoken[last] = i
            # get the next element
            last = 0
        else:
            t = i-spoken[last]
            spoken[last] = i
            last = t
    print(last)
    return last


starting = [7, 14, 0, 17, 11, 1, 2]

memory_game(starting, 2020)

memory_game(starting, 30000000)
