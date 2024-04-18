#include "pi.h"
#include "euler.h"
#include <stdio.h>
#include <math.h>

/**
 * main - checks my code
 *
 * Return: Always return 0
 */
int main(void)
{
	float f;

	f = (pow(EULER, PI)) + 1;
	printf("%.3f\n", f);
	return (0);
}
