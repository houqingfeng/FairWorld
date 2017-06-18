__author__ = 'houqingfeng'
import sqlite3

class SQL:
    sql = None
    cursor = None

    def open(self):
        self.sql = sqlite3.connect('Rush.db')
        if not self.sql:
            print("Open Database failed")
            return
        self.cursor = self.sql.cursor()
        self.cursor.execute('create TABLE IF NOT EXISTS RawData(win FLOAT, balance FLOAT, lose FLOAT, outcome INT)')

    def insert(self, win, balance, lose, outcome, length):
        if not self.cursor:
            return

        for i in range(length):
            # commond = 'insert INTO RawData(win, balance, lose, outcome) VALUES ({0},{1},{2},{3})'.format(win[i], balance[i], lose[i], outcome[i])
            # print(commond)
            self.cursor.execute('insert INTO RawData(win, balance, lose, outcome) VALUES ({0},{1},{2},{3})'.format(win[i], balance[i], lose[i], outcome[i]))

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.sql:
            self.sql.commit()

def main():
    sql = SQL()
    sql.open()
    sql.insert([1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1, 1], 2)
    sql.close()

if __name__ == '__main__':
    main()