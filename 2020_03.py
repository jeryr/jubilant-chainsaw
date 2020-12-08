import advent_of_code_data as data

forest = data.d3_input



def collisions(forest):
    trees = 0
    x = 0
    for row in forest:
        if row[x] == "#":
            trees +=1
        x += 3
        if x > 30:
            x -=31
    return trees


print(collisions(forest))

def multi_collision(forest, steerings):
    def collisions_better(forest, right, down):
        trees = 0
        x = 0
        for i in range(0,len(forest), down):
            if forest[i][x] == "#":
                trees +=1
            x += right
            if x > 30:
                x -=31
        return trees
    multis = 1
    for steering in steerings:
        multis *= collisions_better(forest, steering[0], steering[1])
    return multis

steerings = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

print(multi_collision(forest, steerings))
print(multi_collision(forest, [[3,1]]))

