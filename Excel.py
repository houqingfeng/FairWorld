from __future__ import division
#encoding=utf8
__author__ = 'houqingfeng'

import  xdrlib ,sys
import xlrd
import re
import xlwt
from xlutils.copy import copy
import OneR
import KN
import os
import Sql

excelName = 'dero1.xls'
outcomeExcel = "/Users/houqingfeng/Desktop/outcome.xls"
reRule = r"\d"

firstWrite = True

beginOdds = [1.45,3.96,7.26 ]
endOdds   = [2.35, 3.20, 2.65]

#open excel workspace
def openExcel(name=""):
    try:
        workspace = xlrd.open_workbook(name)
        return workspace
    except Exception, e:
        print str(e)

#open read sheet
def open_read_excel(workSpace, index):
    if not workSpace:
        print "workSpace is None"
    try:
        rb = workSpace.sheets()[index]
        return (rb)
    except Exception, e:
        print str(e)

#open write sheet
def open_write_excel(workSpace, index):
    if not workSpace:
        print "workSpace is None"
    try:
        wb = copy(workSpace)
        ws = wb.get_sheet(index)
        return (ws, wb)
    except Exception, e:
        print(str(e))

#read sheet
def excel_read(sheet, x, y):
     return sheet.cell(x, y).value

#write sheet
def excel_write(sheet, x, y, value):
    try:
        sheet.write(x, y, value)
        #return writeBook.save(excelName)
    except Exception, e:
        print str(e)

def work():
    workSpace = openExcel(excelName)
    readSheet = open_read_excel(workSpace, 0)
    (writeSheet, writeBook) = open_write_excel(workSpace, 0)
    nrows = readSheet.nrows
    ncols = readSheet.ncols
    outlist = readSheet.col_values(6)
    pattern = re.compile(reRule)

    for index in range(len(outlist)):
         outcome = pattern.findall(outlist[index])
         if outcome[0] > outcome[1]:
             excel_write(writeSheet, index, 7, 3)
         elif outcome[0] == outcome[1]:
             excel_write(writeSheet, index, 7, 1)
         else:
             excel_write(writeSheet, index, 7, 0)
    writeBook.save(excelName)

def TestGenerator():
    workSpace = openExcel(excelName)
    readSheet = open_read_excel(workSpace, 0)
    nrows = readSheet.nrows
    ncols = readSheet.ncols
    bWinList = readSheet.col_values(3)
    bBalanceList = readSheet.col_values(4)
    bLoseList = readSheet.col_values(5)
    outcomeList = readSheet.col_values(6)
    bX = list(zip(bWinList, bBalanceList, bLoseList))
    bY = list(outcomeList)
    X = bX[:5584]
    Y = bY[:5584]
    right = 0.0
    testSum = 0
    wrong1Sum = 0
    wrong2Sum = 0
    wrong1 = 0.0
    wrong2 = 0.0
    zong = 0
    rigt = 0
    tesst1 = 0
    teeet = 0
    maxTest = 0
    minTest = 0
    midTest = 0
    rmaxTest = 0
    rminTest = 0
    rmidTest = 0
    for index1 in range(len(bX[5585:-1])):
        index = index1 + 5585
        zong += 1
        tup = OneR.OneRAlgo(bX[5585:-1], bY[5585:-1], bX[index])

        if tup[2] == bY[index]:
            tesst1 += 1
        if tup[2] == 3.0:
            teeet += 1
            testSum += 1
            if 3.0 == bY[index] or bY[index] == 1:
                right += 1
            else:
                print bX[index], sum(bX[index])
        elif tup[2] == 1.0:
            teeet += 1
            wrong1Sum += 1
            if 1.0 == bY[index]:
                wrong1 += 1
        elif tup[2] == 0.0:
            if max(bX[index][0], bX[index][1], bX[index][2]) == bX[index][2]:
                maxTest += 1
            elif min(bX[index][0], bX[index][1], bX[index][2]) == bX[index][2]:
                minTest += 1
            else:
                midTest += 1
            teeet += 1
            wrong2Sum += 1
            if 0.0 == bY[index]:
                wrong2 += 1
                if max(bX[index][0], bX[index][1], bX[index][2]) == bX[index][2]:
                    rmaxTest += 1
                elif min(bX[index][0], bX[index][1], bX[index][2]) == bX[index][2]:
                    rminTest += 1
                else:
                    rmidTest += 1

        if min(bX[index][0], bX[index][1], bX[index][2]) == bX[index][0] and tup[2] == 3:
            rigt += 1
        if min(bX[index][0], bX[index][1], bX[index][2]) == bX[index][1] and tup[2] == 1:
            rigt += 1
        if min(bX[index][0], bX[index][1], bX[index][2]) == bX[index][2] and tup[2] == 0:
            rigt += 1

    if testSum != 0:
        print ("3 prediction's percentage is {0:.3f}%".format(right/testSum * 100.0))
    if wrong1Sum != 0:
        print ("1 prediction's percentage is {0:.3f}%".format(wrong1/wrong1Sum * 100.0))
    if wrong2Sum != 0:
        print ("0 prediction's percentage is {0:.3f}%".format(wrong2/wrong2Sum * 100.0))

    print(tesst1 , testSum + wrong1Sum + wrong2Sum, right + wrong1 + wrong2)
    print testSum, wrong1Sum, wrong2Sum
    # print((rigt) /(zong))
    print(tesst1 / zong)
    print(teeet)

    print
    print maxTest, rmaxTest
    print midTest, rmidTest
    print minTest, rminTest

    # print ("1 wrongditon's percentage is {0:.3f}%".format(wrong1/testSum * 100.0))
    # print ("0 wrongditon's percentage is {0:.3f}%".format(wrong2/testSum * 100.0))
