#!/usr/bin/env python

import sys
import urllib
import urllib2

def httpPost(url, value):
    data = urllib.urlencode(value)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    page = response.read()
    fname = 'response.html'

    with open(fname, 'w') as fd:
      fd.write(page)

if __name__ == '__main__':

    url='http://localhost/foo'

    values = {
             'field1' : 'test1',
             'field2' : '123456'
    };

    httpPost(url, values)

 

