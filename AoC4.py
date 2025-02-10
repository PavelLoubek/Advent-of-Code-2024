# Info + Input
inputLocation = input("Please insert your txt input location: ")
    # C:\Users\loubek\Desktop\input.txt
file = open(inputLocation, "r")
fileString = file.read()
file2DArray = fileString.splitlines()

# Vars
resultPart1 = 0

# Function
def CheckCoordLetter(coordRow, coordCol, letter):
    try:
        if file2DArray[coordRow][coordCol] == letter:
            if coordRow >= 0 and coordCol >= 0:
                return True
            else:
                return False
        else:
            return False
    except:
        return False

# Part 1
for row in range(len(file2DArray)):
    for col in range(len(file2DArray[row])):
        if file2DArray[row][col] == "X":
            # Top left
            if (CheckCoordLetter(row-1,col-1,"M") and CheckCoordLetter(row-2,col-2,"A") and CheckCoordLetter(row-3,col-3,"S")):
                resultPart1+=1
            # Top middle
            if CheckCoordLetter(row-1,col,"M") and CheckCoordLetter(row-2,col,"A") and CheckCoordLetter(row-3,col,"S"):
                resultPart1+=1
            # Top right
            if CheckCoordLetter(row-1,col+1,"M") and CheckCoordLetter(row-2,col+2,"A") and CheckCoordLetter(row-3,col+3,"S"):
                resultPart1+=1
            # Middle left
            if CheckCoordLetter(row,col-1,"M") and CheckCoordLetter(row,col-2,"A") and CheckCoordLetter(row,col-3,"S"):
                resultPart1+=1
            # Middle right
            if CheckCoordLetter(row,col+1,"M") and CheckCoordLetter(row,col+2,"A") and CheckCoordLetter(row,col+3,"S"):
                resultPart1+=1
            # Bottom left
            if CheckCoordLetter(row+1,col-1,"M") and CheckCoordLetter(row+2,col-2,"A") and CheckCoordLetter(row+3,col-3,"S"):
                resultPart1+=1
            # Bottom middle
            if CheckCoordLetter(row+1,col,"M") and CheckCoordLetter(row+2,col,"A") and CheckCoordLetter(row+3,col,"S"):
                resultPart1+=1
            # Bottom right
            if CheckCoordLetter(row+1,col+1,"M") and CheckCoordLetter(row+2,col+2,"A") and CheckCoordLetter(row+3,col+3,"S"):
                resultPart1+=1

# Part 2

# Finish
print("Result for part 1 is " + str(resultPart1))