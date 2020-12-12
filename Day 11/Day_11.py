import copy


def adjacency(comparison, x, y):
    neighbors = comparison[x - 1][y] + comparison[x][y - 1] + comparison[x - 1][y - 1] + comparison[x + 1][y] + comparison[x][y + 1] + comparison[x + 1][y + 1] + comparison[x + 1][y - 1] + comparison[x - 1][y + 1]
    count = neighbors.count('#')
    return count


def partTwoAdjacency(comparison, x, y):
    count = 0
    northWest = (-1, -1)
    north = (-1, 0)
    northEast = (-1, 1)
    east = (0, 1)
    southEast = (1, 1)
    south = (1, 0)
    southWest = (1, -1)
    west = (0, -1)
    count = goDirection(comparison, x, y, *northWest) + goDirection(comparison, x, y, *north) + goDirection(comparison, x, y, *northEast) + goDirection(comparison, x, y, *east) + goDirection(comparison, x, y, *southEast) + goDirection(comparison, x, y, *south) + goDirection(comparison, x, y, *southWest) + goDirection(comparison, x, y, *west)
    return count


def goDirection(comparison, currentx, currenty, x, y):
        while(((0 <= currentx < len(comparison)) and (0 <= currenty < len(comparison[0])))):
            currentx = currentx + x
            currenty = currenty + y
            try:
                if(comparison[currentx][currenty] == '#'):
                    return 1
                if(comparison[currentx][currenty] == 'L'):
                    return 0
            except IndexError:
                return 0
        return 0


def mutate(matrix, comparison):
    for row in range((len(matrix))):
        for col in range((len(matrix[0]))):
            if(comparison[row][col] == 'L'):
                if(partTwoAdjacency(comparison, row, col) == 0):
                    matrix[row][col] = '#'
            if(comparison[row][col] == '#'):
                if(partTwoAdjacency(comparison, row, col) >= 5):
                    matrix[row][col] = 'L'
    return matrix


def countOccupied(input):
    total = 0
    for line in range(len(input)):
        total += input[line].count('#')
    return total


input = []
comparison = []
iterations = 0

with open ("input_ex.txt", "r") as myfile:
    for i in myfile.readlines():
        i = i.strip()
        input.append(list(i))

input.insert(0, (['.'] * (len(input[0]))))
input.insert(len(input)+999, (['.'] * (len(input[0]))))
for line in range(len(input)):
    input[line].insert(0, '.')
    input[line].insert(len(input[line])+999, '.')
    print(input[line])

while (input != (comparison)):
    iterations += 1
    print("Iteration: " + str(iterations))
    comparison = copy.deepcopy(input)
    input = mutate(input, comparison)
    for line in input:
        print(line)

print(countOccupied(input))
