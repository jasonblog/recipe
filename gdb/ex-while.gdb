#
# example of variable, while-loop, and stdout
#

set $a = 5
set $b = 10
while ($a <= $b)
	printf "a=%d,b=%d\n", $a, $b
	set $a = $a + 1
end
