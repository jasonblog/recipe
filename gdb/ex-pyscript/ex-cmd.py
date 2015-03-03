#!/usr/bin/env python
import gdb

class testCmds(gdb.Command):
    """
    Example of input arguments handling
    """

    def __init__(self):
        gdb.Command.__init__(self, "pystart", gdb.COMMAND_USER, gdb.COMPLETE_SYMBOL, True)

    def invoke(self, arg, from_tty):
        #gdb.execute('b main')
        #gdb.execute('run')
        #print "%s"%(gdb.breakpoints())

        args = gdb.string_to_argv(arg)
        print gdb.Value
        val0 = gdb.parse_and_eval(args[0])
        print gdb.Value
        val1 = gdb.parse_and_eval(args[1])
        print val0 + val1

testCmds()
