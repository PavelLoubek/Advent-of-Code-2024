# Info
print("Please insert your full puzzle input:")

# Vars
emptyInput = False
list1 = []
list2 = []
listResultsPart1 = []
listResultsPart2 = []

# List input
while(emptyInput == False):
    inputLine = input()
    if inputLine == "":
        emptyInput = True
        break
    inputsLine = inputLine.split()
    list1.append(inputsLine[0])
    list2.append(inputsLine[1])
list1.sort()
list2.sort()

# Part1
listRange = range(len(list1))
for x in listRange:
    num1 = int(list1[x])
    num2 = int(list2[x])
    if num1 > num2:
        res = num1 - num2
        listResultsPart1.append(res)
    else:
        res = num2 - num1
        listResultsPart1.append(res)
result = sum(listResultsPart1)
print("Result for part 1 is " + str(result))

# Part2
listRange = range(len(list1))
for x in listRange:
    countNum1 = int(list1[x])
    countNum2 = list2.count(list1[x])
    res = countNum1 * countNum2
    listResultsPart2.append(res)
result = sum(listResultsPart2)
print("Result for part 2 is " + str(result))