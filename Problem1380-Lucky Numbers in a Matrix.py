# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:42:15 2020

@author: MagicDi
"""
########################
# First
matrix = [[3,7,8],[9,11,13],[15,16,17]]
def luckyNumbers(matrix):
    mr = []
    mc = []
    for row in matrix:
        mr.append(max(row))
    for i in range(len(row)):
        c = [matrix[j][i] for j in range(len(matrix))]
        mc.append(max(c))
    print(mr)
    print(mc)
    res = [a for a in mc if a in mr]
    return res
luckyNumbers(matrix)


#############################
# Second
def luckyNumbers(matrix):
    res = []
    for r in range(len(matrix)):
        minr = matrix[r][0]
        ind = 0
        for c in range(1,len(matrix[0])):
            if matrix[r][c] < minr:
                minr = matrix[r][c]
                ind = c
        print('--------------',minr)
        for r1 in range(len(matrix)):
            print(matrix[r1][ind])
            if r1 == r and r1== len(matrix)-1:
                res.append(minr)
            elif r1 == r:
                pass
            elif matrix[r1][ind] > minr:
                break
            elif matrix[r1][ind] < minr and r1==len(matrix)-1:
                res.append(minr)
    return res
luckyNumbers(matrix)

#############################
# Third
def luckyNumbers(matrix):
    minr = {min(row) for row in matrix}
    maxc = {max(col) for col in zip(*matrix)} #* to unzip the data
    return list(minr & maxc)
luckyNumbers(matrix)
    
