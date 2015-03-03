#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/module.h>
#include <linux/version.h>

MODULE_DESCRIPTION("hello module!!");
MODULE_AUTHOR("Viller Hsiao <villerhsiao@gmail.com>");
MODULE_LICENSE("GPL");

static int __init test_init(void)
{
    printk("hello module!\n");

    return 0;
}

static void __exit test_exit(void)
{
    printk(KERN_INFO "Goodbye test 1\n");
}

module_init(test_init);
module_exit(test_exit);
