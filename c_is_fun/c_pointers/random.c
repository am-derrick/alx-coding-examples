#include <stdio.h>

void modify(int n)
{
	n = n + 1;
	printf("Address = %d", &n);
}

int main()
{
	int n;
	n = 10;
	modify(n);
	
	printf("n = %d", n);
}


