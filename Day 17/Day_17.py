import copy


def adjacency(comparison, z, x, y):
    neighbors = (comparison[z][x-1][y-1] + 
                comparison[z][x-1][y] + 
                comparison[z][x-1][y+1] + 
                comparison[z][x][y-1] + 
                comparison[z][x][y+1] + 
                comparison[z][x+1][y-1] + 
                comparison[z][x+1][y] + 
                comparison[z][x+1][y+1] +
                comparison[z-1][x-1][y-1] + 
                comparison[z-1][x-1][y] + 
                comparison[z-1][x-1][y+1] + 
                comparison[z-1][x][y-1] + 
                comparison[z-1][x][y+1] + 
                comparison[z-1][x+1][y-1] + 
                comparison[z-1][x+1][y] + 
                comparison[z-1][x+1][y+1] +
                comparison[z+1][x-1][y-1] + 
                comparison[z+1][x-1][y] + 
                comparison[z+1][x-1][y+1] + 
                comparison[z+1][x][y-1] + 
                comparison[z+1][x][y+1] + 
                comparison[z+1][x+1][y-1] + 
                comparison[z+1][x+1][y] + 
                comparison[z+1][x+1][y+1] +
                comparison[z-1][x][y] + 
                comparison[z+1][x][y])
    count = neighbors.count('#')
    return count

# def countOccupied(input):
#     total = 0
#     for line in range(len(input)):
#         total += input[line].count('#')
#     return total

def mutate(cube, comparison):
    for z in range(1, len(cube)-1):
        for x in range(1, len(cube[z]) - 1):
            for y in range(1, len(cube[z][x]) - 1):
                if(comparison[z][x][y] == '#'):
                    if((adjacency(comparison, z, x, y) == 2) or (adjacency(comparison, z, x, y) == 3)):
                        cube[z][x][y] = '#'
                    else:
                        cube[z][x][y] = '.'
                if(comparison[z][x][y] == '.'):
                    if(adjacency(comparison, z, x, y) == 3):
                        cube[z][x][y] = '#'
    return cube

input = []
iterations = 0
cube = [[]]
comparison = [[]]

with open ("input.txt", "r") as myfile:
    for i in myfile.readlines():
        i = i.strip()
        input.append(list(i))

cube[0] = input

for z in range(len(cube)):
    print("Z = " + str(z))
    for x in range(len(cube[z])):
        print(cube[z][x])

print()

def padding(cube):
    for z in range(len(cube)):
        cube[z].insert(0, (['.'] * (len(cube[z][0]))))
        cube[z].insert(len(cube[z])+999, (['.'] * (len(cube[z][-1]))))
        for x in range(len(cube[z])):
            cube[z][x] = ['.'] + cube[z][x] + ['.']
    cube.insert(0, ( [ ['.'] * len(cube[-1][0]) ] * len(cube[-1])) )
    cube.insert(99999, ( [ ['.'] * len(cube[-1][-1]) ] * len(cube[-1])))
    return cube

# for z in range(len(cube)):
#     print("Z = " + str(z))
#     for x in range(len(cube[z])):
#         print(cube[z][x])
cube = padding(cube)
for i in range(6):
    iterations += 1
    print("Iteration: " + str(iterations))
    cube = padding(cube)
    comparison = copy.deepcopy(cube)
    cube = mutate(cube, comparison)
    for z in range(len(cube)):
        print("Z = " + str(z))
        for x in range(len(cube[z])):
            print(cube[z][x])

total = 0
for z in range(len(cube)):
    print("Z = " + str(z))
    for x in range(len(cube[z])):
        count = cube[z][x].count('#')
        total += count

print(total)

# while (cube != (comparison)):
#     iterations += 1
#     print("Iteration: " + str(iterations))
#     cube = padding(cube)
#     comparison = copy.deepcopy(cube)
#     cube = mutate(cube, comparison)
#     for z in range(len(cube)):
#         print("Z = " + str(z))
#         for x in range(len(cube[z])):
#             print(cube[z][x])

# input.insert(0, (['.'] * (len(input[0]))))
# input.insert(len(input)+999, (['.'] * (len(input[0]))))
# for line in range(len(input)):
#     input[line].insert(0, '.')
#     input[line].insert(len(input[line])+999, '.')

# for row in input:
#     print(row)


# while (input != (comparison)):
#     iterations += 1
#     print("Iteration: " + str(iterations))
#     comparison = copy.deepcopy(input)
#     input = mutate(input, comparison)
#     for line in input:
#         print(line)