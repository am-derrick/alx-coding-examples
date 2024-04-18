#include <stdio.h>
#include <stdlib.h>

struct node
{
	int data;
	struct node *leftChild;
	struct node *rightChild;
};
struct node *root = NULL;

void insert(int data)
{
	struct node *tmpNode = (struct node*) malloc(sizeof(struct node));
	struct node *current;
	struct node *parent;
	tmpNode->data = data;
	tmpNode->leftChild = NULL;
	tmpNode->rightChild = NULL;

	if (root == NULL)
	{
		root = tmpNode;
	}
	else
	{
		current = root;
		parent = NULL;
		while(1) {
			parent = current;

			if (data < parent->data)
			{
				current = current->leftChild;

				if (current == NULL)
				{
					parent->leftChild = tmpNode;
					return;
				}
			}
			else
			{
				current = current->rightChild;

				if (current == NULL)
				{
					parent->rightChild - tmpNode;
					return;
				}
			}
		}
	}
}


void pre_ord_trav(struct node* root)
{
	if (root != NULL)
	{
		printf("%d ", root->data);
		pre_ord_trav(root->leftChild);
		pre_ord_trav(root->rightChild);
	}
}

void inorder
