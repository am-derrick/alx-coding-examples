/**
 * struct listint_s - singly linked list
 * @val: integer value
 * @nxt: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s {
    int val;
    struct listint_s* nxt;
}listint_t;
