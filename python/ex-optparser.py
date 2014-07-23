#!/usr/bin/env python

from optparse import OptionParser

def parse_args():
    parser = OptionParser()
    parser.add_option('-a', '--arg1',
                  help='Example argument',
                  metavar='arg1')
    parser.add_option('-v', '--verbose',
                  help='Vervose level',
                  metavar='verbose')

    (options, args) = parser.parse_args()
    return options

if __name__ == '__main__':
    g_opts = parse_args()

    print g_opts
    print g_opts.verbose
    print g_opts.arg1

