#include <stdio.h>

/**
 * add - adds two ints
 * @a: first int
 * @b: second int
 *
 * Return: void
 */
void add(int a, int b)
{
	printf("When you add you get %d\n", a + b);
}

/**
 * minus - subtracts b from a
 * @a: first int
 * @b: second int
 *
 * Return: void
 */
void minus(int a, int b)
{
        printf("When you minus you get %d\n", a - b);
}

/**
 * multiply - multiplies two ints
 * @a: first int
 * @b: second int
 *
 * Return: void
 */
void multiply(int a, int b)
{
        printf("When you multiply you get %d\n", a * b);
}

/**
 * divide - divides two ints
 * @a: first int
 * @b: second int
 *
 * Return: void
 */
void divide(int a, int b)
{
        printf("When you divide you get %d\n", a / b);
}

/**
 * main - main code on func pointers
 *
 * Return: 0 Always
 */
int main(void)
{
	void (*func_ptr[])(int, int) = {add, minus, multiply, divide};
	unsigned int op;
	int a, b;

	printf("Hey there, what's your first integer:\n");
	scanf("%d", &a);
	printf("Choose your operation: 0 to +, 1 to -, 2 to X, 3 to /\n");
	scanf("%u", &op);
	printf("Cool! choose your second integer:\n");
	scanf("%d", &b);

	if (op > 3)
	{
		return (0);
	}

	(*func_ptr[op])(a, b);

	return (0);
}

