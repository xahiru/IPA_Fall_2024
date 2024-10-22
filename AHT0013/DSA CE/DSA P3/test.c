#include <stdio.h>
#include <string.h>

#define MAXSIZE 50

struct student {
    int id;
    char name[50];
    int age;
};

struct sqlist {
    struct student elemlist[MAXSIZE];
    int size;
};

void setnull(struct sqlist *p) {
    p->size = 0;
}

int length(struct sqlist *p) {
    return p->size;
}


void get(struct sqlist *p, int i) {
    if (i < 1 || i > p->size) {
        printf("Index out of bounds\n");
    } else {
        struct student s = p->elemlist[i - 1];
        printf("Student at index %d: ID=%d, Name=%s, Age=%d\n", i, s.id, s.name, s.age);
    }
}

void locate(struct sqlist *p, int id) {
    int i = 0;
    while (i < p->size && p->elemlist[i].id != id) {
        i++;
    }
    if (i == p->size) {
        printf("Student not found\n");
    } else {
        printf("Student found at index: %d\n", i + 1);
    }
}

void insert(struct sqlist *p, int i, struct student s) {
    if (i < 1 || i > p->size + 1 || p->size >= MAXSIZE) {
        printf("Invalid position, cannot insert\n");
    } else {
        for (int j = p->size; j >= i; j--) {
            p->elemlist[j] = p->elemlist[j - 1];
        }
        p->elemlist[i - 1] = s;
        p->size++;
        printf("Student inserted: ID=%d, Name=%s, Age=%d\n", s.id, s.name, s.age);
    }
}

void delete(struct sqlist *p, int i) {
    if (i < 1 || i > p->size) {
        printf("Index out of bounds\n");
    } else {
        for (int j = i - 1; j < p->size - 1; j++) {
            p->elemlist[j] = p->elemlist[j + 1];
        }
        p->size--;
        printf("Student deleted at index %d.\n", i);
    }
}

void display(struct sqlist *p) {
    if (p->size == 0) {
        printf("The list is empty\n");
    } else {
        printf("The list of students:\n");
        for (int j = 0; j < p->size; j++) {
            struct student s = p->elemlist[j];
            printf("ID=%d, Name=%s, Age=%d\n", s.id, s.name, s.age);
        }
    }
}

void search_by_name(struct sqlist *p, char name[]) {
    int i = 0;
    while (i < p->size && strcmp(p->elemlist[i].name, name) != 0) {
        i++;
    }
    if (i == p->size) {
        printf("Student not found\n");
    } else {
        printf("Student found at index: %d\n", i + 1);
        struct student s = p->elemlist[i];
        printf("ID=%d, Name=%s, Age=%d\n", s.id, s.name, s.age);
    }
}

void update_student(struct sqlist *p, int id) {
    int i = 0;
    while (i < p->size && p->elemlist[i].id != id) {
        i++;
    }
    if (i == p->size) {
        printf("Student not found\n");
    } else {
        printf("Enter new Name and Age for student ID %d: ", id);
        scanf("%s %d", p->elemlist[i].name, &p->elemlist[i].age);
        printf("Student updated: ID=%d, Name=%s, Age=%d\n", p->elemlist[i].id, p->elemlist[i].name, p->elemlist[i].age);
    }
}

int main() {
    struct sqlist l;
    setnull(&l);

    struct student s1 = {33120013, "Tuhin", 23};
    struct student s2 = {33120014, "Rabbi", 24};
    struct student s3 = {33120015, "Shimanto", 22};
    struct student s4 = {33120016, "Nuhash", 26};

    insert(&l, 1, s1);
    insert(&l, 2, s2);
    insert(&l, 3, s3);
    insert(&l, 4, s4);

    display(&l);

    int select, i, id;
    char name[50];
    struct student s;

    do {
        printf("\nMenu:\n");
        printf("1: Clear the list\n");
        printf("2: Display the length\n");
        printf("3: Get a student by index\n");
        printf("4: Locate a student by ID\n");
        printf("5: Insert a student\n");
        printf("6: Delete a student\n");
        printf("7: Display the list\n");
        printf("8: Search for a student by name\n");
        printf("9: Update a student's details\n");
        printf("0: Exit\n");
        printf("Choose an option (0-9): ");
        scanf("%d", &select);

        switch (select) {
            case 1:
                setnull(&l);
                printf("List cleared.\n");
                break;
            case 2:
                printf("Length of the list: %d\n", length(&l));
                break;
            case 3:
                printf("Enter index to retrieve: ");
                scanf("%d", &i);
                get(&l, i);
                break;
            case 4:
                printf("Enter ID to locate: ");
                scanf("%d", &id);
                locate(&l, id);
                break;
            case 5:
                printf("Enter student ID, Name, and Age: ");
                scanf("%d %s %d", &s.id, s.name, &s.age);
                printf("Enter position to insert: ");
                scanf("%d", &i);
                insert(&l, i, s);
                break;
            case 6:
                printf("Enter position to delete: ");
                scanf("%d", &i);
                delete(&l, i);
                break;
            case 7:
                display(&l);
                break;
            case 8:
                printf("Enter name to search: ");
                scanf("%s", name);
                search_by_name(&l, name);
                break;
            case 9:
                printf("Enter ID to update: ");
                scanf("%d", &id);
                update_student(&l, id);
                break;
            case 0:
                printf("Exiting.\n");
                break;
            default:
                printf("Invalid choice. Please choose between 0-9.\n");
        }
    } while (select != 0);

    return 0;
}