#ifndef _HEADER_H_
#define _HEADER_H_

#include <stddef.h>

typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_list(const listint_t *h);
listint_t *begin_node(listint_t **head, const int n);
listint_t *end_node(listint_t **head, const int n);
listint_t *insert_node(listint_t **head, unsigned int pos, int n);

#endif /* _HEADER_H_ */
