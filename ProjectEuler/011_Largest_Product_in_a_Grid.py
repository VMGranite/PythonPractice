#!/usr/bin/env python3
# 2/6/2020
# PROJECT EULER 
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?
# https://projecteuler.net/problem=11

grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
        [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
        [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
        [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

def getProductOfList(list):
    sumTotal = 0
    for i in range(0, len(list)):
        if i == 0:
            sumTotal = list[i]
        else:
            sumTotal = sumTotal * list[i]
    return sumTotal

# check horizontal matches
def checkHorizontal(grid):
    print("\n-- CHECKING HORIZONTAL PRODUCTS --")
    largestProduct = 0
    rowIndex = 0
    for row in grid: 
        print("Row: " + str(rowIndex))
        rowIndex += 1
        for i in range(0, (len(row) - 3)):
            print(row[i: (i + 4)])
            sumTotal = getProductOfList(row[i: (i + 4)])
            largestProduct = sumTotal if sumTotal > largestProduct else largestProduct
    print("The largest product of horizontal groups: " + str(largestProduct))
    return(largestProduct)

# check vertical matches
def checkVertical(grid):
    print("\n-- CHECKING VERTICAL PRODUCTS --")
    rowIndex = 0
    largestProduct = 0
    sumTotal = 0
    gridLength = len(grid)
    # Get All 4 Item Vertical Lists in Column
    for i in range(0, gridLength):
        print("Column: " + str(i))
        rowIndex = 0
        # stay within bounds to have 4 elements 
        while rowIndex < (gridLength - 4):
            # get the desired 4 rows
            verticalList = []
            for row in range(rowIndex, (rowIndex + 4)):
                # get the element in each row for desired vertical list
                thisRow = grid[row]
                element = thisRow[i]
                verticalList.append(element)
                
            print(verticalList)
            sumTotal = getProductOfList(verticalList)
            largestProduct = sumTotal if sumTotal > largestProduct else largestProduct
            rowIndex += 1

    print("The largest product of vertical groups: " + str(largestProduct))
    return(largestProduct)

# check diagonals \
def checkDiagonal(grid, isForwardDiagonal):
    print("\n-- CHECKING BACKWARD DIAGONAL PRODUCTS --")
    rowIndex = 0
    largestProduct = 0
    sumTotal = 0
    gridLength = len(grid)
    for i in range(0, (gridLength - 3)):
        print("Diagonal Column: " + str(i))
        rowIndex = 0
        # stay within bounds to have 4 elements 
        while rowIndex < (gridLength - 3):
            # get the desired 4 rows
            FDList = []
            #Change starting element depending on diagonal orientation
            if isForwardDiagonal:
                itemIndex = 3
            else:
                itemIndex = 0
            for row in range(rowIndex, (rowIndex + 4)):
                # get the element in each row for desired Forward Diagonal list
                thisRow = grid[row]
                element = thisRow[i+itemIndex]
                FDList.append(element)
                #Change element indexing depending on diagonal orientation
                if isForwardDiagonal:
                    itemIndex -= 1
                else:
                    itemIndex += 1
            print(FDList)
            sumTotal = getProductOfList(FDList)
            largestProduct = sumTotal if sumTotal > largestProduct else largestProduct
            rowIndex += 1
    if isForwardDiagonal:
        print("The largest product of forward diagonal groups: " + str(largestProduct))
    else:
        print("The largest product of backward diagonal groups: " + str(largestProduct))
    return(largestProduct)

# check which product is the greatest 
def getLargestProduct(horizontal, vertical, forwardDiagonal, backwardDiagonal):
    productsList = [horizontal, vertical, forwardDiagonal, backwardDiagonal]
    productsList.sort()
    print("\n--CHECKING LARGET PRODUCT--")
    print("Largest Product is:", productsList[-1]) 
    return productsList[-1]

# The largest products of each category
horizontalProduct = checkHorizontal(grid)
verticalProduct = checkVertical(grid)
forwardDiagonalProduct = checkDiagonal(grid, True)
backwardDiagonalsProduct = checkDiagonal(grid, False)

getLargestProduct(horizontalProduct, verticalProduct, forwardDiagonalProduct, backwardDiagonalsProduct)