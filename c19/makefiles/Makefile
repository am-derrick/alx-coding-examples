# Compiler
CC = gcc

# Compiler flags
CFLAGS = -Wall -Werror -Wextra -pedantic

# Source files
SRCS = main.c utils.c

# Object files
OBJS = $(SRCS:.c=.o)

# Target
TARGET = my_prog

# Default 
all: $(TARGET)

# Build the exe
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(TARGET) -o $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJS) $(TARGET)




