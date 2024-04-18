#include <stdio.h>

int main()
{
	int a[4][2] = { {0,3}, {1,2}, {4,5}, {6,7} };
	int i, j;

	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("a[%d][%d] = [%d]\n", i,j, a[i][j]);
		}
	}
	return (0);
}
