#include <stdio.h>

void test(void);

void real_test(void)
{
    printf("real function\n");
}

extern __typeof__ (test) test __attribute__ ((alias ("real_test")));

