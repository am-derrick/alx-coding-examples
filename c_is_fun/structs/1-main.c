#include <stdio.h>
#include "car.h"

/**
 * main - main code
 *
 *
 * Return: Always 0
 */
int main(void)
{
	struct car my_car;

	my_car.name = "Mercedes";
	my_car.class = "C";
	my_car.number = 200;
	
        printf("My cool car is a %s %s %d, awesome right?\n", my_car.name, my_car.class, my_car.number);
	return (0);
}
