# Info
print("Please insert your full puzzle input:")

# Vars
list = []
resultPart1 = 0
resultPart2 = 0
listAscending = True
listEquals = False
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
            listEquals = True

        # Part 1
        for i in range(len(list)-1):
            if listEquals:
                break
            elif listAscending:
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
        
        # Part 2 - a very bad for range happened, not used to Python and how it works, but keeping the workaround
        problemDampener = False
        ascendingCount = 0
        descendingCount = 0

        if listEquals:
            list.remove(list[0])
            problemDampener = True
            listEquals = False
        if list[0]+maxVar <= list[1] or list[0]-maxVar >= list[1]:
            list.remove(list[0])
            problemDampener = True
        # This one is painful but I'm too deep in my thoughts to care
        for j in range(len(list)-1):
            if list[j] < list[j+1]:
                ascendingCount+=1
            elif list[j] > list[j+1]:
                descendingCount+=1
            else:
                continue
        if ascendingCount > descendingCount and descendingCount < 2:
            listAscending = True
        elif descendingCount > ascendingCount and ascendingCount < 2:
            listAscending = False
        else:
            continue
        for i in range(len(list)-1):
            index = i
            if problemDampener:
                index+=1
                try: 
                    list[index+1]
                except:
                    resultPart2+=1
                    break
            # print (index,list[index],list[index+1])
            if listAscending:
                if list[index] < list[index+1] and list[index]+maxVar >= list[index+1]:
                    if index+1 >= len(list)-1:
                        resultPart2+=1
                        break
                    continue
                elif problemDampener == False:
                    try: 
                        list[index+2]
                    except:
                        resultPart2+=1
                        break
                    else:
                        if list[index] < list[index+2] and list[index]+maxVar >= list[index+2]:
                            # index+=1
                            problemDampener = True
                            continue
                        else:
                            break
                else:
                    break
            else:
                if list[index] > list[index+1] and list[index]-maxVar <= list[index+1]:
                    if index+1 >= len(list)-1:
                        resultPart2+=1
                        break
                    continue
                elif problemDampener == False:
                    try: 
                        list[index+2]
                    except:
                        resultPart2+=1
                        break
                    else:
                        if list[index] > list[index+2] and list[index]-maxVar <= list[index+2]:
                            # index+=1
                            problemDampener = True
                            continue
                        else:
                            break
                else:
                    break

    # Finish
    else:
        print("Result for part 1 is " + str(resultPart1))
        print("Result for part 2 is " + str(resultPart2))
        emptyInput == True
        break