#include <stdio.h>

int sum(int n)
{
	if (n != 0)
		return n + sum(n-1);
	else
		return n;
}

int main()
{
	int num, res;
	printf("Enter an integer: \n");
	scanf("%d", &num);

	res = sum(num);

	printf("The sum is %d\n", res);
	return 0;
}
