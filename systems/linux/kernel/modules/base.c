/*
 * Hello world module
 * 
 * This is really basic, mainly for a starting point for modules.
 * 
 * 0x4248
 */
#include <linux/kernel.h>
#include <linux/module.h>


int init_module(void)
{
    pr_info("Hello world 1.\n");
    return 0;
}


/* Exit function */
void cleanup_module(void)
{
    pr_info("Goodbye world 1.\n");
}

module_init(init_module); 
module_exit(cleanup_module); 

MODULE_LICENSE("GPL");
MODULE_AUTHOR("0x4248");
MODULE_DESCRIPTION("A hello world driver");
