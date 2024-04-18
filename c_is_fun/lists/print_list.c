#include "header.h"
#include <stdio.h>

/**
 * print_list - prints a linked list
 * @h: pointer to start of the linked list
 *
 * Return: number of elements
 */
size_t print_list(const listint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}
