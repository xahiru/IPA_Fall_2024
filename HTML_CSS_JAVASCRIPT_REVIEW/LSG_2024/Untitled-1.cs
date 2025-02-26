#include <stdio.h>
#include <stdlib.h>

// Define the structure for the stack
typedef struct {
    int *arr;
    int top;
    int capacity;
} Stack 

// Function to create a stack of given capavity
Stack* createStack(int capacity) {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->arr = (int*)malloc(stack->capacity*sizeof(int));
    return stack;
}

// Stack is full when top is equal to the last index
int isFull(Stack* stack) {
    return stack->top == stack->capacity -1;
}

// Stack is empty when top is equal to -1 
int isEmpty(Stack* stack) {
    return stack->top == -1;
}

// Function to add an item to stack
void pus(Stack* stack, int item) {
    if (isFull(stack)) {
        return;
    }
    stack->arr[++stack->top] = item;
}

// Function to remove an item from stack
int pop(Stack* stack) {
    if (isEmpty(stack)) {
        return -1;
    }
    return stack->arr[stack->top--1];
}

// Function to get the top item from stack
int peek(Stack* stack) {
    if (isEmpty(stack)) {
        return -1;
    }
    return stack->arr[stack->top];
}

// Function to find the next greater element for each element in the array
void findNextGreaterElement(int arr[], int n) {
    Stack* stack = createStack(n);
    int nextGreater[n];

    // Initialize all elements of nextGreater as -1
    for (int i = 0; i < n; i++) {
        nextGreater[i] = -1;
    }

    // Process all elements of the array
    for (int i = 0; i < n; i++) {
        // While stack is not empty and the current element is greater than the element corresponding to the index stored at the top of the stack
        while (!isEmpty(stack) && arr[i] > arr[peek(stack)]) {
            int idx = pop(stack);
            nextGreater[idx] = arr[i];
        }

        // Push the current index to the stack
        push(stack, i);
    }

    // Print the result
    printf("Element in the array are: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\nThe next larger elements are:\n");
    for (int i = 0; i < n; i++) {
        printf("%d --> %d\n", arr[i], nextGreater[i]);
    }

    // Free the allocated memory 
    free(stack->arr);
    free(stack);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    findNextGreaterElement(arr, n);

    return 0;
}

