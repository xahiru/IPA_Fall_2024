#include <stdio.h>
#include <stdbool.h>
#define MAX 100
char stack[MAX];
int top = -1;
void push(char c) {
    if (top <MAX -1){
        stack[++top] = c;
    }
}
char pop(){
    if (top != -1){
        return stack [top--];
    }
    return '\0';
}
bool isBalanced(char expr[]){
    int i;
    for (i=0;expr[i] != '\0'; i++){
        if (expr[i] == '(' || expr[i] == '{' || expr[i] == '['){
            push(expr[i]);
        } else if (expr[i] == ')' || expr[i] == '}' || expr [i] == ']'){
            if(top ==-1){
                return false;
            }
            char openBracket = pop();
        if ((expr[i] ==')' && openBracket != '(') || (expr [i] =='}' && openBracket != '{') || (expr[i == ']' && openBracket != '['])){
            return false;
        }
        }
    }
    return top == -1;
}

int main() {
char expr [MAX];
printf("Enter an expression: ");
scanf("%s",expr);
if (isBalanced(expr)){
    printf("Balanced\n");
} else {
    printf("Not Balanced\n");
}
return 0;
}
