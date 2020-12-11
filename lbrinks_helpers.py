"""Functions that promise to have usefulness for more than one challenge, or even project"""

def load_to_list(file, fun = None):  
    """Returns a list of each line of the file with the supplied function applied."""  
    with open(file) as file:
        content = file.read().splitlines()
        if fun == None:
            return content
        output = [fun(line) for line in content]
        return output
