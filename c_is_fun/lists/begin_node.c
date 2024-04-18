#include "header.h"
#include <stdlib.h>

/**
 * begin_node - adds a new node to the beggining of a linked list
 * @head: double pointer to the linked list
 * @n: number to add
 *
 * Return: address of new node
 */
listint_t *begin_node(listint_t **head, const int n)
{
	listint_t *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
