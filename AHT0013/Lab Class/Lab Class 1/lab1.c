#include <stdio.h>

int main() {
    int arr[10];
    int i;

    arr[0] = 1;
    arr[1] = 1;
    arr[2] = 2;
    for (i = 3; i < 10; i++) {
        arr[i] = i;
    }

    printf("Elements in array are: ");
    for (i = 0; i <10; i++) {
        printf("%d ",arr[i]);
    }

    return 0;
}