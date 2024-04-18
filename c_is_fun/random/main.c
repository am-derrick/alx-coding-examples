#include "main.h"
#include <stdio.h>

int main()
{
        printf("Address: %p\n", &print_hxdc);
        print_hxdc(1000, 1);
        return (0);
}
