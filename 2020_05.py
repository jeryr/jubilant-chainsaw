import numpy as np

def load_list(filepath, slice):
    integer_list = []
    with open(filepath) as file:
        content = file.read().splitlines()
        for line in content:
            line1, line2 = line[:slice], line[slice:]
            # Convert first to a true binary string and then directly to a an integer base 10
            line1 = line1.replace("F", "0").replace("B", "1")
            line1 = int(line1, 2)
            line2 = int(line2.replace("L", "0").replace("R", "1"), 2)
            integer_list.append([line1, line2])
    return integer_list


b = load_list(".\\data\\2020_05.txt", 7)
b = np.array(b)

seat_ids = b[:,0]*8+b[:,1]
print(seat_ids.max())

min_seat = seat_ids.min()

# use the formula for continous sums (n+1)n/2 to find the missing value

should = len(seat_ids) * (len(seat_ids)+1) / 2

my_seat = should - sum(seat_ids - min_seat) + min_seat

print(int(my_seat))
