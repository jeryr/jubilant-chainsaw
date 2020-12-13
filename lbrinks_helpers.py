"""Functions that promise to have usefulness for more than one challenge, or even project"""

def load_to_list(file, fun = None):  
    """Returns a list of each line of the file with the supplied function applied."""  
    with open(file) as file:
        content = file.read().splitlines()
        if fun == None:
            return content
        output = [fun(line) for line in content]
        return output


def load_instruction_list(filepath, sep=" ", fun=int):
    """Generates a list of 2 item lists, containing string-fun pairs, sepearated at sep."""    
    with open(filepath) as file:
        content = file.read().splitlines()
        instructions = []
        for line in content:
            instruction, value = line.split(sep= sep)
            instructions.append([instruction, fun(value)])
        return instructions