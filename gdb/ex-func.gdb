#
# example of function, arguments and document
#


define foo
	set var $a = $arg0
	set var $b = $arg1
	echo \n
	printf "	Hello World=%d,%d\n", $a, $b 
end

# use 'help foo' in gdb to show the document
document foo
	example of function, arguments and echo
end

echo \nfoo's helper information is:\n
help foo

echo \nExecution result of \"foo 5 10\" is:
foo 5 10
