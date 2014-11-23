#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, os, pdb
from sgmllib import SGMLParser

class AccountTable(SGMLParser):

    def __init__(self, name = ''):
        SGMLParser.__init__(self)

        # data
        self.dataTable = []         # final table
        self.dataRow = []           # one row for temprarily use
        self.tdData = ''            # default data content
        self.name = name
        self.webpage = []

        # state machine
        self.idxTblCur = 0          # current idx
        self.idxTd = 0              # data in row
        self.idxTr = 0              # data in row
        self.isData = False         # data in row

    # private funtion
    def _append_row(self, row):
        self.dataTable.append(row)

    # public function
    def get_data(self):
        return self.dataTable

    def parse_url(self, url):
        # open url and read page into self.webpage
        webcode = urllib.urlopen(url)
        if webcode.code == 200:
            self.webpage = webcode.read()
            webcode.close()

        self.feed(self.webpage)
        self.close()

    def start_table(self, attrs):
            self.idxTblCur += 1

    def end_table(self):
        return

    def is_target_table(self):
        return (self.idxTblCur == 2)

    def is_target_data(self):
        return (self.isData == True)

    def start_tr(self, attrs):
        if not self.is_target_table():
            return;

        # data row
        self.idxTr += 1
        self.idxTd = 0
        self.dataRow = []
        return

    def end_tr(self):
        if not self.is_target_table():
            return;

        if self.is_target_tr():
            # recieve Row data
            self._append_row(self.dataRow)

    def start_td(self, attrs):
        if not self.is_target_table():
            return;

        if self.is_target_tr():
            self.idxTd += 1

        self.tdData = ''
        self.isData = True

    def end_td(self):
        if not self.is_target_table():
            return;

        self.dataRow.append(self.handle_line(self.tdData))
        self.isData = False

    def handle_data(self, text):
        if not self.is_target_data():
            return;

        # line = text.strip().decode('big5').encode('utf8')
        self.tdData = text.strip()

    def handle_line(self, line):
        return line

if __name__ == "__main__":
    acctab = AccountTable.__init__(self, 'Income Statement')
    acctab.parse_url ('http://jdata.yuanta.com.tw/z/zc/zcq/zcqa/zcqa_' + \
                      stock + '.djhtm')

    dat = acctab.get_data()
    print dat
