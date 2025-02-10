# Info + Input
inputLocation = input("Please insert your txt input location: ")
    # C:\Users\loubek\Desktop\input.txt
file = open(inputLocation, "r")
fileString = file.read()
fileSplitInputs = fileString.splitlines()
listRules = fileSplitInputs[:fileSplitInputs.index('')]
listUpdates = fileSplitInputs[fileSplitInputs.index('')+1:]

# Vars
resultPart1 = 0
resultPart2 = 0
ruleValid = True
listInvalidUpdates = []
ruleApplied = True

# Part 1
for upd in listUpdates:
    updList = upd.split(",")
    ruleValid = True
    for index in range(len(updList)):
        for rule in listRules:
            ruleList = rule.split("|")
            if ruleList[0] == updList[index]:
                if ruleList[1] in updList[:index]:
                    ruleValid = False
    if ruleValid:
        resultPart1 += int(updList[len(updList)//2])

# Part 2
    else:
        listInvalidUpdates.append(upd)

for upd in listInvalidUpdates:
    updList = upd.split(",")
    while ruleApplied:
        ruleApplied = False
        for index in range(len(updList)):
            for rule in listRules:
                ruleList = rule.split("|")
                if ruleList[0] == updList[index]:
                    if ruleList[1] in updList[:index]:
                        foundUpdValueIndex = updList.index(ruleList[1])
                        updList.pop(foundUpdValueIndex)
                        updList.insert(index,ruleList[1])
                        ruleApplied = True
    resultPart2 += int(updList[len(updList)//2])
    ruleApplied = True



# Finish
print("Result for part 1 is " + str(resultPart1))
print("Result for part 2 is " + str(resultPart2))