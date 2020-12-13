from lbrinks_helpers import load_to_list
import numpy as np
# this problems requires on go to determine the changes, and one to apply the changes. if you change in place, the puzzle doesn't work. 
# perhaps use numpy matrices, represent taken seats as 1, free seats as -1 and floor as 0. then elementwise changes can be performed by multiplying, *-1 for a change. if the changing matrix stays all ones, there is an equilibrium. 

def seating_to_matrix(seating):
    """Transforms the list of string to a matrix, and adds a row and column of floor to the end"""
    matrix = [[0]+[-1 if c == "L" else 0 for c in row]+[0] for row in seating]
    matrix.insert(0, [0 for i in range(len(seating[0])+2)])
    matrix.append([0 for i in range(len(seating[0])+2)])
    seating = np.array(matrix)
    return seating

# these next two should be combined into on function
def will_be_vacated(seating, row=91, column=97):
    """Checks wether a seat will be vacated in the next round"""
    vacated = np.ones(seating.shape)
    easy = np.where(seating == -1, 0, seating)
    for r in range(1, row):
        for c in range(1, column):
            if easy[r,c] == 0:
                continue
            # this needs to be one higher than the specified 4, since the own seat is counted
            if easy[r-1:r+2, c-1:c+2].sum() >= 5:
                vacated[r,c] = -1
    return vacated.astype(np.int32)

def will_be_occupied(seating, row=91, column=97):
    """Checks wether a seat will be occupied in the next round"""
    occupied = np.ones(seating.shape)
    easy = np.where(seating == -1, 0, seating)
    for r in range(1, row):
        for c in range(1, column):
            if seating[r,c] == -1:
                if easy[r-1:r+2, c-1:c+2].sum() == 0:
                    occupied[r,c] = -1
    return occupied.astype(np.int32)

# this approach no longer works for part two. no we have to check the next most adjacent seat in each direction. seat[c,c]. Also we now have to handle out of index errors. This isn't the most elegant solution, but...

def occupied_around(seating, row, column, row_max=91, column_max=97):
    """Returns the amount of taken seats that can be seen from the specified seat"""
    adjacent_view = 0
    # down
    for r in range(row+1, row_max):
        if seating[r, column] == -1:
            break
        if seating[r, column] == 1:
            adjacent_view += 1
            break
    # up
    for r in range(row-1, 0, -1):
        if seating[r, column] == -1:
            break
        if seating[r, column] == 1:
            adjacent_view += 1
            break
    # right
    for c in range(column+1, column_max):
       if seating[row, c] == -1:
           break
       if seating[row, c] == 1:
            adjacent_view += 1
            break 
    # right
    for c in range(column-1, 0, -1):
        if seating[row, c] == -1:
            break
        if seating[row, c] == 1:
            adjacent_view += 1
            break 
    # down-right
    for r in range(row+1, row_max): 
        try:
            if seating[r, column+r-row] == -1:
                break
            if seating[r, column+r-row] == 1:
                adjacent_view += 1
                break
        except IndexError:
            break
    # up-right
    for r in range(row-1, 0, -1): 
        try:
            if seating[r, column+r-row] == -1:
                break
            if seating[r, column+r-row] == 1:
                adjacent_view += 1
                break
        except IndexError:
            break
    # down-left
    for r in range(row+1, row_max): 
        try:
            if seating[r, column-r+row] == -1:
                break
            if seating[r, column-r+row] == 1:
                adjacent_view += 1
                break
        except IndexError:
            break
    # up-left
    for r in range(row-1, 0, -1): 
        try:
            if seating[r, column-r+row] == -1:
                break
            if seating[r, column-r+row] == 1:
                adjacent_view += 1
                break
        except IndexError:
            break
    return adjacent_view
    
def change(seating, row = 91, column = 97):
    changing = np.ones(seating.shape)
    for r in range(1, row):
        for c in range(1, column):
            if seating[r][c] == -1:
                if occupied_around(seating, r, c) == 0:
                    changing[r][c] = -1
            if seating[r][c] == 1:
                # here the seat itself isn't counted
                if occupied_around(seating, r, c) >= 5:
                    changing[r][c] = -1
    return changing.astype(np.int32)





seating = seating_to_matrix(load_to_list(".\\data\\2020_11.txt"))
test_case = seating_to_matrix(load_to_list(".\\data\\2020_11_test.txt")) 

# condition = np.ones(seating.shape)
# transformator = np.zeros(seating.shape)


# while np.any(transformator != condition):
#     transformator = will_be_occupied(seating) * will_be_vacated(seating)
#     seating *= transformator

# print(np.where(seating == -1, 0, seating).sum())

# transformator = np.zeros(seating.shape)
# seating = seating_to_matrix(load_to_list(".\\data\\2020_11.txt"))


# while np.any(transformator != condition):
#      transformator = change(seating)
#      seating *=transformator

# print(np.where(seating == -1, 0, seating).sum())