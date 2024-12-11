# Info
print("Please insert your full puzzle input:")

# Vars
list = []
resultPart1 = []

# Part 1
# Add while to add more inputs
inputLine = input()
if inputLine != "":
    list = inputLine.split()
    if list[0] < list[1]:

    elif list[0] > list[1]:

    else:

    for i in range(len(list)-1):
        # Check first two numbers if descending or ascending
        # Then check each

else:
    print("Result for part 1 is " + str(resultPart1))