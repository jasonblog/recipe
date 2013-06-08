#!/usr/bin/env python
import gdb

class testArgs(gdb.Command):
    """
    Example of input arguments handling
    """

    def __init__(self):
        gdb.Command.__init__(self, "pyshowargs", gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, True)

    def invoke(self, arg, from_tty):
        args = gdb.string_to_argv(arg)
        print "Argument lists: %s"%(args)


testArgs()
