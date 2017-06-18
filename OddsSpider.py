__author__ = 'houqingfeng'

import urllib2
import re
import Excel
import time

def oddsWebSpider():
    _500url = 'http://odds.500.com/ouzhi.php?cid=293'
    _310url = 'http://www.310win.com/buy/jingcai.aspx?typeID=105&oddstype=2&date=2017-5-05'
    pattern = re.compile(r"[0-9]\.[0-9][0-9]|[0-9][0-9]\.[0-9][0-9]")
    urlfile = urllib2.urlopen(_310url)
    html = urlfile.read()
    urlfile.close()
    wordlist = re.findall(pattern, html)

    wordLocate = 4
    fp = open("test.txt", "w+")
    listOdds = []
    while wordLocate < len(wordlist) - 4:
        odds = wordlist.pop(wordLocate)
        fp.write(odds)
        fp.write("\t")
        ++wordLocate
        odds = wordlist.pop(wordLocate)
        fp.write(odds)
        fp.write("\t")
        ++wordLocate
        odds = wordlist.pop(wordLocate)
        fp.write(odds)
        fp.write("\n")
        ++wordLocate
    fp.close()

    fp = open("test.txt", "r+")
    for line in fp.readlines():
        print(line.split("\n")[0])


def main():
    oddsWebSpider()
    # while True:
    #     row = 0
    #     oddsWebSpider(row)
    #     row += 1
    #     time.sleep(3600)

if __name__ == '__main__':
    main()