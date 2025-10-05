#include "lib/libbit.h"
#include "lib/libbus.h"
#include <stdio.h>

bit NOT(bit a){
    return !(a);
}

bit NAND(bit a, bit b){
    return NOT(a & b);
}

bit AND(bit a, bit b){
    bit ret = NAND(a,b);
    return NAND(ret, ret);
}


bit OR(bit a, bit b){
    return NAND(NAND(a,a), NAND(b,b));
}

int main(){
    bus_4 my_bus;
    my_bus[0] = 1;
    my_bus[1] = 1;
    my_bus[3] = AND(my_bus[0], my_bus[1]);
    printf("%d", my_bus[3]);   
}