def KNTestGenerator():
    workSpace = openExcel(excelName)
    readSheet = open_read_excel(workSpace, 0)
    nrows = readSheet.nrows
    ncols = readSheet.ncols
    bWinList = readSheet.col_values(3)
    bBalanceList = readSheet.col_values(4)
    bLoseList = readSheet.col_values(5)
    outcomeList = readSheet.col_values(6)
    bX = list(zip(bWinList, bBalanceList, bLoseList))
    bY = list(outcomeList)
    X = bX[:4500]
    Y = bY[:4500]
    testlist = bX[4501:-1]
    for item in testlist:
        tupleT = KN.K_N_Algorithem(X, Y, item)
        print(tupleT[:5])

def predictWork(m=4990):
    workSpace = openExcel(excelName)
    readSheet = open_read_excel(workSpace, 0)
    nrows = readSheet.nrows
    ncols = readSheet.ncols
    bWinList = readSheet.col_values(3)
    bBalanceList = readSheet.col_values(4)
    bLoseList = readSheet.col_values(5)
    outcomeList = readSheet.col_values(6)
    bX = list(zip(bWinList, bBalanceList, bLoseList))
    bY = list(outcomeList)
    X = bX[:m]
    Y = bY[:m]
    # print(X)
    # print(Y)
    test = raw_input("enter: ")
    beginOdds = test.split("\t")
    beginOdds = map(lambda x: float(x), beginOdds)
    print beginOdds, sum(beginOdds)
    workSpace = openExcel(excelName)


