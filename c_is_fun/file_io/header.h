#ifndef _HEADER_H_
#define _HEADER_H_

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int _putchar(char c);
ssize_t read_write(const char *file, size_t num);

#endif /* _HEADER_H_ */
