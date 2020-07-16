#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* reverseString(char* s) {
    int start = 0;
    int end = strlen(s) - 1;
    char temp;

    while(start < end) {
        temp = s[start];
        s[start] = s[end];
        s[end] = temp;
        start++;
        end--;
    }

    return s;
}
