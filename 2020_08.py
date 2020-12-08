def load_input():    
    with open(".\\data\\2020_08.txt") as file:
        content = file.read().splitlines()
        instructions = []
        for line in content:
            instruction, value = line.split()
            instructions.append([instruction, int(value)])
        return instructions

def read_instruction(instruction):
    instruction, value = instruction[0], instruction[1]

    if instruction == "nop":
        return 1
    if instruction == "jmp":
        return value
    if instruction == "acc":
       global accumulation
       accumulation += value
       return 1

instructions = load_input()

accumulation = 0


used = []

i = 0

while i not in used:
    used.append(i)
    i += read_instruction(instructions[i])








    
    if i == len(instructions)-1:
return TRUE
        break
else:
    return False

print(accumulation)
