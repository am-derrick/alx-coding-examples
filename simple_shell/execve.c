#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	char *newargv[] = { NULL, "hello", "c13", NULL };
	char *environ[] = { NULL };

	if (argc != 2)
	{
		fprintf(stderr, "Error: %s\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	newargv[0] = argv[1];
	execve(argv[1], newargv, environ);
	perror("execve");
	exit(EXIT_FAILURE);

}
