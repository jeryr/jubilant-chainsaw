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


def transformer(seating, row=91, column=97):
    """Returns a transformator matrix that multiplicatively changes the seating area to the next round (part 1)"""
    transform = np.ones(seating.shape)
    easy = np.where(seating == -1, 0, seating)
    for r in range(1, row):
        for c in range(1, column):
            if seating[r, c] == 1:
                # this needs to be one higher than the specified 4, since the own seat is counted
                if easy[r-1:r+2, c-1:c+2].sum() >= 5:
                    transform[r, c] = -1
            elif seating[r, c] == -1:
                if easy[r-1:r+2, c-1:c+2].sum() == 0:
                    transform[r, c] = -1
            else:
                continue
    return transform.astype(np.int32)


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
    # left
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
            if seating[r, column-r+row] == -1:
                break
            if seating[r, column-r+row] == 1:
                adjacent_view += 1
                break
        except IndexError:
            break
    # down-left
    for r in range(row+1, row_max):
        if column-r+row == 0:
            break
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
        if column+r-row == 0:
            break
        try:
            if seating[r, column+r-row] == -1:
                break
            if seating[r, column+r-row] == 1:
                adjacent_view += 1
                break
        except IndexError:
            break
    return adjacent_view


def change(seating, row=91, column=97):
    """Returns the transformative matrix according to rules in part 2"""
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


def find_equilibrium(seatings, method):
    """Applies the specified method on the seating area, until no more changes occur and prints the sum of occupied seats"""
    seating = seatings.copy()
    condition = np.ones(seating.shape)
    transformator = np.zeros(seating.shape)
    while np.any(transformator != condition):
        transformator = method(seating)
        seating *= transformator
    print(seating[seating == 1].sum())


seating = seating_to_matrix(load_to_list(".\\data\\2020_11.txt"))

find_equilibrium(seating, transformer)
find_equilibrium(seating, change)
