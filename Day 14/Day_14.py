def bitfield(n):
    temp = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
    return ([0] * (36 - len(temp))) + temp

def findOccurrences(str, ch):
    return [i for i, letter in enumerate(str) if letter == ch]

def applyMask(zeroList, oneList, array):
    for item in zeroList:
        array[item] = 0
    for item in oneList:
        array[item] = 1
    return array

def applyMaskPartTwo(xList, oneList, array):
    for item in xList:
        array[item] = 'X'
    for item in oneList:
        array[item] = 1
    #floatingIndices = findOccurrences(str(array), 'X')
    resultList = []
    print("New Array: " + str(array))
    if((array[0] == 0) or (array[0] == 1)):
        resultList.append(str(array[0]))
    else:
        resultList = ['0', '1']
    for i in range(1, len(array)):
        if((array[i] == 0) or (array[i] == 1)):
            for j in range(len(resultList)):
                resultList[j] += str(array[i])
        else:
            resultList = [x + '0' for x in resultList] + [x + '1' for x in resultList]
    return resultList


with open ("input.txt", "r") as myfile:
    lines = myfile.readlines()
    input = [line.rstrip('\n') for line in lines]


for lines in input:
    print(lines)

#mask = input[0].lstrip('mask = ')
#print(mask)

myDict = {}

#Part One
# for i in range(0, len(input)):
#     if(input[i].startswith('mask')):
#         mask = input[i].lstrip('mask = ')
#         zeroOccurrences = findOccurrences(mask, '0')
#         oneOccurrences = findOccurrences(mask, '1')
#         xOccurrences = findOccurrences(mask, 'X')
#     else:
#         myDict[str(input[i][4:input[i].rfind(']')])] = applyMask(zeroOccurrences, oneOccurrences, bitfield(int(input[i].split('= ')[1])))

print("Part Two Debugging")
#Part Two
for i in range(0, len(input)):
    if(input[i].startswith('mask')):
        mask = input[i].lstrip('mask = ')
        oneOccurrences = findOccurrences(mask, '1')
        xOccurrences = findOccurrences(mask, 'X')
    else:
        originalAddress = int(input[i][4:input[i].rfind(']')])
        print("Original Address: " + str(originalAddress))
        newAddresses = applyMaskPartTwo(xOccurrences, oneOccurrences, bitfield(originalAddress))
        print("New Addresses: " + str(newAddresses))
        for item in newAddresses:
            res = int("".join(str(x) for x in item), 2) 
            print(int(input[i].split('= ')[1]))
            myDict[str(res)] = int(input[i].split('= ')[1])

print(myDict)

values = myDict.values()

total = 0
for item in values:
    total += item

print(total)

# for k, v in myDict.items():
#     myDict[k] = 
