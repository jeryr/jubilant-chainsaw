from lbrinks_helpers import load_to_list
from itertools import product

def decoder_v_1(instructions):
    mem = {}
    for line in instructions:
        parts = line.split()
        if parts[0].startswith("mem"):
            address = parts[0][4: -1]
            mem[address] = bitmask(parts[2], mask)
        else:    
            mask = parts[2]

    print(sum([mem[address] for address in mem]))

def bitmask(value, mask, unchanged ="X"):
    bits = list(bin(int(value))[2:].zfill(36))
    new_value = [bits[i] if mask[i]==unchanged else mask[i] for i in range(36)]
    return int("".join(new_value), 2)

def floating_bits(mask):
    masks = []
    x_count = mask.count("X")
    binaries = [list(bin(x)[2:].zfill(x_count)) for x in range(2**x_count)]
    for binary in binaries:
        x = 0
        floating_mask = list(mask)
        for i in range(36):
            if floating_mask[i] == "X":
                floating_mask[i] = binary[x]
                x += 1
        masks.append(floating_mask)
    ["".join(value) for value in masks]
    return masks

def decoder_v_2(instructions):
    mem = {}
    for line in instructions:
        parts = line.split()
        if parts[0].startswith("mem"):
            address = parts[0][4: -1]
            addresses = [bitmask(address, mask, "0") for mask in masks]
            for a in addresses:
                mem[a] = parts[2]
        else:    
            masks = floating_bits(parts[2])
    
    print(sum([int(mem[address]) for address in mem]))
    return mem

instructions = load_to_list(".\\data\\2020_14.txt")

decoder_v_1(instructions)

mem = decoder_v_2(instructions)
s = 0
for key in mem:
    s += int(mem[key])
print(s)