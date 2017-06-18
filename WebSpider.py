__author__ = 'houqingfeng'

import urllib2
import re
import Excel
import time

def oddsWebSpider(row1):
    _500url = 'http://odds.500.com/ouzhi.php?cid=293'
    _310url = 'http://www.310win.com/buy/jingcai.aspx?typeID=105&oddstype=2&date=2017-3-17'
    pattern = re.compile(r"[0-9]\.[0-9][0-9]|[0-9][0-9]\.[0-9][0-9]")
    urlfile = urllib2.urlopen(_310url)
    html = urlfile.read()
    urlfile.close()
    wordlist = re.findall(pattern, html)

    wordLocate = 4
    line = 0
    row = 0
    listOdds = []
    while wordLocate < len(wordlist) - 4:
        testList = []
        testList.append(float(wordlist.pop(wordLocate)))
        ++wordLocate
        testList.append(float(wordlist.pop(wordLocate)))
        ++wordLocate
        testList.append(float(wordlist.pop(wordLocate)))
        ++wordLocate
        print(testList)
        listOdds.append(Excel.spider(testList, line, row))
        row += 1
    Excel.outcome(listOdds, row1)

def main():
    while True:
        row = 0
        oddsWebSpider(row)
        row += 1
        time.sleep(3600)

if __name__ == '__main__':
    main()