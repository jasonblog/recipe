#!/usr/bin/env python
import gdb

class printHelloWorld(gdb.Command):
    """
    Example to print message
    """

    def __init__(self):
        gdb.Command.__init__(self, "printhw", gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, True)

    def invoke(self, arg, from_tty):
        print "hello world"


printHelloWorld()
