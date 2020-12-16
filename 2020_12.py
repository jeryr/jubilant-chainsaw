from lbrinks_helpers import load_to_list
import numpy as np
import math


def rotate(heading, degrees):
    """Returns the heading turned counter-clockwise by degrees"""
    radians = math.radians(degrees)
    x, y = heading
    xx = x * math.cos(radians) + y * math.sin(radians)
    yy = -x * math.sin(radians) + y * math.cos(radians)
    # the second part experienced trouble without rounding here.
    return round(xx), round(yy)


def move_ship(course):
    position = np.array([0, 0])
    heading = np.array([0, 1])
    move = {
        "F": heading,
        "N": np.array([1, 0]),
        "S": np.array([-1, 0]),
        "E": np.array([0, 1]),
        "W": np.array([0, -1])
    }
    for i in course:
        if i[0] == "L":
            heading[0], heading[1] = rotate(heading, i[1])
            continue
        if i[0] == "R":
            heading[0], heading[1] = rotate(heading, -i[1])
            continue
        position += move[i[0]]*i[1]
    print(np.abs(position).sum())


def move_waypoint(course):
    waypoint = np.array([1, 10])
    position = np.array([0, 0])
    move = {
        "N": np.array([1, 0]),
        "S": np.array([-1, 0]),
        "E": np.array([0, 1]),
        "W": np.array([0, -1])
    }
    for i in course:
        if i[0] == "L":
            waypoint[0], waypoint[1] = rotate(waypoint, i[1])
            continue
        if i[0] == "R":
            waypoint[0], waypoint[1] = rotate(waypoint, -i[1])
            continue
        if i[0] == "F":
            position += waypoint*i[1]
            continue
        waypoint += move[i[0]]*i[1]
    print(np.abs(position).sum())


course = load_to_list(".\\data\\2020_12.txt")
course = [[i[0], int(i[1:])] for i in course]

move_ship(course)

move_waypoint(course)
