#!/usr/bin/env python3
# 2/11/2020
# PROJECT EULER 
# https://projecteuler.net/problem=28


# Create a unique blank matrix
matrix = [["x" for i in range(5)] for j in range(5)]

print("- START -")
for row in matrix:
        print(row)

# width = 1001
# number = width * width
width = 5
number = width * width

horizontalIndexRight = 0
horizontalIndexLeft = width
verticalIndexLeft = 0
verticalIndexRight = width

center = width - int(width / 2)
numbersToSum = []

#Populate the Spiral Matrix
while horizontalIndexRight < horizontalIndexLeft:
    # print("Index Right: " + str(horizontalIndexRight))
    # print("Index Left: " + str(horizontalIndexLeft))
    
    print("- Left -")
    topRightFilled = False
    for a in range(horizontalIndexRight, horizontalIndexRight + 1):
        for b in reversed(range(0, width)):
            #print("[" + str(a) + ", " + str(b) + "]")
            if matrix[a][b] == "x":
                #top corner right number
                if topRightFilled == False:
                    topRightFilled = True
                    numbersToSum.append(number)
                #top corner left number
                if (b - 1) == 0 and matrix[a][b-1] == "x":
                    numbersToSum.append(number-1)
                elif b != 0 and matrix[a][b-1] != "x":
                    numbersToSum.append(number)
                matrix[a][b] = number
                number -= 1

    for row in matrix:
        print(row)

    #Break from spiraling early if the center of the matrix is populated
    if matrix[center][center] != "x":
        print("- Spiral Matrix Populated -")
        break
 
    print("- Down -")
    for a in range(0, width):
        #print("[" + str(a) + ", " + str(verticalIndexRight-1) + "]")
        if matrix[a][verticalIndexLeft] == "x":
            #BOTTOM LEFT FIRST
            #if verticalIndexLeft + 1 != width and matrix[a][verticalIndexLeft + 1] != "x"
            #BOTTOM LEFT NEXT
            matrix[a][verticalIndexLeft] = number
            number -= 1
    verticalIndexLeft += 1

    for row in matrix:
      print(row)

    if (horizontalIndexRight+1) != horizontalIndexLeft:
        bottomLeftFilled = False
        print("- Right -")
        for a in range(horizontalIndexLeft - 1, horizontalIndexLeft):
            for b in range(0, width):
                #print("[" + str(a) + ", " + str(b) + "]")
                if matrix[a][b] == "x":
                    #BOTTOM RIGHT FIRST
                    #BOTTOM RIGHT NEXT
                    matrix[a][b] = number
                    number -= 1

        for row in matrix:
            print(row)

    print("- Up -")
    for a in reversed(range(0, width)):
        #print("[" + str(a) + ", " + str(verticalIndexLeft) + "]")
        if matrix[a][verticalIndexRight-1] == "x":
            matrix[a][verticalIndexRight-1] = number
            number -= 1
    verticalIndexRight -= 1

    for row in matrix:
      print(row)   

    horizontalIndexRight += 1
    horizontalIndexLeft -= 1

print("Numbers to Sum: ")
print(list(dict.fromkeys(numbersToSum)))
    

