#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	FILE *stream;
	char *lineptr = NULL;
	size_t n = 0;
	ssize_t lines_read;

	if (argc != 2) {
		fprintf(stderr, "Error: %s\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	stream = fopen(argv[1], "r");
	if (stream == NULL) {
		perror("fopen");
		exit(EXIT_FAILURE);
	}

	while ((lines_read = getline(&lineptr, &n, stream)) != -1)
	{
		printf("We've read the length of %lu\n", lines_read);
		fwrite(lineptr, n, 1, stdout);
	}

	free(lineptr);
	fclose(stream);
	exit(EXIT_SUCCESS);
}
