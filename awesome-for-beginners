#include <stdio.h>
#include <math.h>

int findNthDigit(int n) {
    long long base = 9;
    int digits = 1;
    long long start = 1;
    while (n > base * digits) {
        n -= base * digits;
        base *= 10;
        digits++;
        start *= 10;
    }
    start += (n - 1) / digits;
    int digitIndex = (n - 1) % digits;
    char numberStr[20];
    sprintf(numberStr, "%lld", start);
    return numberStr[digitIndex] - '0';
}
