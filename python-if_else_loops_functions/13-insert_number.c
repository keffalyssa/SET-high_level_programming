#include <stdlib.h>
<<<<<<< HEAD
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;

	while (current->next != NULL && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
=======
   #include "lists.h"

   /**
    * insert_node - inserts a number into a sorted singly linked list
    * @head: pointer to pointer of first node of the list
    * @number: integer to insert
    *
    * Description: inserts number in ascending order
    * Return: address of the new node, or NULL if it failed
    */
   listint_t *insert_node(listint_t **head, int number)
   {
   	listint_t *new;
   	listint_t *current;

   	/* Allocate memory for new node */
   	new = malloc(sizeof(listint_t));
   	if (new == NULL)
   		return (NULL);

   	new->n = number;
   	new->next = NULL;

   	/* Case 1: Empty list or insert at head */
   	if (*head == NULL || (*head)->n >= number)
   	{
   		new->next = *head;
   		*head = new;
   		return (new);
   	}

   	/* Case 2: Insert in middle or at end */
   	current = *head;

   	while (current->next != NULL && current->next->n < number)
   		current = current->next;

   	new->next = current->next;
   	current->next = new;

   	return (new);
   }
>>>>>>> 7e817e0d7c99364e4ec66f38c0a58b902aa5789d
