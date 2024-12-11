print("Please insert your full puzzle input:")

emptyInput = False
list1 = []
list2 = []
listResults = []
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
listRange = range(len(list1))
for x in listRange:
    num1 = int(list1[x])
    num2 = int(list2[x])
    if num1 > num2:
        res = num1 - num2
        listResults.append(res)
    else:
        res = num2 - num1
        listResults.append(res)
result = sum(listResults)
print(result)