#include <stdio.h>
#include <stdlib.h>
typedef struct Node {
    int value;
    struct Node* nextNode;
} Node;
Node* createNewNode(int value) {
    Node* node = (Node*)malloc(sizeof(Node));
    if (node == NULL) {
        printf("Memory allocation failed.\n");
        exit(1);
    }
    node->value = value;
    node->nextNode = NULL;
    return node;
}
void printList(Node* headNode) {
    Node* currentNode = headNode;
    printf("Values in the linked list:\n");
    while (currentNode != NULL) {
        printf("Value = %d\n", currentNode->value);
        currentNode = currentNode->nextNode;
    }
}
int main() {
    int numberOfNodes, inputValue;
    Node* headNode = NULL;
    Node* lastNode = NULL;
    printf("Enter the number of nodes: ");
    if (scanf("%d", &numberOfNodes) != 1 || numberOfNodes <= 0) {
        printf("Invalid input. Please enter a positive integer.\n");
        return 1;
    }
    for (int i = 1; i <= numberOfNodes; i++) {
        printf("Enter data for node %d: ", i);
        if (scanf("%d", &inputValue) != 1) {
            printf("Invalid input. Please enter an integer value.\n");
            return 1;
        }
        Node* newNode = createNewNode(inputValue);
        if (headNode == NULL) {
            headNode = newNode;
        } else {
            lastNode->nextNode = newNode;
        }
        lastNode = newNode;
    }
    printList(headNode);
    lastNode = headNode;
    while (lastNode != NULL) {
        Node* nextNode = lastNode->nextNode;
        free(lastNode);
        lastNode = nextNode;
    }
    return 0;
}