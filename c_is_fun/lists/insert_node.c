#include "header.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node in a linked list at a given position
 * @head: double pointer to the list
 * @pos: position to insert the node
 * @n: integer to insert
 *
 * Return: pointer
 */
listint_t *insert_node(listint_t **head, unsigned int pos, int n)
{
	unsigned int i;
	listint_t *current, *new;

	if (head == NULL)
		return (NULL);

	if (pos != 0)
	{
		current = *head;
		for (i = 0; i < pos - 1 && current != NULL; i++)
		{
			current = current->next;
		}
		if (current == NULL)
			return (NULL);
	}

	new = malloc(sizeof(listint_t));
	if (new = NULL)
		return (NULL);
	new->n = n;

	if (pos == 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
