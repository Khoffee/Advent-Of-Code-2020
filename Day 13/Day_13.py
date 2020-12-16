from math import ceil

def findNext(bus):
    global earliest
    return int(ceil(earliest/float(bus)))

with open ("input.txt", "r") as myfile:
    lines = myfile.readlines()
    input = [line.rstrip('\n') for line in lines]

# earliest = int(input[0])

# print("Earliest: " + str(earliest))
#buses = [int(x) 
# for x in input[1].split(',') if x != 'x']  FOR PART ONE

input_ex = '17,x,13,19'
input_ex2 = '17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,23,x,x,x,x,x,x,x,787,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'
departures = [x for x in input_ex2.split(',')]


print(departures.index("787") - departures.index("23"))
print(departures.index("787") - departures.index("19"))
print(departures.index("787") - departures.index("13"))
print(departures.index("787") - departures.index("523"))
print(departures.index("787") - departures.index("41"))
print(departures.index("787") - departures.index("17"))

print("The buses after")
print(departures.index("37") - departures.index("787"))
print(departures.index("29") - departures.index("787"))


t = 0
while True:
    t += 787
    if ((t % 17 == 14) and (t % 41 == 0) and (t % 523 == 31) and (t % 19 == 12) and (t % 23 == 8) and (t + 6)%37==0):
        break
    if (t > 100000000000):
        print("test123")

print(t - 48)
# print(t-3)

# bestBus = 15015935
# for bus in buses:
#     nextDeparture = findNext(bus)
#     print("This bus: " + str(bus))
#     nextDeparture = nextDeparture * bus
#     if ((bestBus * findNext(bestBus)) - earliest > (nextDeparture - earliest)):
#         bestBus = bus
#print((findNext(bestBus) * bestBus - earliest) * bestBus)