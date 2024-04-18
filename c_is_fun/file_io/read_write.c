#include "header.h"
#include <unistd.h>
#include <stdlib.h>

/**
 * read_write - reads a test from file
 * @file: name of the file
 * @num: number of chars to read from the file
 *
 * Return: number of chars or 0
 */
ssize_t read_write(const char *file, size_t num)
{
	char *buf = NULL;
	int fd;
	ssize_t bytes;

	if (!file || !num)
		return (0);

	buf = malloc(num + 1);
	if (!buf)
		return (0);

	fd = open(file, O_RDONLY);
	if (fd == -1)
		return (free(buf), 0);

	bytes = read(fd, buf, num);
	if (bytes == -1)
		return (free(buf), 0);

	buf[num] = '\0';
	bytes = write(STDOUT_FILENO, buf, bytes);
	if (bytes == -1)
		return (free(buf), 0);

	free(buf);
	close(fd);
	return (bytes);
}
