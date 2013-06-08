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

class testArgs2(gdb.Command):
    """
    Example of parsing and manipulate arguments
    """

    def __init__(self):
        gdb.Command.__init__(self, "pyaddargs", gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, True)

    def invoke(self, arg, from_tty):
        args = gdb.string_to_argv(arg)
        val0 = gdb.parse_and_eval(args[0])
        val1 = gdb.parse_and_eval(args[1])
        print "arg1 + arg2 =  %d"%(val0 + val1)


testArgs()
testArgs2()
