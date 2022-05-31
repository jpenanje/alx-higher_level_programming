#include "lists.h"

/**
 * check_cycle - check if list has a cycle in it
 * @list: type listint_t
 * Return: 1 if there is a cycle, 0 otherwis
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list, *second = list;

	while (first != NULL && second != NULL && second->next != NULL)
	{
		first = first->next;
		second = second->next->next;
		if (second == first)
			return (1);
	}
	return (0);
}
