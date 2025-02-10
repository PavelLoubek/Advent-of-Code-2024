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

# Finish
print("Result for part 1 is " + str(resultPart1))
print("Result for part 2 is " + str(resultPart2))