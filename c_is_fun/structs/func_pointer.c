#include <stdio.h>

void func(int a)
{
	printf("Value of a = %d\n", a);
}

int main()
{
	void (*func_ptr)(int) = func;
	func_ptr(10);

	return (0);
}
