/*
 * warning: ‘testdata’ is used uninitialized in this function
 *
 * result: test() has a uninitalized variable testdata. The value of testdata
 *         might vary at runtime with the definition VARCTRL. Please note the
 *         testcase is too simple and it will be optimized at higher optimize
 *         level.
 */

#include <stdio.h>


struct retval
{
  int a;
  int b;
  char c;
  int d;
}

struct retval * test(void)
{
    struct retval testdata;

    
    printf("uninitialized test data=%d\n", testdata);
}

int
main(int argc, char **argv)
{
    dirty_stack(VARCTRL);
    test();
    return 0;
}
