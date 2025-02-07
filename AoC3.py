# Modules
import re

# Vars
listMulsPart1 = []  # extracted muls from input
listResultsPart1 = []   # multiplied all muls
finalResultPart1 = ""   # all muls added up
Part1RegexFind = r'mul\((\d{1,3}),(\d{1,3})\)'

# Info + Input
inputLocation = input("Please insert your txt input location: ")
    # C:\Users\loubek\Desktop\input.txt
file = open(inputLocation, "r")
fileString = file.read()

# Part 1
listMulsPart1 = re.findall(Part1RegexFind, fileString)
for i in listMulsPart1:
    listResultsPart1.append(int(i[0])*int(i[1]))
finalResultPart1 = sum(listResultsPart1)

# Part 2

# Finish
print("Result for part 1 is " + str(finalResultPart1))