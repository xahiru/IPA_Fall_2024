#include<stdio.h>


int converter(long long n) {
    int decimalNum = 0,i = 1,remainder;

    while (n > 0) {
        remainder = n % 10;
        dicimalNum += remainder * i;
        i *= 2;
        n /= 10;
    }

    return decimalNum;
}

int main() {
    long long binaryNum;


    printf("Enter a binary number: ");
    scanf("%lld" , &binaryNum);


    printf("Decimal : %d\n", converter(binaryNum));

    return 0;
}