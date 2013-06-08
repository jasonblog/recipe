set height 0
file gcc_dry2

python execfile("./ex-args.py")

echo \n
pyshowargs when gdb meet python "data is 0xdeadbeef"
