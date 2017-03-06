#_.*encoding=utf8*._
from __future__ import division
from sklearn.datasets import load_iris
database = load_iris()
X = database.data
Y = database.target

x = X[:100]
y = Y[:100]
def OneRAlgo(X, Y, targetList):

    targetValue = [] #特征值
    for i in range(len(Y)):
        for j in range(len(targetValue)):
            if targetValue[j] == Y[i]:
                break
        else:
            targetValue.append(Y[i])
    targetValue = sorted(targetValue, reverse=True)

    lineNum = len(X[0])
    if len(targetValue) > lineNum:
        targetValue = targetValue[len(targetValue)-lineNum:len(targetValue)]
        targetValue = [int(x) for x in targetValue]

    dicList = [{}]*lineNum
    outcomeList = [{}] * lineNum

    for i in range(lineNum):
        dic = {}
        for raw in zip(X, Y):
            if dic.get((raw[0][i], raw[1]), None) != None:
                dic[(raw[0][i], raw[1])] += 1
            else:
                dic[(raw[0][i], raw[1])] = 1
        dicList[i] = dic


    for i in range(lineNum):
        dic = {}
        everyValueOdds = 0.0
        everyValueSum = 0.0
        maxTarget = 0.0
        for item in X:
            value = item[i]
            for target in targetValue:
                if dicList[i].get((value, target), None) != None:
                    if dic.get(value, None) != None:
                        continue
                    everyValueSum += dicList[i][(value, target)]
                    if (dicList[i][(value, target)] >= everyValueOdds):
                        maxTarget = target
                        everyValueOdds = dicList[i][(value, target)]
            else:
                if dic.get(value, None) != None:
                        continue
                dic[value] = (maxTarget, everyValueOdds, everyValueSum)
                everyValueOdds *= 0.0
                everyValueSum *= 0.0
                maxTarget *= 0.0
        else:
            outcomeList[i] = dic

    targetL = 0
    targetOdds = 0.0
    targetV =0.0
    target = 0
    success = 0
    sum1 = 0
    xList = []
    sumX = 0
    for i in range(lineNum):
       if outcomeList[i].get(targetList[i], None) != None:
           sumX += outcomeList[i][targetList[i]][1]
    for i in range(lineNum):
        if outcomeList[i].get(targetList[i], None) != None:
            xList.append(outcomeList[i][targetList[i]][1]/sumX)
        else:
            xList.append(0)

    for i in range(lineNum):
       if outcomeList[i].get(targetList[i], None) != None:
           odds = outcomeList[i][targetList[i]][1] / outcomeList[i][targetList[i]][2]
           tup = (targetList[i], outcomeList[i][targetList[i]][1], outcomeList[i][targetList[i]][2], odds)
           print("{0:.2f}, {1}, {2}, {3:.2f}%".format(tup[0], tup[1], int(tup[2]), tup[3]*100))
           print
           if targetOdds <= odds:
               targetOdds = odds
               targetL = i
               targetV = targetList[i]
               target = outcomeList[i][targetList[i]][0]
               success = outcomeList[i][targetList[i]][1]
               sum1 = outcomeList[i][targetList[i]][2]
    return (targetV, targetL, targetValue[targetL], targetOdds * 100.0, int(success), int(sum1))

def main():

    filename = r'odds1.txt'
    alist = []
    outlist = []
    lines = open(filename, 'r').readlines()
    print(len(lines))
    for line in lines:
        print(line)
        list = line.strip().split('\t')
        target_s = []
        outlist.append(float(list[-1]))
        for i in range(len(list) - 1):
            target_s.append(float(list[i]))
        alist.append(target_s)
    print(alist)
    #print OneRAlgo(alist, outlist, [2.10, 3.25, 3.25])
    # list = [line.strip().split(',') for line in lines ]#字段以逗号分隔，这里取得是第4列
    # file_object = open('odds.txt')
    # lines = file_object.readline()
    #
    # try:
    #     all_the_text = file_object.read()
    #     print(all_the_text)
    # finally:
    #     file_object.close( )

if __name__ == '__main__':
    main()