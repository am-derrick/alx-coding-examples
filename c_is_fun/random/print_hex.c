#include "main.h"
#include <stdio.h>

/**
 * print_hxdc - prints hexadecimal conversion of integer
 * @n: unsigned integer
 * @c: selector for uppercase or lowercase scenario
 * Return: length of hexadecimal number printed
 */

int print_hxdc(unsigned int n, unsigned int a)
{
	unsigned int array[11];
	unsigned int i;

	while (n)
	{
		array[i] = n % 16;
		n /= 16;
		printf("%u", array[i]);
		i++;
	}
	i--;

	for (; i >= 0; i--)
	{
		if (array[i] > 9 && a == 0)
		{
			_putchar((array[i] -10) + 97);
			continue;
		}
		else if (array[i] > 9 && a == 1)
		{
			_putchar((array[i] -10) + 65);
			continue;
		}
		_putchar(array[i] + '0');
	}
	_putchar('\n');
}

/**
 * print_hex - prints unsigned int in lowercase hex notation
 * @args: unsigned int to print
 * Return: number of digits printed
 *
**
int print_hex(va_list args)
{
	return (print_hxdc(va_arg(args, unsigned int), 0));
}

*
 * print_HEX - prints an unsigned int in uppercase hex notation
 * @args: unsigned int to print
 * Return: number of digits printed
 *
**
int print_HEX(va_list args)
{
	return (print_hxdc(va_arg(args, unsigned int), 1));
}
II*/
