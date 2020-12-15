from lbrinks_helpers import load_to_list
from itertools import product
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')
logging.disable(logging.CRITICAL)


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
    test = "".join(bits)
    new_value = [bits[i] if mask[i]==unchanged else mask[i] for i in range(36)]
    return int("".join(new_value), 2)

def floating_bits(address, mask):
    adresses = []
    x_count = mask.count("X")
    binaries = [list(bin(x)[2:].zfill(x_count)) for x in range(2**x_count)]
    logging.debug(f"mask: {mask}")
    for binary in binaries:
        masked = list(bin(int(address))[2:].zfill(36))
        x = 0
        for i in range(36):
            if mask[i] == "1":
                masked[i] = "1"
            if mask[i] == "X":
                masked[i] = binary[x]
                x += 1
        masked = "".join(masked)
        logging.debug(f"{masked}")
        logging.debug(f"{int(masked,2)}")
        adresses.append(masked)
    logging.debug(f"masks: {adresses}")
    return adresses

def decoder_v_2(instructions):
    mem = {}
    for line in instructions:
        parts = line.split()
        if parts[0].startswith("mem"):
            address = parts[0][4: -1]
            addresses = floating_bits(address, mask)
            logging.info(f"{addresses}")
            for a in addresses:
                mem[a] = parts[2]
        else:    
            mask = parts[2]
    
    print("Solution")
    print(sum([int(mem[address]) for address in mem]))
    return mem

instructions = load_to_list(".\\data\\2020_14.txt")


decoder_v_1(instructions)

decoder_v_2(instructions)