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
	printf("When you add the two, you get %d\n", a+b);
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
	printf("When you subtract the two, you get %d\n", a-b);
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
	printf("When you multiply the two, you get %d\n", a*b);
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
	printf("When you divide the two, yhou get %d\n", a/b);
}

/**
 * main - main code
 *
 * Return: 0 always
 */
int main()
{
	void (*func_ptr[])(int, int) = {add, minus, multiply, divide};
	unsigned int operation;
	int a, b;

	printf("Hey, input your first integer:\n");
	scanf("%d", &a);
	printf("Choose your operation: 0 for +, 1 for -, 2 for x, 3 for /\n");
	scanf("%d", &operation);
	printf("Great, input your second integer:\n");
	scanf("%d", &b);

	if (operation > 3)
	{
		return 0;
	}
	
	(*func_ptr[operation])(a,b);

	return 0;
}
