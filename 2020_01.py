from lbrinks_helpers import load_to_list

expenses = load_to_list(".\\data\\2020_01.txt", int)


def tester_twice(v):
    for i in range(len(v)):
        for b in range(i, len(v)):
            if v[i] + v[b] == 2020:
                print(f"{v[i]} + {v[b]} = 2020")
                print(f"Product: {v[i]*v[b]}")
                break


def tester_thrice(v):
    for i in range(len(v)):
        for b in range(i, len(v)):
            for c in range(b, len(v)):
                if v[i] + v[b] + v[c] == 2020:
                    print(f"{v[i]} + {v[b]} + {v[c]} = 2020")
                    print(f"Product: {v[i]*v[b]*v[c]}")


tester_twice(expenses)
tester_thrice(expenses)
