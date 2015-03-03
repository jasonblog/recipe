/*
 * warning: ‘testdata’ is used uninitialized in this function
 *
 * result: test() has a uninitalized variable testdata. The value of testdata
 *         might vary at runtime with the definition VARCTRL. Please note the
 *         testcase is too simple and it will be optimized at higher optimize
 *         level.
 */

#include <stdio.h>

#define VARCTRL 45

int dummy[128];

int dirty_stack(int seed)
{
    int test[128];
    int i, max;

    max = seed % 128;
    for(i = 0; i < seed; i ++)
        test[seed] = seed;

    for(i = 0; i < 128; i ++)
        dummy[i] = test[i];

    return test[100];
}

int
main(int argc, char **argv)
{
    dirty_stack(VARCTRL);
    test();
    return 0;
}
