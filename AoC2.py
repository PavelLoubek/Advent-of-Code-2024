# Info
print("Please insert your full puzzle input:")

# Vars
list = []
resultPart1 = 0
listAscending = True
minVar = 1
maxVar = 3
emptyInput = False

# Part 1
# Add while to add more inputs
while(emptyInput == False):
    inputLine = input()
    if inputLine != "":
        list = inputLine.split()
        list = [ int(x) for x in list ]
        if list[0] < list[1]:
            listAscending = True
        elif list[0] > list[1]:
            listAscending = False
        else:
            continue
        for i in range(len(list)-1):
            if listAscending:
                if list[i] < list[i+1] and list[i]+maxVar >= list[i+1]:
                    if i+1 == len(list)-1:
                        resultPart1+=1
                    continue
                else:
                    break
            else:
                if list[i] > list[i+1] and list[i]-maxVar <= list[i+1]:
                    if i+1 == len(list)-1:
                        resultPart1+=1
                    continue
                else:
                    break
            # Check first two numbers if descending or ascending
            # Then check each
    else:
        print("Result for part 1 is " + str(resultPart1))
        emptyInput == True
        break