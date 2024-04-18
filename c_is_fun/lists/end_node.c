#include "header.h"
#include <stdlib.h>

/**
 * end_node - adds a new node to the end of a linked list
 * @head: double pointer to list
 * @n: integet to add
 *
 * Return: pointer
 */
listint_t *end_node(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head = NULL)
	{
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next != NULL)
	{
		current = current->next;
	}
	current->next = new;
	return (new);
}
