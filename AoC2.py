# Info
print("Please insert your full puzzle input:")

# Vars
list = []
resultPart1 = 0
resultPart2 = 0
listAscending = True
minVar = 1
maxVar = 3
emptyInput = False

# Main - the 2 parts could be together and work simultaneously, but I like them separated here.
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

        # Part 1
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
        
        # Part 2
        problemDampener = False
        for i in range(len(list)-1):
            if listAscending:
                if list[i] < list[i+1] and list[i]+maxVar >= list[i+1]:
                    if i+1 == len(list)-1:
                        resultPart2+=1
                    continue
                elif problemDampener == False:
                    try: 
                        list[i+2]
                    except:
                        resultPart2+=1
                        break
                    else:
                        if list[i] < list[i+2] and list[i]+maxVar >= list[i+2]:
                            i+=1
                            problemDampener == True
                            continue
                else:
                    break
            else:
                if list[i] > list[i+1] and list[i]-maxVar <= list[i+1]:
                    if i+1 == len(list)-1:
                        resultPart2+=1
                    continue
                elif problemDampener == False:
                    try: 
                        list[i+2]
                    except:
                        resultPart2+=1
                        break
                    else:
                        if list[i] > list[i+2] and list[i]-maxVar <= list[i+2]:
                            i+=1
                            problemDampener == True
                            continue
                else:
                    break

    # Finish
    else:
        print("Result for part 1 is " + str(resultPart1))
        print("Result for part 2 is " + str(resultPart2))
        emptyInput == True
        break