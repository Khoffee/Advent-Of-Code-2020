def initializeDict(inputList, myDict):
    for i in range(len(inputList)):
        myDict[inputList[i]] = [i+1, i+1]

def countingGame(myDict, turns, lastSpoken):
    if lastSpoken not in myDict.keys():
        myDict[lastSpoken] = [0, len(myDict)]
    else:
        myDict[lastSpoken][0] = myDict[lastSpoken][1]
        myDict[lastSpoken][1] = len(myDict)+1
    for i in range(len(myDict)+2, turns+1):
        chosenNum = myDict[lastSpoken][1] - myDict[lastSpoken][0]
        lastSpoken = chosenNum
        if chosenNum in myDict.keys():
            myDict[chosenNum][0] = myDict[chosenNum][1]
            myDict[chosenNum][1] = i
        else:
            myDict[chosenNum] = [i, i]
    print(chosenNum)

        

input = [1, 20, 8, 12, 0, 14]
input_ex = [0, 3, 6]
myDict = {}
lastSpoken  = 0

initializeDict(input, myDict)
countingGame(myDict, 30000000, 0)