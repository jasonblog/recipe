#include <stdio.h>

void __attribute__ ((weak)) test(void)
{
    printf("weak one\n");
}

int
main(int argc, void **argv)
{
    test();
    printf("hello world\n");
    return 0;
}
