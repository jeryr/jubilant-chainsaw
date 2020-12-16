from lbrinks_helpers import load_to_list
import numpy as np


def XMAS(xmas, preamble):
    for i in range(preamble, len(xmas)):
        if has_sum(xmas[i], xmas[i-preamble:i]):
            continue
        else:
            print(xmas[i])
            return xmas[i]


def has_sum(x, code):
    for i in range(len(code)):
        for j in range(i+1, len(code)):
            if code[i] + code[j] == x:
                return True
    return False


def weakness(xmas, x):
    for i in range(len(xmas)):
        t = xmas[i]
        j = i + 1
        while t <= x:
            if t == x:
                solution = np.array(xmas[i:j])
                print(i)
                print(j-1)
                return(solution.max() + solution.min())
            t += xmas[j]
            j += 1


crypto = load_to_list(".\\data\\2020_09.txt", int)

weakpoint = XMAS(crypto, 25)
print(weakness(crypto, weakpoint))
