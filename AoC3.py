# Modules
import re

# Vars
listMulsPart1 = []  # extracted muls from input
listResultsPart1 = []   # multiplied all muls
finalResultPart1 = ""   # all muls added up
Part1RegexFind = r'mul\((\d{1,3}),(\d{1,3})\)'

Part2RegexFindAll = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
Part2RegexFindMul = r'mul\((\d{1,3}),(\d{1,3})\)'
mulEnabled = True
listInputsPart2 = []  # extracted muls, do's and don'ts from input
listResultsPart2 = []   # multiplied all filtered muls
finalResultPart2 = ""   # all filtered muls added up



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
listInputsPart2 = re.findall(Part2RegexFindAll, fileString)
for i in listInputsPart2:
    if i == "do()":
        mulEnabled = True
    elif i == "don't()":
        mulEnabled = False
    else:
        if mulEnabled:
            mul = re.match(Part2RegexFindMul,i)
            listResultsPart2.append(int(mul.group(1))*int(mul.group(2)))
finalResultPart2 = sum(listResultsPart2)

# Finish
print("Result for part 1 is " + str(finalResultPart1))
print("Result for part 2 is " + str(finalResultPart2))