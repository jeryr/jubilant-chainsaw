from lbrinks_helpers import load_instruction_list


def read_instruction(instruction):
    """Returns the relative position of the next instruction and the change for accumulation"""
    instruction, value = instruction[0], instruction[1]
    if instruction == "nop":
        return 1, 0
    if instruction == "jmp":
        return value, 0
    if instruction == "acc":
        return 1, value


def generate_lists(instructions):
    """Yields all lists, in which one nop <=> jmp conversion has taken place."""
    for i in range(len(instructions)):
        if instructions[i][0] == "acc":
            continue
        if instructions[i][0] == "nop":
            yield [instructions[j] if j != i else ["jmp", instructions[j][1]] for j in range(len(instructions))]
        if instructions[i][0] == "jmp":
            yield [instructions[j] if j != i else ["nop", instructions[j][1]] for j in range(len(instructions))]


def find_loop(instructions, check_for_endless=False):
    """Prints and returns the value in the accumulation variable. If check_for_endless it only prints this value and return True if there was no endless loop."""
    accumulation = 0
    used = []
    used.append(len(instructions))
    i = 0
    while i not in used:
        used.append(i)
        i_p, accumulation_p = read_instruction(instructions[i])
        i += i_p
        accumulation += accumulation_p
    if not check_for_endless:
        print(accumulation)
        return(accumulation)
    if check_for_endless:
        if i == len(instructions):
            print(accumulation)
            return True
        return False


instructions = load_instruction_list(".\\data\\2020_08.txt")
find_loop(instructions)

p = generate_lists(instructions)

for changed_instructions in p:
    if find_loop(changed_instructions, True):
        break
