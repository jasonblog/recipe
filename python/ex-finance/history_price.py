#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2, time, datetime

DATE_FMT = '%Y-%m-%d'
TIME_FMT = '%H:%M:%S'

class HistoryPrice(object):

    def __init__(self, stock, start_date, end_date=datetime.date.today().isoformat()):
        # collect variables value
        self.date,self.time,self.start,self.high,self.low,self.close,self.volume,self.adjclose = ([] for _ in range(8))
        self.stock = str(stock)
        self.start_date = start_date
        self.end_date = end_date

        try:
            # stock in listed company
            csv = urllib2.urlopen(self.get_url()).readlines()
        except urllib2.HTTPError, e:
            # try the OTC case
            try:
                csv = urllib2.urlopen(self.get_url(where = 'TWO')).readlines()
            except urllib2.HTTPError, e:
                csv = ['{0},0,0,0,0,0,0\n'.format(start_date),
                '{0},0,0,0,0,0,0\n'.format(end_date)]
        csv.reverse()
        # feed tables from csv file
        for bar in xrange(0, len(csv) - 1):
            ds, start, high, low, close, volume,adjc = csv[bar].rstrip().split(',')
            start, high, low, close, adjc = [float(x) for x in [start, high, low, close, adjc]]
            '''
            # change values to one after adjusted
            if close != adjc:
                factor = adjc/close
                start, high, low, close = [x*factor for x in [start, high, low, close]]
            '''
            dt = datetime.datetime.strptime(ds,'%Y-%m-%d')
            # change data to object content
            self.append(dt, start, high, low, close, volume, adjc)

    def get_url(self, where = 'TW'):
        start_year, start_month, start_day = self.start_date.split('-')
        start_month = str(int(start_month) - 1)
        end_year,end_month,end_day = self.end_date.split('-')
        end_month = str(int(end_month) - 1)

        url_string = 'http://ichart.finance.yahoo.com/'
        url_string += 'table.csv?s={0}.{1}'.format(self.stock, where)
        url_string += '&a={0}&b={1}&c={2}'.format(start_month, start_day, start_year)
        url_string += '&d={0}&e={1}&f={2}'.format(end_month, end_day, end_year)
        return url_string

    def append(self,dt,start,high,low,close,volume,adjclose):
        self.date.append(dt.date())
        self.time.append(dt.time())
        self.start.append(float(start))
        self.high.append(float(high))
        self.low.append(float(low))
        self.close.append(float(close))
        self.volume.append(int(volume))
        self.adjclose.append(float(adjclose))

    def get_max_adjclose(self):
        try:
            m = max(self.adjclose)
        except ValueError, e:
            print self.adjclose
            m = 0
        return m

    def get_min_adjclose(self):
        return min(self.adjclose)

    def get_max(self):
        return max(self.high)

    def get_min(self):
        return min(self.low)

if __name__ == '__main__':
    q = HistoryPrice('2330', '2000-01-01', '2001-12-31')    # download year to date Apple data
    print q.get_max_adjclose()                             # print it out
    print q.get_min_adjclose()                             # print it out

