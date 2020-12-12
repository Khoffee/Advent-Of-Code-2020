currentx = 0
currenty = 0
face = 0

north = (0,1)
east = (1, 0)
south = (0, -1)
west = (-1, 0)
waypoint = [10, 1]

def translate(units, x, y):
    global currentx, currenty
    currentx += (units * x)
    currenty += (units * y)

def translateWaypoint(units, x, y):
    global waypoint
    waypoint[0] += (units * x)
    waypoint[1] += (units * y)

def forward(units):
    global face
    if((face % 360) == 0):
        translate(units, *east)
    if((face % 360) == 90):
        translate(units, *north)
    if((face % 360) == 180):
        translate(units, *west)
    if((face % 360) == 270):
        translate(units, *south)

def forwardWaypoint(units):
    global waypoint, currentx, currenty
    currentx += (waypoint[0] * units)
    currenty += (waypoint[1] * units)

def rotateClockwise():
    global waypoint
    temp = waypoint[0]
    waypoint[0] = waypoint[1]
    waypoint[1] = temp * (-1)

def rotateCounterClockwise():
    global waypoint
    temp = waypoint[0]
    waypoint[0] = (waypoint[1]) * (-1)
    waypoint[1] = temp

with open ("input.txt", "r") as myfile:
    lines = myfile.readlines()
    input = [line.rstrip('\n') for line in lines]

# for instruction in input:
#     if(instruction[0] == 'N'):
#         Waypoint(int(instruction[1:]), *north)
#     if(instruction[0] == 'S'):
#         Waypoint(int(instruction[1:]), *south)
#     if(instruction[0] == 'E'):
#         Waypoint(int(instruction[1:]), *east)
#     if(instruction[0] == 'W'):
#         Waypoint(int(instruction[1:]), *west)
#     if(instruction[0] == 'L'):
#         face = face + int(instruction[1:])
#     if(instruction[0] == 'R'):
#         face = face - int(instruction[1:])
#     if(instruction[0] == 'F'):
#         forward((int(instruction[1:])))
    
for instruction in input:
    if(instruction[0] == 'N'):
        translateWaypoint(int(instruction[1:]), *north)
    if(instruction[0] == 'S'):
        translateWaypoint(int(instruction[1:]), *south)
    if(instruction[0] == 'E'):
        translateWaypoint(int(instruction[1:]), *east)
    if(instruction[0] == 'W'):
        translateWaypoint(int(instruction[1:]), *west)
    if(instruction[0] == 'L'):
        for i in range(int(int(instruction[1:])/90)):
            rotateCounterClockwise()
    if(instruction[0] == 'R'):
        for i in range(int(int(instruction[1:])/90)):
            rotateClockwise()
    if(instruction[0] == 'F'):
        forwardWaypoint((int(instruction[1:])))

print("current x: " + str(currentx))
print("current y: " + str(currenty))
