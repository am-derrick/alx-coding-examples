#include "header.h"

/**
 * binary_to_int - converts from base 2 to decimal
 * @b: points to a string of chars
 *
 * Return: converted number or 0 on failure
 */
unsigned int binary_to_int(const char *b)
{
	unsigned res = 0;

	if (!b)
		return (0);
	while (*b)
	{
		if (*b != '0' && *b != '1')
			return (0);
		res <<= 1;
		if (*b & 1)
			res += 1;
		b++;
	}
	return res;
}
