# Info + Input
inputLocation = input("Please insert your txt input location: ")
    # C:\Users\loubek\Desktop\input.txt
file = open(inputLocation, "r")
fileString = file.read()
file2DArray = fileString.splitlines()
file2DArray = [list(row) for row in file2DArray] # Converts each string into its own chars

# Vars
resultPart1 = 0
outOfMap = False
guardPosition = [0,0]
resultPart2 = 0
orientation = 0

# Function
def CheckCoord(coordRow, coordCol, orient):
    global guardPosition
    global orientation
    global outOfMap
    nextPosition = OrientationReturnMove(coordRow, coordCol, orient)
    if nextPosition[0] >= 0 and nextPosition[1] >= 0 and nextPosition[0] < len(file2DArray) and nextPosition[1] < len(file2DArray[coordRow]):
        if file2DArray[nextPosition[0]][nextPosition[1]] == ".":
            guardPosition = nextPosition
            file2DArray[coordRow][coordCol] = "X"
        elif file2DArray[nextPosition[0]][nextPosition[1]] == "#":
            orientation = OrientationRotate(orient)
        elif file2DArray[nextPosition[0]][nextPosition[1]] == "X":
            guardPosition = nextPosition
            file2DArray[coordRow][coordCol] = "X"
        else:
            return
    else:
        file2DArray[guardPosition[0]][guardPosition[1]] = "X"
        outOfMap = True

def OrientationRotate(orient):
    if orient == 3:
        return 0
    else:
        return orient+1
    
def OrientationReturnMove(coordRow, coordCol, orient):
    if orient == 0:
        return [coordRow-1,coordCol]
    elif orient == 1:
        return [coordRow,coordCol+1]
    elif orient == 2:
        return [coordRow+1,coordCol]
    elif orient == 3:
        return [coordRow,coordCol-1]
    else:
        return False

# Main - Guard initial location
for row in range(len(file2DArray)):
    for col in range(len(file2DArray[row])):
        if file2DArray[row][col] == "^":
            guardPosition = [row,col]
            break

# Part 1
while not outOfMap:
    CheckCoord(guardPosition[0],guardPosition[1],orientation)
# file2DArray = [''.join(row) for row in file2DArray] # Converts each char back into its own strings
resultPart1 = sum(row.count('X') for row in file2DArray)

# Finish
print("Result for part 1 is " + str(resultPart1))
print("Result for part 2 is " + str(resultPart2))