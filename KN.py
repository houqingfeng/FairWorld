from __future__ import division
#_.*encoding=utf8*._
__author__ = 'houqingfeng'
import os
import math

def K_N_Algorithem(X = [], Y = [], testList = []):
    dic = {}

    for index in range(len(X)):
        distance = -1
        if (X[index][0] >= (testList[0] - 0.1) or X[index][0] <= (testList[0] + 0.1))and (X[index][1] >= (testList[1] - 0.1) or X[index][1] <= (testList[1] + 0.1)) and (X[index][2] >= (testList[2] - 0.1) or X[index][2] <= (testList[2] + 0.1)):
            distance = math.sqrt((X[index][0] - testList[0])**2
                                 + (X[index][1] - testList[1])**2
                                 + (X[index][2] - testList[2])**2)
        if distance != -1:
            if not dic.get(distance, False):
                dic[distance] = []
            dic[distance].append(Y[index])

    test = sorted(dic)
    values = []
    for item in test:
        values.append(dic.get(item))

    return zip(test, values)

def K_N(X, Y, testList):
    pass

def main():
    K_N_Algorithem([[3, 4, 5], [3, 2, 5], [1, 9, 5]], [3, 4, 5], [1, 2, 3])

if __name__ == '__main__':
    main()