#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime, pdb
from sgmllib import SGMLParser
from account_table import AccountTable

class Revenue(AccountTable):

    def __init__(self, stock='', duration='year'):
        AccountTable.__init__(self, 'Revenue')

        self.isTargetTbl = False
        self.idxTargetTr = 6
        self.idxItemTd = 1
        self.duration = duration
        if self.duration == 'year':
            self.parse_url ('http://jdata.yuanta.com.tw/z/zc/zch/zch_' + \
                            stock + '.djhtm')

    def start_table(self, attrs):
        if len(attrs) > 0:
            for at in attrs:
                if at[0] == 'id' and \
                   at[1] == 'oMainTable':
                       self.isTargetTbl = True

    def end_table(self):
        if self.isTargetTbl:
            self.isTargetTbl = False

    def is_target_table(self):
        return (self.isTargetTbl)

    def is_target_tr(self):
        return (self.is_target_table() and \
                self.idxTr >= self.idxTargetTr)

    def is_target_data(self):
        return (self.is_target_tr() and self.isData)

    def is_title_row(self):
        # first row is title
        if (self.idxTr == self.idxTargetTr):
            return True
        else:
            return False
    def is_date_col(self):
        # first column is date string
        return (self.idxTd == self.idxItemTd and \
                self.idxTr > self.idxTargetTr)

    def is_content(self):
        return (self.idxTd != self.idxItemTd and \
                self.idxTr > self.idxTargetTr)

    def handle_line(self, line):
        if self.is_title_row():
            return line.decode('big5').encode('utf8')
        if self.is_content():
            # remove comma in numbers and percentage symbol
            if line == '':
                return 0

            if line.find(',') >= 0:
                return int(line.replace(',', ''))

            if line.find('%') >= 0:
                return float(line.replace('%', ''))

        elif self.is_date_col():
            year, month = line.split('/')
            date = datetime.date(int(year) + 1911, int(month), 1)
            return date

        else:
            return line.decode('big5').encode('utf8')

    def get_yoy_6mon_avg(self):
        mon = self.dataTable[1][0].month
        tbl = self.dataTable

        avg = tbl[1][4] + tbl[2][4] + \
              tbl[3][4] + tbl[4][4] + \
              tbl[5][4] + tbl[6][4]

        if (mon == 7):
            avg = avg - tbl[6][4] + tbl[6][6]
        if (mon == 6):
            avg = avg - tbl[5][4] + tbl[5][6]
        if (mon == 5):
            avg = avg - tbl[4][4] + tbl[4][6]
        if (mon == 4):
            avg = avg - tbl[3][4] + tbl[3][6]
        if (mon == 3):
            avg = avg - tbl[2][4] + tbl[2][6]
        if (mon == 2):
            avg = avg - tbl[1][4] + tbl[1][6]

        return (avg / 6.0)

    def get_yoy_last_mon(self):
        mon = self.dataTable[1][0].month
        if mon == 2:
            return self.dataTable[1][6]
        else:
            return self.dataTable[1][4]

    def get_yoy_estimated(self):
        last = self.get_yoy_last_mon()
        avg6 = self.get_yoy_6mon_avg()
        return [ min (last, avg6),
                 last,
                 avg6]

    def get_last_date(self):
        return self.dataTable[1][0]

    def get_accumulated(self, date):
        accum_revenue = 0
        for dat in self.dataTable[1:-2]:
            if dat[0] == date:
                accum_revenue = dat[5]
                break

        return accum_revenue

    def get_table(self):
        # last row is comment
        return self.dataTable[0:-2]

def to_csv(data):
    return ''.join(["{0},{1},{2},{3},{4},{5},{6}\n".format (
        data[tr][0],
        data[tr][1],
        data[tr][2],
        data[tr][3],
        data[tr][4],
        data[tr][5],
        data[tr][6])
        for tr in xrange(len(data))])

def write_csv(data):
    filename = 'test.csv'
    with open(filename, 'w') as f:
        f.write(to_csv(data))

def main():
    incstat = Revenue("2330")
    dat = incstat.get_table()
    print dat
    write_csv(dat)
    yoy = incstat.get_yoy_estimated()
    print yoy[0]
    print yoy[1]
    print yoy[2]
    print incstat.get_accumulated(incstat.get_last_date())

if __name__ == "__main__":
    main()
