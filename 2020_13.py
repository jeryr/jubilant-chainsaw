import numpy as np
from sympy.ntheory.modular import crt

x = "x"
timestamp = 1007268
buslines = [17, x, x, x, x, x, x, 41, x, x, x, x, x, x, x, x, x, 937, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x,
            x, x, 13, x, x, x, x, 23, x, x, x, x, x, 29, x, 397, x, x, x, x, x, 37, x, x, x, x, x, x, x, x, x, x, x, x, 19]
bus_id = [i for i in buslines if i != "x"]

in_service = np.array(bus_id)
next_bus = np.ceil(timestamp / in_service) * in_service - timestamp
print(int(in_service[np.argmin(next_bus)] * next_bus.min()))

residue = [-i % buslines[i]
           for i in range(len(buslines)) if buslines[i] != "x"]
print(crt(bus_id, residue))
