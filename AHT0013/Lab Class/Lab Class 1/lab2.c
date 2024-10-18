#include <stdio.h>
#include <stdlib.h>

#define MAX 100

typedef struct {
    int elements[MAX];
    int size;
} SequentialList;

void initializeList(SequentialList *list);
void insertElement(SequentialList *list, int element);
int locateElement(SequentialList *list, int x);
int getElementAtIndex(SequentialList *list, int index);
void deleteElement(SequentialList *list, int element);
void traverselist(SequentialList *list);
int main() {
    SequentialList list;
    initializeList(&list);

    insertElement(&list, 10);
    insertElement(&list, 20);
    insertElement(&list, 30);

    traverselist(&list);
    printf("Element at index 1: %d\n", getElementAtIndex(&list, 1));
    printf("First occurrence of 20 is at index: %d\n", locateElement(&list, 20));

    deleteElement(&list, 20);
    traverselist(&list);

    return 0;
}

void initializeList(SequentialList *list) {
    list->size = 0;
}

void insertElement(SequentialList *list, int element) {
    if (list->size < MAX) {
        list->elements[list->size] = element;
        list->size++;
    } else {
        printf("List is full. Cannot insert element.\n");
    }
}

int locateElement(SequentialList *list, int x) {
    for (int i = 0; i < list->size; i++) {
        if (list->elements[i] == x) {
            return i;
        }
    }
    return -1;
}

int getElementAtIndex(SequentialList *list, int index) {
    if (index >= 0 && index < list->size) {
        return list->elements[index];
    }
    printf("Invalid index\n");
    return -1;
}

void deleteElement(SequentialList *list, int element) {
    int index = locateElement(list, element);
    if (index != -1) {
        for (int i = index; i < list->size - 1; i++) {
            list->elements[i] = list->elements[i + 1];
        }
        list->size--;
    } else {
        printf("Element not found in the list.\n");
    }
}

void traverselist(SequentialList *list) {
    printf("list elements: ");
    for (int i = 0; i < list->size; i++) {
        printf("%d ", list->elements[i]);
    }
    printf("\n");
}