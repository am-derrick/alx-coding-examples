#include <stdio.h>

void change_val(int *m)
{
	*m = 402;
}

int main(void)
{
	int n;

	n = 98;
	printf("Value of n is %d\n", n);
	change_val(&n);
	printf("Value of n is %d\n", n);
	return (0);
}
