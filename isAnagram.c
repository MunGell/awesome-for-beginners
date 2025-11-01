#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 100

int isAnagram(char str1[], char str2[]) {
    int count[256] = {0};
    int i;

    for (i = 0; str1[i] != '\0'; i++) {
        if (isalpha(str1[i]))
            count[tolower(str1[i])]++;
    }

    for (i = 0; str2[i] != '\0'; i++) {
        if (isalpha(str2[i]))
            count[tolower(str2[i])]--;
    }

    for (i = 0; i < 256; i++) {
        if (count[i] != 0)
            return 0;
    }

    return 1;
}

int main() {
    char str1[MAX], str2[MAX];

    printf("Enter first string: ");
    fgets(str1, MAX, stdin);
    printf("Enter second string: ");
    fgets(str2, MAX, stdin);

    str1[strcspn(str1, "\n")] = '\0';
    str2[strcspn(str2, "\n")] = '\0';

    if (isAnagram(str1, str2))
        printf("'%s' and '%s' are anagrams.\n", str1, str2);
    else
        printf("'%s' and '%s' are not anagrams.\n", str1, str2);

    return 0;
}
