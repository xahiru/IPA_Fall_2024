#include <stdio.h>
#include <stdlib.h>

struct node {
    int num;
    struct node *nextptr;
} *stnode;

void createNodeList(int n);
void displayList();
void insertAtEnd(int num);

int main() {
    int n, num;

    printf("\n\n Linked List : To create and display Singly Linked List :\n");
    printf("-------------------------------------------------------------\n");

    printf(" Input the number of nodes : ");
    scanf("%d", &n);

    createNodeList(n);

    printf("\n Data entered in the list : \n");
    displayList();

    printf("\n\n Inserting a new node at the end of the list.\n");
    printf(" Input data for the new node: ");
    scanf("%d", &num);
    insertAtEnd(num);

    printf("\n Data in the list after inserting a new node at the end: \n");
    displayList();

    return 0;
}

void createNodeList(int n) {
    struct node *fnNode, *tmp;
    int num, i;

    stnode = (struct node *)malloc(sizeof(struct node));

    if(stnode == NULL) {
        printf(" Memory cannot be allocated.");
    } else {

        printf(" Input data for node 1 : ");
        scanf("%d", &num);
        stnode->num = num;      
        stnode->nextptr = NULL;
        tmp = stnode;

        for(i = 2; i <= n; i++) {
            fnNode = (struct node *)malloc(sizeof(struct node));

            if(fnNode == NULL) {
                printf(" Memory cannot be allocated.");
                break;
            } else {
                printf(" Input data for node %d : ", i);
                scanf(" %d", &num);

                fnNode->num = num;
                fnNode->nextptr = NULL;

                tmp->nextptr = fnNode;
                tmp = tmp->nextptr;
            }
        }
    }
}

void displayList() {
    struct node *tmp;

    if(stnode == NULL) {
        printf(" List is empty.");
    } else {
        tmp = stnode;

        while(tmp != NULL) {
            printf(" Data = %d\n", tmp->num);
            tmp = tmp->nextptr;
        }
    }
}

void insertAtEnd(int num) {
    struct node *newNode, *tmp;

    newNode = (struct node *)malloc(sizeof(struct node));

    if(newNode == NULL) {
        printf(" Memory cannot be allocated.");
    } else {
        newNode->num = num;
        newNode->nextptr = NULL;

        if(stnode == NULL) {
            stnode = newNode;
        } else {
            tmp = stnode;

            while(tmp->nextptr != NULL) {
                tmp = tmp->nextptr;
            }

            tmp->nextptr = newNode;
        }
    }
}