#include <stdio.h>

/**
 *
 *
 */
int main(int argc, char *argv[])
{
	int n;
	printf("This was called with \"%s\".\n",argv[0]);

	if (argc > 1)
	{
		for (n = 1; n < argc; n++)
		{
			printf("argv[%d] = %s\n", n, argv[n]);
		}
	}
	else
	{
		printf("No other arguments.\n");
	}
	return (0);
}
