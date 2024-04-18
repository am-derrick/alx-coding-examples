#include <stdio.h>

int main()
{
	int a[4][2] = { {1,2}, {3,6}, {7,9}, {8,5}};
	int i, j;

	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 2; j++)
		{
			printf("a[%d][%d] = %d\n", i,j,a[i][j]);
		}
	}
	return (0);
}
