#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list
 * @head: Pointer to the head of the list to reverse
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL;
listint_t *current = head;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *second_half = NULL;
listint_t *first_half = *head;
listint_t *temp = NULL;
int is_pal = 1;

if (*head == NULL || (*head)->next == NULL)
return (1);

/* Find the middle node using fast and slow pointers */
while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
}

/* Reverse the second half of the list */
second_half = reverse_list(slow);
temp = second_half; /* Keep reference to restore later */

/* Compare the first half and reversed second half */
while (second_half != NULL)
{
if (first_half->n != second_half->n)
{
is_pal = 0;
break;
}
first_half = first_half->next;
second_half = second_half->next;
}

/* Restore the list to its original state */
reverse_list(temp);

return (is_pal);
}