#4	3.35	1.75	3.65	3.35	1.83
    print("*" * 40)
    print
    tup = OneR.OneRAlgo(bX[:-1], bY[:-1], (beginOdds))
    print("{0:.2f}, {1}, {2}, {3:.2f}%, {4}, {5}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5]))
    print("*"*40)

    print beginOdds, sum(beginOdds)
    print
    tup = OneR.OneRAlgo(bX[:m-1000], bY[:m-1000], (beginOdds))
    print("{0:.2f}, {1}, {2}, {3:.2f}%, {4}, {5}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5]))
    print("*"*40)
    print beginOdds, sum(beginOdds)
    print
    tup = OneR.OneRAlgo(bX[:m-2000], bY[:m-2000], (beginOdds))
    print("{0:.2f}, {1}, {2}, {3:.2f}%, {4}, {5}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5]))
    print("*"*40)
    print beginOdds, sum(beginOdds)
    print
    tup = OneR.OneRAlgo(bX[:m-3000], bY[:m-3000], (beginOdds))
    print("{0:.2f}, {1}, {2}, {3:.2f}%, {4}, {5}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5]))
    print("*"*40)

    # tupleT = KN.K_N_Algorithem(bX[:-1], bY[:-1], beginOdds)
    # victory = 0
    # balance = 0
    # lost = 0
    # testNumber = 50
    # for i in range(testNumber):
    #     for item in tupleT[i][1]:
    #         if item == 3.0:
    #             victory += 1
    #         elif item == 1.0:
    #             balance += 1
    #         else:
    #             lost += 1
    # print(tupleT[:testNumber])
    # print("3 : {0}, 1 : {1}, 0: {2}".format(victory, balance, lost))
    # print("*"*40)

def KNPredict(testlist=[]):
    workSpace = openExcel(excelName)
    readSheet = open_read_excel(workSpace, 0)
    nrows = readSheet.nrows
    ncols = readSheet.ncols
    bWinList = readSheet.col_values(3)
    bBalanceList = readSheet.col_values(4)
    bLoseList = readSheet.col_values(5)
    outcomeList = readSheet.col_values(6)
    bX = list(zip(bWinList, bBalanceList, bLoseList))
    bY = list(outcomeList)
    X = bX[:-1]
    Y = bY[:-1]
    tupleT = KN.K_N_Algorithem(X, Y, testlist)
    print(tupleT[:5])

def outcome(outlist=[], column=1):

    fp = open("2017.3.14.txt", "r")
    context = ""
    try:
        index = 0
        for item in fp.readlines():
            context += item.split("\n")[0] + "\t" + str(outlist[index]) + "\n"
            print(item)
            index += 1
        fp.close()
    except Exception, e:
        str(e)

    if context == "":
        for item in outlist:
            context += str(item) + "\n"
    try:
        fp = open("2017.3.14.txt", "w+")
        fp.write(context)
        fp.write()
    except Exception, e:
        str(e)

    # wb = xlwt.Workbook()
    # sheet = wb.add_sheet("yest")
    # row = 0
    # for item in outlist:
    #     sheet.write(row, column, item)
    #     row += 1
    # wb.save("test.xls")

    # workSpace = openExcel(outcomeExcel)
    # (writeSheet, writeBook) = open_write_excel(workSpace, 0)
    # excel_write(writeSheet, line, row, value)
    #writeBook.save(excelName)

def spider(testlist=[], line=0, row=0):
    workSpace = openExcel(excelName)
    readSheet = open_read_excel(workSpace, 0)
    nrows = readSheet.nrows
    ncols = readSheet.ncols

    bWinList = readSheet.col_values(3)
    bBalanceList = readSheet.col_values(4)
    bLoseList = readSheet.col_values(5)
    outcomeList = readSheet.col_values(6)
    bX = list(zip(bWinList, bBalanceList, bLoseList))
    bY = list(outcomeList)
    m=nrows
    X = bX[:m]
    Y = bY[:m]
    beginOdds = testlist


    outDic = {3: 0, 1: 0, 0: 0}
#4	3.35	1.75	3.65	3.35	1.83
    #print("*" * 40)

    tup = OneR.OneRAlgo(bX[:-1], bY[:-1], (beginOdds))
    outDic[int(tup[2])] += 1
    # print("{0:.2f}, {1}, {2}, {3:.2f}%, {4}, {5}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5]))
    # print("*"*40)

    # print beginOdds, sum(beginOdds)
    # print
    tup = OneR.OneRAlgo(bX[:m-1000], bY[:m-1000], (beginOdds))
    outDic[int(tup[2])] += 1
    # print("{0:.2f}, {1}, {2}, {3:.2f}%, {4}, {5}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5]))
    # print("*"*40)
    # print beginOdds, sum(beginOdds)
    # print
    tup = OneR.OneRAlgo(bX[:m-2000], bY[:m-2000], (beginOdds))
    outDic[int(tup[2])] += 1
    # print("{0:.2f}, {1}, {2}, {3:.2f}%, {4}, {5}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5]))
    # print("*"*40)
    # print beginOdds, sum(beginOdds)
    # print
    tup = OneR.OneRAlgo(bX[:m-3000], bY[:m-3000], (beginOdds))
    outDic[int(tup[2])] += 1
    # print("{0:.2f}, {1}, {2}, {3:.2f}%, {4}, {5}".format(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5]))
    # print("*"*40)

    value = 0
    times = 0
    for (key, value1) in outDic.items():
        if value1 >= times:
            value = key
            times = value1
    return value

def predict():
    while True:
        try:
            predictWork()
        except Exception, e:
            print(str(e))

def insertSQL():
    workSpace = openExcel(excelName)
    readSheet = open_read_excel(workSpace, 0)
    nrows = readSheet.nrows
    ncols = readSheet.ncols
    bWinList = readSheet.col_values(3)
    bBalanceList = readSheet.col_values(4)
    bLoseList = readSheet.col_values(5)
    outcomeList = readSheet.col_values(6)

    sql = Sql.SQL()
    sql.open()
    sql.insert(bWinList, bBalanceList, bLoseList, outcomeList, len(bWinList))
    sql.close()

def main():
    #work()
    #TestGenerator()
    #KNTestGenerator()
    predict()
    # insertSQL()

if __name__ == '__main__':
    main()
