#include "header.h"
#include <stdio.h>

/**
 * main - main
 *
 * Return: Always 0
 */
int main(void)
{
	unsigned int n;

	n = binary_to_int("56");
	printf("%u\n", n);
	n = binary_to_int("101");
        printf("%u\n", n);
	n = binary_to_int("10001101");
        printf("%u\n", n);
	return (0);
}
